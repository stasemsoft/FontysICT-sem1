# Sample class Animal caretaker

## Example
```cs
class Animal Attendant {
   private string Name;
   private DateTime InDienstSinds;

   public void SetName(string name) {
      Name = name;
   }

   public bool Take care(Monkey monkey) {
      // Take care of monkey...
      Console.Out.WriteLine( monkey.CreateSound() );
      return true;
   }

}
```

Here you see a new class, _Animal Caretaker_. This one has a name and an entry date. Each caretaker can also take care of a monkey. So you can see that you can also use other classes you create in self-created classes:

```cs
Animal Caregiver caregiver = new Animal Caregiver();
caregiver.SetName("Henk");
caregiver.Care(kong);
```

Try giving the caregiver a date of hire yourself. _DateTime_ is also a class.


### Example

```cs
class Player {

   private string Name;
   private int Number ofLives;
   private int Score;

   public void SetName(string name) {
      Name = name;
   }

   public void SetNumberLives(int lives) {
      NumberLives = lives;
   }

   public void EarnPoints(int points) {
      if (IsGameOver() == false) {
         Score = Score + points;
      }
   }

   public void LossLife() {
      if (IsGameOver() == false) {
         NumberLives = NumberLives - 1;
      }
   }

   // read carefully what is written here!
   public bool IsGameOver() {
      return (NumberLives <= 0);
	  // remember: (NumberLives <= 0) is already a Boolean.
   }

   public override string ToString() {
      return Name + ": " + Score;
   }

}
```

Here on the left you see a class for a player in a game. Each player has a name, a current score and a number of lives. There are three methods. The Earn Points method allows a certain number of points to be added to the player's score. However, this can only be done when the player is not yet game over.

A player is game over when the number of lives is 0 or lower. The player loses points using the LoseLife method. This will decrease the number of lives by 1 when the player is not yet game over.

What is Scott's total score in after executing the piece of code on the next page? Run the code for verification!

```cs
Player s = new Player();
s.SetName("Scott Pilgrim");
s.SetNumberofLives(3);
while (s.IsGameOver() != false)
{
   s.EarnPoints(100);
   s.LossLives();
}
Console.Out.WriteLine(s);
```