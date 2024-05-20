# Theory Property

A "property" gives you access to a "property" of a "property." You probably used properties before, now you learn how to make them yourself.

## Use of existing property

You've probably already seen the "property editor" in Visual Studio, especially if you've created a WinForm app. Here you can view and customize all kinds of _properties_ of a _Form_, _Button_, _TextBox_ and many other .

If you request the _Text_ of a _TextBox_ from code, or you specify a value, use properties.

```cs
string input = TextBoxInput.Text;
// dan een aantal berekeningen (weggelaten)
result = ...
// tot slot de uitkomst in een label terug:
LabelOutput.Text = result;
```

## Own properties for own objects

Suppose you have a Stopwatch class,
Then this one could have a private field seconds.
Do you want this field to be read only by other code,
you can create a property for this.
The convention is that fields are written with lowercase letters;
Properties are started with a capital letter.
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

Below are a few ways in which this class may not be used.

```cs
Stopwatch sw = new Stopwatch();
int tijd1 = sw.seconds;                  // Mag niet, omdat field seconds private is.
int tijd2 = sw.Seconds;                  // Mag wel (hoofdletter) omdat de property public is.
sw.Seconds = 10;                        // Mag niet (geen setter)
```

Another possibility is to set a field in a certain way. For example, we could make the stopwatch adjustable with minutes:

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
sw.Minutes = 5;                         // Instellen in minuten
int tijd = sw.Seconds;                  // Uitlezen in seconden (300)
```

## External bronnen

* [CSharp.Net tutorials](http://csharp.net-tutorials.com/classes/properties/)
* [MS programming Guide](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/properties)
* [CodeProject](https://www.codeproject.com/Articles/1006217/Diving-into-OOP-Day-Properties-in-Csharp-A-Practic)
* [MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370889(v=vs.85).aspx)

If you want to read more about properties, you can find a good explanation on MSDN (for now ignore the more extensive example under the example header).
[MSDN on properties](http://msdn.microsoft.com/en-us/library/w86s7x04.aspx)
