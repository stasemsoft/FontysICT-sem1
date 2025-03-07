# Enum

## Definition of Enum
- Enumerations (or enums for short) allow you to represent items in a structured, ordered way.
- An enumeration allows elements to be addressed by a name. (At the machine code level, enums are stored as integers, starting from 0 by default.)
- Visual Studio helps prevent typos and logical errors.

## Example

```cs
enum Day
{
   Sunday,
   Monday,
   Tuesday,
   Wednesday,
   Thursday,
   Friday,
   Saturday
}
```

The following code is then possible:

```cs
Day d;
d = Day.Wednesday;
```

Another example is the months of the year: January through December.

## Why should I use enums?

Here's an example that demonstrates why:
A calendar application where you can add an item to a weekday.
Initial approach:

```cs
void AddToCalendar(int day, string item)
```

The days in the week are created as constants. Sunday is 0, Monday is 1, etc.
The same applies to the months in the year: January is 0, February is 1, etc.

Now if you make a programming error:

```cs
AddToCalendar(February, "whole month of spectacular offers");
```

This will incorrectly add the item on Monday... Oops.

With enums, the compiler prevents this error because Month and Day are different types:

```cs
void AddToCalendar(Day day, string item)
```

# Additional Resources
+ [pptx](knowEnum.pptx)