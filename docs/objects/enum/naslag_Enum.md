# Baseline knowledge: Enum

## Enum

An enum is a data type that can contain a number of predefined values, for example, the days of the week, the months of the year, the colors of the rainbow, etc.

An enum is defined with the keyword `enum` and the name of the enum. The values are placed between curly braces `{}`.

```C#
enum Color
{
    Red,
    Green,
    Blue
}
```

The values of an enum can be retrieved with the name of the enum followed by a period and the name of the value.

```C#
Color color = Colour.Red;
```

An enum can only hold a limited amount of data, viz.
`int`, `uint`, `long`, `ulong`, `short`, `ushort`, `byte` or `sbyte`.

(Also `char` is a possibility, but why this is is fun to figure out for yourself!)

To indicate which type to use, this can be placed after the enum name.

You can also assign your own values to an enum, for example:

```C#
enum Color
{
    Red = 1,
    Green = 2,
    Blue = 3
}
/*
    This below is also valid, but less neat. For better code, use the above way, then it is also immediately clear which value belongs to which color.
*/

enum color
{
    Red = 1,
    Green,
    Blue
}
```

Logical conditions (and even arithmetic operations) can be performed on enums.

```C#

enum Colour
{
    Red = 1,
    Green = 2,
    Blue = 3
}

public void Test()
{
    Colour colour = Colour.Red;
    if(color == Colour.Red)
    {
        Console.WriteLine("Colour is red");
    }
    if(colour == Colour.Green)
    {
        // Do something else
    }
    if(color == Colour.Blue)
    {
        // Do something else
    }

    Colour newColour = colour + 1;
    Console.WriteLine(newColour);
}
```

Outcome:

```md
Color is red
Green
```

Enums are mainly used to easily switch between types, or pass data in a simple way.

### Example

```C#

enum Vehicle
{
    Plane,
    Boat,
    Car
}

public string GetLicenseFromType(Vehicle type)
{
    switch(type)
    {
        case Vehicle.Plane:
            return "Pilot license";
        case Vehicle.Boat:
            return "Boat license";
        case Vehicle.Car:
            return "Driver license";
        default:
            return "No license";
    }
}
```