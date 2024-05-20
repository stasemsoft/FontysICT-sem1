# GUI vs. Domain

## Starting point

A (possibly previously created) program that contains a number of classes
in it and a User Interface (possibly Graphical).
(We will assume a Console app here for the story)

The customer appears satisfied and wants a new version of the program:
this new version should do the same thing, but from a WinForms app.

## Approach

Idea: Working solution with 3 projects: 1 class library, 1 (e.g.) WinForms, 1 Console

- MsgBox.Show vs Console.WriteLine
- Console.Readline vs textbox.Text
- Method that throws an exception that is then caught in the GUI.