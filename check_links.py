#!/usr/bin/env python3
"""Check for broken links in markdown files."""

import re
import os
from pathlib import Path
from urllib.parse import urlparse

def extract_links(content, file_path):
    """Extract all links from markdown content."""
    links = []
    
    # Remove code blocks to avoid extracting links from code examples
    # Match code blocks: ```language ... ```
    code_block_pattern = r'```[\s\S]*?```'
    content_without_code = re.sub(code_block_pattern, '', content)
    
    # Also remove inline code: `code`
    inline_code_pattern = r'`[^`]+`'
    content_without_code = re.sub(inline_code_pattern, '', content_without_code)
    
    # Match markdown links: [text](url) or ![text](url "alt")
    pattern = r'\]\(([^)]+)\)'
    for match in re.finditer(pattern, content_without_code):
        link = match.group(1)
        # Skip anchor-only links
        if link.startswith('#'):
            continue
        # Handle angle brackets around URLs: <https://...> -> https://...
        if link.startswith('<') and link.endswith('>'):
            link = link[1:-1]
        # Remove quotes and alt text from image links
        # Handle: figures/image.png "alt text" -> figures/image.png
        # Handle both regular and smart quotes (including Unicode curly quotes)
        # Unicode left/right double quotes: \u201c \u201d
        # Unicode left/right single quotes: \u2018 \u2019
        # Use regex to remove everything after any quote character (including Unicode)
        link = re.sub(r'["""''\u201c\u201d\u2018\u2019].*$', '', link)
        # Remove any trailing spaces or quotes (including Unicode)
        link = link.rstrip('"').rstrip("'").rstrip('"').rstrip("'").rstrip('\u201c').rstrip('\u201d').rstrip('\u2018').rstrip('\u2019').strip()
        if link:
            links.append(link)
    return links

def check_link(link, source_file):
    """Check if a link is valid."""
    source_dir = source_file.parent
    
    # Handle GitHub Pages links FIRST (before general external links)
    # These are links to the GitHub Pages site and should be treated as valid
    if 'stasemsoft.github.io' in link or 'stasemsoft.github.io/FontysICT-sem1' in link:
        return {'type': 'github_pages', 'valid': None, 'link': link}
    
    # Handle external links (http/https)
    if link.startswith('http://') or link.startswith('https://'):
        return {'type': 'external', 'valid': None, 'link': link}
    
    # Handle mailto links
    if link.startswith('mailto:'):
        return {'type': 'mailto', 'valid': None, 'link': link}
    
    # Handle relative links
    # Remove anchor if present
    link_path = link.split('#')[0]
    if not link_path:
        return {'type': 'anchor', 'valid': True, 'link': link}
    
    # Resolve relative path
    if link_path.startswith('/'):
        # Absolute path from repo root
        target = Path('.') / link_path.lstrip('/')
    else:
        # Relative to source file
        target = (source_dir / link_path).resolve()
    
    # Normalize path
    try:
        target = target.resolve()
        exists = target.exists()
        
        # If target doesn't exist, check common variations
        if not exists:
            # Check if it's a directory with index file
            if target.is_dir():
                for index in ['readme.md', 'index.md', 'README.md', 'index.html']:
                    if (target / index).exists():
                        exists = True
                        break
            else:
                # Check if it's a file without extension (try .md)
                if not target.suffix:
                    md_target = target.with_suffix('.md')
                    if md_target.exists():
                        exists = True
                        target = md_target
                    else:
                        # Check if it's a directory
                        if target.is_dir():
                            for index in ['readme.md', 'index.md', 'README.md']:
                                if (target / index).exists():
                                    exists = True
                                    break
    except:
        exists = False
    
    return {
        'type': 'internal',
        'valid': exists,
        'link': link,
        'resolved': str(target)
    }

def main():
    """Main function to check all links."""
    base = Path('.')
    broken_links = []
    all_links = []
    
    # Find all markdown files
    md_files = list(base.rglob('*.md'))
    
    print(f"Checking {len(md_files)} markdown files...\n")
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            links = extract_links(content, md_file)
            
            for link in links:
                result = check_link(link, md_file)
                result['source_file'] = str(md_file.relative_to(base))
                all_links.append(result)
                
                if result['type'] == 'internal' and not result['valid']:
                    broken_links.append(result)
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    # Report results
    print(f"Total links found: {len(all_links)}")
    print(f"Broken internal links: {len(broken_links)}\n")
    
    if broken_links:
        print("=" * 80)
        print("BROKEN LINKS FOUND:")
        print("=" * 80)
        for link_info in broken_links:
            print(f"\nFile: {link_info['source_file']}")
            print(f"  Link: {link_info['link']}")
            print(f"  Resolved to: {link_info.get('resolved', 'N/A')}")
    else:
        print("✅ No broken internal links found!")
    
    # Summary of link types
    external_count = sum(1 for l in all_links if l['type'] == 'external')
    github_pages_count = sum(1 for l in all_links if l['type'] == 'github_pages')
    internal_valid = sum(1 for l in all_links if l['type'] == 'internal' and l['valid'])
    
    print(f"\n{'=' * 80}")
    print("SUMMARY:")
    print(f"  External links: {external_count} (not checked)")
    print(f"  GitHub Pages links: {github_pages_count} (not checked)")
    print(f"  Valid internal links: {internal_valid}")
    print(f"  Broken internal links: {len(broken_links)}")

if __name__ == '__main__':
    main()

