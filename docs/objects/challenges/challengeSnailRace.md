# Challenge SnailRace

### Introduction

For the **Great Snail Race 2025**, starting from an empty project with Visual Studio
an application must be created to run a Snail Race.

1. Create a new Windows Form Project.
2. Rename 'Form1' to 'SnailRaceForm'. If you do this by *renaming* the *file* in the *Solution Explorer* Visual Studio suggests that it renames the *Code Element* (in this case the Form) as well: great!
Create a new class Snail. `Ctrl+Shift+A` (or right-click on project in *Solution Explorer*), type a *class name*/*file name* and `OK`.
4. On the Form, put 5 PictureBoxes, right under each other, use the image 'snail.jpg' for each. If you do it smart you drag 1 onto your *Form*, add an image to it and copy the *PictureBox* several more times (use `ctrl+C` and `ctrl+V`).
5. Add a button with Text 'Race'.
6. In class Snail, create a constructor with (for now) 2 parameters:
	1. int minimumSpeed
	2. int maximumSpeed
7. Add 2 private Fields (also called member variables or instance variables):
	1. minimumSpeed
	2. maximumSpeed
8. Class Snail should now be given a `Field` 'pictureBox' of type PictureBox (to do this, add at the beginning of the file: `using System.Windows.Forms;`). Note: a *professional software engineer* would not do it this way: If you already know a better way do it that way! Fields we always make private.
9. Add a `Field` to the Form (so outside a method declared) of type List&lt;Snail&gt;:

```cs
List<Snail> snails = new List<Snail>();
```

10. In SnailRaceForm_Load (if you don't already have it, double-click the Form), add the following code:

```cs
snails.Add( new Snail(2,8) );
snails.Add( new Snail(1,8) );
snails.Add( new Snail(4,6) );
snails.Add( new Snail(3,8) );
snails.Add( new Snail(3,9) );
```

11. Invent (and realize) a way to let each snail know which PictureBox belongs to it.
12. Add another narrow but high PictureBox to the right of the screen.
13. When button Race is clicked, all snails slide to the right in turn until the first one(s) hit the wall.
	Note that all snails must be given the same number of turns.
	2. In class Snail, add a method 'SlideA Piece()'that adjusts the X value and returns a boolean value: true if that snail hit the wall in that turn, and false otherwise.
	3. A MessageBox reports the winner(s) afterwards.
	4. Use 1 Random object in the whole program.
	5. Keep with the 'step size' of each snail with its minimum and maximum speed. For example a snail that has minimum 3 and maximum 6 must step up a random number between 3 and 6 per turn (Whether the values 3 and 6 are also allowed is up to you).
14. Each winner gets an amount of money. This amount can change later but at the moment it is 12.25 euros. Add labels with the amount each racer has earned so far. Use string formatting for this.