# Challenge Word Finder


| Version | 1 - Jan Oonk |
| --- | --- |
| Level | 4 or 5.
| Learning Objectives | Class, Property, Constructor, private/public, UI separation, algorithm, file read/write. |
| Prior knowledge required | Method, GUI, Basic Types, If. |
| Challenge Type | Programming, Algorithm.


![woordenzoeker](figures/woordenzoeker.png "woordenzoeker")

Based on a set of words (from a text file), generate a word search puzzle of a specified width x height. Words are hidden both horizontally (left-right whether eighth-front or not) and vertically (top-bottom whether rear-front or not).

Make sure the words stay within the playing area and do not "wrap" to the other side of the playing area.
Then the player should be able to search for the words. Part of the player screen consists of overview of words to be searched and other part is the playing field of letters.

The player can mark words in the playfield by selecting letters using the left button of the mouse. A letter that has already been selected is de-selected when clicked again. The selected letters are automatically checked after clicking.
Letters can only be selected in the same direction as the previously selected letter(s).

If the selected letters are recognized as a word in the list of hidden words then this word is crossed out.
While selecting letters, they are circled in orange.

If the selected letters form a word yet to be searched for, the circles turn permanently green.

Letters can be selected more often and be part of multiple words.

Show a timer how long the player has been playing.


## Concepts

+ Sure: Class, constructor, private/public, property, field, method, file handling, enum, List.
+ Most likely: method/constructor overloading, UML, exceptions, static, casting.
+ Possibly: XAML


## Resources

+ [Sprite Font Generator](https://www.scirra.com/forum/sprite-font-generator-v3_t86546)
+ [Write Text on a Bitmap](https://stackoverflow.com/questions/6311545/c-sharp-write-text-on-bitmap)
+ [Sound Engine](https://www.ambiera.com/irrklang/downloads.html)
+ [Database connectie e.d.](http://csharp-station.com/Tutorial/AdoDotNet)
+ [Webclient](https://msdn.microsoft.com/en-us/library/system.net.webclient(v=vs.110).aspx)
+ [How to: Request Data Using the WebRequest Class](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/how-to-request-data-using-the-webrequest-class)
+ [What difference is there between WebClient and HTTPWebRequest classes in .NET?](https://stackoverflow.com/questions/4988286/what-difference-is-there-between-webclient-and-httpwebrequest-classes-in-net)
+ [JSON Parser](https://www.newtonsoft.com/json)

## Variation / additional features:
+ level 1 - save the high scores (is elapsed play time) and player name to a file.
+ level 1 - add variation, via a menu option, to search numbers instead of words.
+ level 1 - difficulty of the puzzle to be generated can be set via a start menu or the like, e.g. by putting words more often backwards in the puzzle, diagonally.
+ level 1 - Once all the words have been found, the player must put the remaining letters in the correct order to form a word or correct sentence.
+ level 1 - categorize the words into themes, so that hidden words are all related to each other e.g. category/theme Plants, Movies or similar.
+ level 1 - Get the words, which are hidden in the puzzle to be generated, from a database instead of a file. Create a simple database model and design first.
+ level 1 - Add nice soundeffects to certain events like correct word, incorrect word, letter select, puzzle finish etc.
+ level 1 - When escape is pressed, any selected letters are deselected.
+ level 1 - Build in 2nd letter selection way: letters can also be selected by holding and dragging the left button. All letters are selected between initial letter and mouse position. On release, the word formed by the selected letters is checked. If it is wrong/not right yet, it can be selected again in the same direction (by the normal way or this new way), so the previous selected letters remain active (orange).
+ level 1 - If you select letters by clicking on them and you do not select the next letter in the same direction and/or the letter is not connected to 1 of the previously selected letters then all these selected letters will be deselected.
+ level 2 - store the high scores in a central place (file or database). Create a simple web service for this purpose.
+ level 2 - players like to compare their high scores in a fair way, so make sure that the puzzles are presented in exactly the same way to the different players, so all letters in a puzzle and hidden words are in exactly the same place. Display high scores for each puzzle. To do this, give each puzzle a unique name or id. Show this in a selection menu so you can load a particular puzzle.
+ Level 3 - Soon the highscore webservice (see previous extension) turns out to have been hacked by script kiddies who managed to figure out the url. Devise a way to secure the web service so that unrealistic or unjustified high scores cannot be sent to the web service.