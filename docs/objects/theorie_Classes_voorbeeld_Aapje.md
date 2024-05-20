# Example class Monkey

## Example
```cs
class Monkey {
   private string Species;
   private int Age;

   public void SetSpecies(string species) {
      Species = species;
   }

   public string CreateSound() {
      return "Oek oek oek."
   }

   public override string ToString() {
      return Kind + " says " +
      CreateSound();
   }

}
```

Here a class _Monkey_ is created. Each monkey you create in the code is of a certain kind and has an age. The age is an integer and the type of monkey is a string.

Create a monkey with:

```cs
Monkey kong = new Monkey();
kong.SetSpecies("Gorilla");
```

Each monkey can also be rendered as a string using the ToString method. Try it out for yourself:

```cs
Console.Out.WriteLine(kong);
```