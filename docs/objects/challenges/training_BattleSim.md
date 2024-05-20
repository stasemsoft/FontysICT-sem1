# Training BattleSim

| Date                     | Week 11/12                                                   |
| ------------------------ | ------------------------------------------------------------ |
| Version                  | 1 - Inge van Engeland                                        |
| Learning Objectives      | Class, Property, Constructor, private/public, UI separation. |
| Required prior knowledge | Method, GUI, Basic Types, If.                                |
| Challenge Type           | Programming                                                  |

![sim](figures/BattleSim.png "battlesim")


### Introduction
In the game BattleSim you can fight with two players against each other.
In this version, the left player is a Knight and the right player is a Ranger.
Both players have 100 hit points each.
It is a turn-based game, so in turns the players attack each other.
The strength of the attack is between 0 (one miss) and 30.
If the player takes a hit of more than 25, you have a "Critical hit."
The moment the number of hit points is 0 or less,
then, unfortunately, that player has lost.


### Assignment
Program the BattleSim. Figure
[](#fig:BattleSim)
is an example of what the screen might look like.

BattleSim command

- Create a class Player, it has a name and a number of hit points.
- Create the properties and constructor for this class.
- The class Player has a method to receive damage and a method to give damage.
- An attack gives 0-30 damage.
- If the attack is 0, it is a miss (give a message that it was a miss).
- If the attack is 25+, it is a "Critical Hit" (give a message).
- After each attack, the hit points are updated on the screen.
- If the number of hit points is 0 or less, then that player has lost.
- Characters take turns attacking.
- When it is one player's turn, the other player cannot click the "Attack" button.


### Extra
Make up features to expand your BattleSim. For example:
- Picture that changes when the player has won / lost
- Start screen where you can choose a character and give it a name
- An "Explore" button with which you can find a health potion, for example.
- Keep track of hit points in a Progress Bar.
- Weapons, armor etc.