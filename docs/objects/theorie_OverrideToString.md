# override ToString()

```cs
class Person {

   // Field
   private string name;

   // Property
   public string Name
   {
      get { return this.name; }
   }

   // ctor
   public Person(string name)
   {
      this.name = name;
   }

   public override string ToString()
   {
      return this.name;
   }
}
```


Programming tip: put your own objects in the user interface. By this we mean that you put objects themselves in the UI, not strings or other variables. For example, to add a Person object to a listbox:

```cs
listBox1.Items.Add(new Person("Sjakie"));
```

Use casting to retrieve the object from a UI control:

```cs
Person p = (Person)listBox1.Items[2];
```

Program a `ToString()` method into all your `classes` to ensure that you always have a good textual representation of your objects.
# Extra 

+ [video 57, kudvenkat, override ToString()](https://www.youtube.com/watch?v=MwPZLPNR3ns&t=0s&list=PLAC325451207E3105&index=57)
+ [docs.microsoft about ToString()](https://docs.microsoft.com/en-us/dotnet/api/system.object.tostring?view=net-5.0)
+ [docs.microsoft about ToString()](https://docs.microsoft.com/en-us/dotnet/api/system.object.tostring?view=net-5.0)
+ [pptx](knowOverrideToString.pptx)
