#Training Traffic Light

We are going to program traffic lights (popularly known as stop lights).
Now it's a pretty straightforward variant,
but after theory in later chapters it will be extended.
So save the code you create!

## Analysis

Before we start typing code we always think about what we want to achieve:
- The client requires the code to be in English.
- I want to have the ability to create multiple `objects` of type *TrafficLight*, but I only want to program it once.
- A *TrafficLight* can have the colors (*states*) `green', `orange', `red': use English names for these states.
- For safety, when creating a TrafficLight, the state is always set to *red*.
- From *red*, the state can only become *green*, then *orange*, then *red* again.


## Design
- A `Console` project to named *Traffic*.
- A `class` *TrafficLight*.
- This class has a `private` `Field` *color* of type *String*.
- Initial value of *color*: *Red*
- The class gets a `method` *NextState()* that gives the TrafficLight the next value of *color*.
- We also want to be able to ask a TrafficLight what the current color is: `public String GetCurrentColor()`

## Realization.
- Create the items listed in the design.
- The `method` *NextState* returns the color **after** changing the color: `public String NextState() {...}`

A Console app has a *main*method (`public static void Main(string [] args)`)
in which you can put code like:

```cs
TrafficLight trafficLight = new TrafficLight();
// color has to be "Red".
Console.WriteLine(trafficLight.GetCurrentcolor());
trafficLight.NextState();
// color has to be "green".
Console.WriteLine(trafficLight.GetCurrentColor());
trafficLight.NextState();
// color has to be "orange".
Console.WriteLine(trafficLight.GetCurentColor());
trafficLight.NextState();
// and 'red' again!
Console.WriteLine(trafficLight.GetCurentColor());
```

The above code is somewhat sloppily put together: check for errors!
Correct them if necessary and test the program.
Can you think of any improvements to the program?