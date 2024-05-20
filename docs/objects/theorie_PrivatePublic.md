# Private and Public

### Private
- Information hiding*: `Fields` within a `class` are always made `private`.
- Advantage: better maintainable software, programmers can not just enter the *internals* of your `class` from other `classes`, but use the appropriate `methods` and/or `properties`.


### Methods
`Methods` that must be callable from the outside are thus typically `public`. If they are `methods` that are only meant to be used within the `class` you better make them `private`.

### Properties
A property often defines a way to retrieve or even change the value of a field. The retrieval can often be `public`, but for most fields it is not intended that the value can be changed from the outside.

```cs
class Person
{
   // Make Fields private
   private string name;
   private int age;

   public Person(string Name, int Age)
   {
      this.name = Name;
      this.age = Age;
   }

}
```

It is now not possible to externally change the value of a `field` like `age`:

```cs
Person person = new Person("Pietje Puk");
int age = person.age; // so this does NOT work!
```

Of course, in `class` *Person* a `method` can be created that returns the value of `field` *age*, a so-called *get-method*:

```cs
public int GetLife()
{
   return this.age;
}
```

so that the age can be retrieved:

```cs
int age = person.GetAge();
```

Note that the *age* cannot therefore be changed from the outside, only queried!

### Why?

So what is the advantage of this? Well, within a year, the developer of this `class` will get the first complaints that not the ages are not calculated correctly, since that the *age* is not a fixed value: at the moment the *person* has a birthday, the value must be incremented.
In this case, you can see that it is wiser to store the *date of birth* of the person (since it does not change) and then when the *age* is requested, the correct value is calculated.
The programmer can now change the `class` without any problems:

```cs
class Person
{
   // fields
   private string name;
   private DateTime date of birth;

   public int GetLife()
   {
      int age;
      ... // add code here to calculate the age using the date of birth.
      return age;
   }
```

Because the field *age* was `private` the programmer can change it without causing problems elsewhere in code that uses it, external code calls the method *GetAge()* and it will work without problems after the change.



### Encapsulation
Suppose there is a bug in (the value of fields of) a certain `class`, then it is also nice to know that (in case of `private` fields) the bug must be somewhere in the `class`. This is called `Encapsulaton`: a piece of behavior of a program is shielded. This makes it easier to reuse part of your program.
Encapsulation simply means that a group of fields, methods and other properties
are seen as a single, delimited unit or object.
This sounds a bit dry, so another wording that may be clearer is
by viewing encapsulation as the ability of a class to keep fields and methods
that are of no interest to others.
The best reason to shield certain parts of your class is to make your code easier to use. Classes use private fields to keep track of their state; how many lives do I have left, how fast can I move, et cetera. This information is not necessarily of interest to other code, but it is essential to the operation of the class. If everyone could just change the fields, the functioning of your class becomes a lot more unreliable and random: if you are the only one who can change the number of lives, you know exactly where in your code it can happen that your lives are set to 0. This advantage falls away if everyone can adjust the number of lives.
### External References

+ [Over private](https://softwareengineering.stackexchange.com/questions/143736/why-do-we-need-private-variables)
+ [Techopedia](http://www.techopedia.com/definition/3787/encapsulation-c)
