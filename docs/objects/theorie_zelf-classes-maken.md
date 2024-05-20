

# Dictation C# classes

# 1. Classes

A `Class` is a kind of *blueprint*. Think of it as a drawing of what something should look like and what that "thing" can do once you actually start making it. Of a boat you first make a `design`, a `design`: What kind of wood do you need? Where are the connections? What kind of engine will be in it? Et cetera. This design, the blueprint, cannot sail. You cannot float on it. Only when the boat is made can you do anything with it. You can even make several boats out of it! It's the same way with classes. A class is the blueprint for "something." You can't start working with it until you ***instance*** the blueprint: create an **object** of that ***type***.

Another comparison is that of a ***running belt***: Several things (objects) of a certain type can roll off a conveyor belt: Every time I call `new` to the class, an object of that type comes rolling off the conveyor belt. How the conveyor belt is 'programmed' determines what an object of that type can eventually do.

First we're going to look at some examples you already know. Then we are going to create our own **class**.

## 2.1. Using classes

You've seen the `class Random` before, probably without knowing it was a class. An example:

```cs
Random die = new Random();
int number = die.Next();
```

First, a variable of type Random named `dice` is created. (Yes, a `class` is a `type`, although in C# not all types are also a class). The `Random` here is the class, the assembly line: calling `new` against it (next line) creates a new object of this type and the variable `dice` refers to this object.  

We say that die is an `instance` (instance) or `object` of the Random class. Hence the term object-oriented: `Object Oriented Programming`, O.O.P. for short).

In the third line, you see that the die is used to retrieve a random number. So there you are using functionality described in the Random class. We then say that you call the `method` `Next` (`call`t) on the object `dice`.

Tip: You get a `NullPointerException` when you use an instance of a `class` without being created with new.

Your **form** is also a class. In each class you can program `fields` (variables, but outside a method) and `methods`. Look at the following little example (leave out `partial` and the addition `: Form`).

```cs
public partial class FormDemo : Form
{
   private Random die = new Random();

   public int ThrowDice();
   {
      return die.Next(1, 7);
   }

   private void buttonDoSomething_Click(object ...)
   {
      int number = ThrowDice();
   }

}
```

In the example, a `field` is added to form of type Random and named die. This is initialized immediately, on the same line still. In the rest of the program you can safely use the die.

A `method` has also been added to the form. This, like the variable, can be used anywhere in this FormDemo class. This is also done in the click `event handler` of the button. When the user presses the button, a *next* roll of the die will be thrown. The random number is returned by the Throw Dice method (`return value`). The output of this method is captured in an integer named `number`.


### Example existing class: StringBuilder
Below is another example of using a class.

```cs
StringBuilder welcome = new StringBuilder();
welcome.Append("Welcome ");
welcome.Append("at programming");
MessageBox.Show(welcome.ToString());
```

The StringBuilder class is used here. Also, try out the above piece of code for yourself. On the first line of code, a variable of type StringBuilder is created. The variable is called welcome and is initialized immediately. Via the 'Append' method, pieces of text can be added to it. This is displayed in its entirety, by calling the 'ToString()' method, to the user.

Try adding some `fields` and `methods` to your form yourself. See what you can do with them.

## 2.2. Creating your own classes

Imagine a boat with a speed, a name, a weight and a number of crew members. The boat can sail and can drop anchor. How would you create this in the software? Create all kinds of variables and separate methods? What if multiple boats are needed? Fortunately, for this kind of *complex type* we can create our own classes. Consider the following example.

```cs
class Boat
{
   private int Speed;
   private string Name;
   private int Weight;
   private int Number of Crew;

   // Below are the methods.
   public int GetSpeed() {
      return Speed;
   }

   public void SetSpeed(int speed)
   {
      Speed = velocity;
   }

   public void Varen(int speed) { ... }

   public bool AnchorEject() { ... }

}
```

In this example you should see all the aspects that were described in the piece of text above. This is how to create a class! This can be done very easily in Visual Studio by right-clicking on your C# project in the Solution Explorer and choosing 'Add' > 'Class'. Now you can enter a name for your class and you're done. Now you can add fields and methods. Just like with your form.

```cs
Boot boot = new Boot();
boat.Sailing(100);
MessageBox.Show("The speed is " ``+ boot.GetSpeed());
```

In the above example, you can see how to use a class of your own creation. Proprietary just like a variable of type Random. You create a variable of the appropriate type (in this case Boot) and initialize it with the `constructor` (which is a kind of method with the same name as the class). This all happens on the first line of the above piece of code. Now you can use the variable! You can call methods from it, such as `Boat` and `GetSpeed`.

```cs
Boot flDutch = new Boot();
Boat titanic = new Boat();
flDutch.GetSpeed();
titanic.GetSpeed();
```

Finally, above you can see one of the most powerful aspects of OOP. You can use any class to create multiple instances of it. Now I have two boats in my code! Each boat with its own interpretation. This way I can very easily add boats in the code.

Try creating and using your own class! What can you come up with and what will you do with it?