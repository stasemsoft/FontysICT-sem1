| Level | 3 of 5 |
| ------------------- | ---------------------------------- |
| Learning Objectives | Class, constructor, object, field. |
| Prior knowledge required | Basic knowledge about objects.         |
| Challenge Type | Realize.                        |


### Introduction
In this assignment we are going to program a game called "Invaders!!!". In this game you are the defender of the earth, and you protect our earth from the invading creatures. You have to prevent the creatures from landing on the earth and destroying a city, by clicking on them with the mouse.
If you shoot at a creature by clicking on it it loses a life and goes back to the top of the screen to try to land on the earth again. Creatures that reach the bottom of the screen count as "landed" and destroy a city. If all creatures have lost all their lives the player wins, however, if all cities are destroyed the creatures win.
### Assignment
Program the game Invaders!!! where your program must meet the following requirements:
1. Your program contains a class Invader with private fields Position and Lives. Position is the y-coordinate of the invader on the screen and Life is a number starting at 5 (each time the user clicks on an invader with the mouse, the Life field is decreased by one).
2. The constructor sets the starting value of Levens to 5.
3. Invaders can move (from top to bottom), die (when they run out of lives) and they should have the ability to lower their lives (when you click on them). Program that nicely with methods in the class Invader (and then call those methods from your form.
4. In your form, create an array of 6 Invader objects and use those to further program the game in the form.