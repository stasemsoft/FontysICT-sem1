# Example class Monkey

## Example
```cs
class Monkey {
   private string species;
   private int age;

   public void SetSpecies(string species) {
      this.species = species;
   }

   public string CreateSound() {
      return "Oek oek oek.";
   }

   public override string ToString() {
      return species + " says " +
             CreateSound();
   }

}
```

Here a class _Monkey_ is created. Each monkey you create in the code has a species and an age. The age is an integer and the species is a string.

Create a monkey with:

```cs
Monkey kong = new Monkey();
kong.SetSpecies("Gorilla");
```

Each monkey can also be rendered as a string using the ToString method. Try it out for yourself:

```cs
Console.Out.WriteLine(kong);
```