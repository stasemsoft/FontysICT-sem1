# Theory: Properties

A "property" gives you access to a "property" of an object. You've probably used properties before, now you'll learn how to create them yourself.

## Using Existing Properties

You've probably already seen the "property editor" in Visual Studio, especially if you've created a WinForm app. Here you can view and customize all kinds of _properties_ of a _Form_, _Button_, _TextBox_, and many other controls.

When you retrieve the _Text_ of a _TextBox_ from code, or specify a value, you're using properties:

```cs
string input = TextBoxInput.Text;
// then some calculations (omitted)
result = ...
// finally, put the result in a label:
LabelOutput.Text = result;
```

## Creating Properties for Your Own Objects

Suppose you have a Stopwatch class,
which could have a private field for seconds.
If you want this field to be read-only by other code,
you can create a property for it.
The convention is that fields are written with lowercase letters;
Properties start with a capital letter.
See the example below:

```cs
class Stopwatch
{
    private int seconds;                // Field
    public int Seconds                  // Property
    {
        get { return seconds; }         // Getter
    }
}
```

Below are examples of how this class can and cannot be used:

```cs
Stopwatch sw = new Stopwatch();
int time1 = sw.seconds;                 // Not allowed, because field seconds is private
int time2 = sw.Seconds;                 // Allowed (capital letter) because the property is public
sw.Seconds = 10;                        // Not allowed (no setter)
```

Another possibility is to set a field in a specific way. For example, we could make the stopwatch adjustable with minutes:

```cs
class Stopwatch
{
    private int seconds;                // Field
    public int Seconds                  // Property
    {
        get { return seconds; }         // Getter
    }
    public int Minutes                  // Property
    {
        get { return seconds / 60; }    // Getter
        set { seconds = value * 60; }   // Setter
    }
}

Stopwatch sw = new Stopwatch();
sw.Minutes = 5;                         // Set in minutes
int time = sw.Seconds;                  // Read in seconds (300)
```

## External Resources

* [CSharp.Net tutorials](http://csharp.net-tutorials.com/classes/properties/)
* [MS programming Guide](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/properties)
* [CodeProject](https://www.codeproject.com/Articles/1006217/Diving-into-OOP-Day-Properties-in-Csharp-A-Practic)
* [MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370889(v=vs.85).aspx)

If you want to read more about properties, you can find a good explanation on MSDN (for now ignore the more extensive example under the example header).
[MSDN on properties](http://msdn.microsoft.com/en-us/library/w86s7x04.aspx)
