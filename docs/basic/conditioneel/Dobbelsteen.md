# Training - Dices and Randomness

If you want to program a game, even the simplest games (tic-tac-toe) encounter the problem: how do I program randomness? How do I make a random move? How do you program that?

To experience this, you will write a small program that simulates the random behavior of a dice. If this so-called "proof-of-concept" program works, you will have a better understanding of how to consider the necessary randomness during design and have more certainty about the game's chances of success.

## Assignment
Create a user interface with 6 picture boxes and a button that looks like this:
![[Dobbelsteen-ui.png]]

There are six objects of type **PictureBox** and a "Roll dice!" button on the form. The **PictureBox** objects are all invisible when the program is running (the **Visible Property** is set to **false**).

The goal is that every time the "Roll dice!" button is clicked, exactly one random PictureBox becomes visible. The other picture boxes become invisible. Program this functionality.

## Extensions
- Level * - Place all **PictureBox** objects exactly on top of each other (so it looks like the same dice is being rolled again each time).
- Level ** - Use a single switch statement (tip: Search the internet for a source) instead of multiple "if ... else ..." statements.

## Checklist
If you have completed the assignment correctly, you have met the following points:
- When the program starts, no dice images are visible.
- When the button is pressed, exactly one dice image becomes visible.
- When the button is pressed again, exactly one image (this may happen to be the same one) of a dice becomes visible.
- If you click the button dozens of times in a row, you will see the images for dice 1, 2, 3, 4, 5, and 6 shown at least once.
- If you click the button dozens of times in a row, two images are never shown at the same time.
- You have not used more "if ... else ..." constructs than necessary.
- You have code lines in each "if ... else ..." construct in the "if" block.
- You have code lines in each "if ... else ..." construct in the "else" block or you have omitted the "else" block.
- Extension a: Regardless of the value rolled, the image with the number of eyes is always shown in the same place.
- Extension b: Besides the "switch" statement, you have not used any more "if ... else ..." statements and you have not used a "default" case within the switch statement.

## Resources
- [Choice structures](https://stasemsoft.github.io/softwarematerial/docs/basic/conditioneel/naslag_Keuzestructuren.html)
- [Random class Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/api/system.random?view=net-5.0)