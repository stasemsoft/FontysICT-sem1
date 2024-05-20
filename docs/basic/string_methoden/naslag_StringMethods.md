# Basic knowledge: String operations (String methods)

Some common String functions are demonstrated and briefly explained below.
This document is written as a *naslag work*,
it is not specifically written to teach how to program with variables.


## String merging
The `plus` character allows strings to be concatenated together.
```cs
string text = "a text."
string words = "Says here."
string s = words + text;
```

The `s` `variable` is given the value `"Here is a text."` Note that spaces are not automatically added.
```cs
  string text = "text."
  string words = "Here stands";
  string s = words + " a " + text;
```

The &quot;+&quot;sign allows strings to be concatenated together. The &quot;s&quot; variable here is given the value &quot;Here is a text.&quot;

## IndexOf

Determine the position of a String within another String:
The *Position* variable is given the value `1`.
Note that the position of the first &quot;e&quot; found in the String is
is found (counting from `0`):
```cs
string text = "line of text";
int position = text.IndexOf("e");
```

Multiple letters can also be searched for in sequence:
```cs
string text = "line of text";
int position = text.IndexOf("tek");
```

The &quot;Position&quot; variable is given the value 6.
**Not found** returns `-1`:
```cs
string text = "line of text";
int position = text.IndexOf("a");
```
The &quot;Position&quot; variable is given the value -1. So the value -1 means: the String does not occur within the other String.

## Substring

Copy a piece from a string:
```cs
string text = "line of text";
string partText = text.Substring(0, 1);
```

which results in the value &quot;r&quot; appearing in partText because exactly 1 letter is copied from the original text starting from position 0.

Some more examples with Substring.
```cs
"abc".Substring(0,1) // this gives "a" (start from character with index 0, take 1 character)
"abc".Substring(0,2) // this gives "ab" (start from character with index 0, take 2 characters)
"abc".Substring(1,1) // returns "b" (start from index 1, take 1 character)
```
Good exercise: type this once into a Console app, try to predict what comes out and print the value with `Console.WriteLine()`, check to see if what you thought is correct. Play around with this until you understand how it works. Then I'm sure you'll be able to predict what comes out of this as well:

```cs
Console.WriteLine("abcdef".Substring(1,1)); // How long and what letters?
// Enter line by line (after seeing if you understand line before it):
Console.WriteLine("abcdef".Substring(3,2));
Console.WriteLine("abcdef".Substring(0,6));
// What would happen to:
Console.WriteLine("abcdef".Substring(0,7));
// or at:
Console.WriteLine("abcdef".Substring(7,1));
// important that you saw what happens at those last 2!
```


```cs
string text = "line of text";
string partText = text.Substring(6, 5);
```
This code results in the value &quot;text&quot; appearing in partText because exactly 5 letters are copied from the original text starting from position 6.

## Length

Define the number of characters in a string. Behind `Length
no open and close parenthesis because it is
a `property` (property) of the string and not a `method`
that you execute.
```cs
string text = "line of text";
int length = text.Length;
```

This code results in the value `11` appearing in length because the text is exactly eleven long. Note: this includes spaces in the text.
The `double quotes` to indicate beginning and end of the String value are not included.
```cs
string text = "";
int length = text.Length;
```

This code results in the value `0` appearing in *length*
because there are no characters in the string.