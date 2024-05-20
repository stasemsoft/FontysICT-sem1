# String methods
## Introduction
In this assignment, you will work with string methods. You use those methods to filter information from a piece of text, edit a piece of text, and determine where a particular word is in the text.

+ Learning Objective 1: You can write a small C# program from a given specification using the string methods IndexOf, Replace, and Substring. You know all the variants of these string functions.
+ Learning objective 2: You can work with multiple projects in a solution.
+ Learning objective 3: you can independently give property's of user interface components a value in C#.

## Preparation
Create a Windows Forms application in Visual Studio with a form containing a Textbox, a Button and a Label. Read through the OIS dictum and master the theory of string methods (also called string functions) IndexOf, Replace and Substring.

## Assignments
### Assignment 1 - Index of 'e'

```
User requirement:
The user types (in the Textbox) any text. After this, the user clicks on the button. The program then displays in the label the (first) index of the letter "e". The program shows in the label -1 if the letter e does not occur in the entered text.
```

Program the above user requirement.

### Task 2 - Haxor
Create a second project within your solution and on the form again put a Textbox, a Label and a Button.

```
User requirement: the user types any text and presses the button. The program then displays the entered text in the label in the so-called haxor notation.
```

Program this user requirement.

**Haxor notation**:
+ Each letter a is replaced by a 4.
+ Each letter s is replaced by a 5.
+ Each letter e is replaced by a 3.
+ The letters v and V shall be replaced by ____ .
+ The letters m and M shall be replaced by ________.


### Assignment 3 - Hello you!
Create a third project within your solution and put a Textbox, two Radiobuttons and a Button on the form. One Radiobutton will be labeled "Male" and the other Radiobutton will be labeled "Female".

```
User requirement: the user types his first and last name. For example, "Marietje Jansen." And ticks a radio button with his gender (for example, "Female"). The program then displays a MessageBox with the text "Hello Miss Jansen" or "Hello Mr. Jansen," depending on the text entered and radio button selected.
```

Note the requirements:
1. The user enters First Name + Last Name, but the MessageBox displays the text without the first name.
2. Input as "Jan de Graaf" and radio button gender "Man" produces the message "Hello Mr. de Graaf".


### Additional commands
Too easy or need more practice? Then make these extras.

1. Expand assignment 1 so that the whole thing becomes "case insensitive." So an e or an E in the input text will produce the same result.
2. Extend command 2 so that a Haxor text can be converted to readable text. To do this, add a Checkbox that allows the user to specify whether he wants to convert from text->Haxor or from Haxor->text.
3. Extend command 3 so that when input as "Jan de Graaf" it shows the text "Hello Mr. Graaf, the" by using the string method LastIndexOf. Extend command 3 so that input like " jan janssen " (with lots of spaces at the beginning, at the end and in between) still works. So output is "Hello Mr. Janssen" (without extra spaces).

(May 19, 2015 coined by Marcel Veldhuijzen)