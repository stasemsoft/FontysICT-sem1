# Challenge Four-in-a-row
	   
| Learning Goal      | Class, method, constructor, object, private, enum. |
| ------------------ | -------------------------------------------------- |
| Extra              | Algorithm,                                         |
| Required Knowledge | Object, Method, If.                                |
| Challenge Type     | Programming.                                       |


## Four in a row

### Analysis, Design, Realization

Ideal if you can do the Analysis (What should the product do?) and the Design (How will the product do it?) on a whiteboard where you stand with a group of people. Talk about what _classes_ you think you'll need if you're going to program **Four** **on** **a** **Row**. Try **together** to reach a good end result.

When you have thought of all the _classes_, then think of what exactly you would call those classes: write those names down. Remember that also the _current_ _state_ of the game must be stored in objects.

Note the following:
+ A ***class name*** starts with and ***Capital letter*** and is ***single***: so `class Student`, not `class Students`.
+ In a compound name, each new word begins with a _capital letter_, so
	+ `CamelBump`
	+ `StudentResult`
	+ `ChessBoard`


Create the game 4 in a row where you can play against the computer.
Keep in mind the requirements below:


+ Program class *Set* with two `integer` `properties` Row and Column
(the property Row is read-only, it is computed as the stones fall down). The constructor accepts a reference to class Game (see below) and an integer column.
An enum Field with possible values Red and Yellow.

```cs
enum Field {Red,Yellow}
```

+ Class Game with internally a private array of 6 by 7 (two-dimensional array)

```cs
Field[] board:
board = new Field[6,7];
```

+ It is preferably a console application. The game board need not be printed. May be, but with `Console.WriteLine`s (then run through the array and print it step by step).
+ The class Game has methods like `CreateASet()` to come up with the best move for the computer and `AcceptASet(Set z)` (to accept a move from the user).
+ The method `ConsiderAndSet()` can initially look for the first best free column. If there is no more free column then the method `SimilarPlay()` can be called which stops the game. Create private auxiliary methods such as bool `HasPlayerWon()` and `bool HasComputerWon()` that you call yourself.

```cs
private Random Edge;

public SetAndSet()
{
   return new Put(Edge.Next(7));
}
```