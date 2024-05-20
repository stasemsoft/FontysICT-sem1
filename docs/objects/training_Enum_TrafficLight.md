# Training Traffic Light (with an enum)

We are going to program traffic lights (again).
If you have already done the TrafficLight Challenge from a previous chapter,
especially if you copied the example code (with the errors in it) you will have noticed that
using a *String* for the state (color) of a TrafficLight
quickly leads to errors! For example, *Orange*, *Orange* and *orange*
all accepted by the compiler but the values are different:
this can cause all kinds of bugs:
For example, take 2 TrafficLights, say *trafficLight1* and *trafficLight2*.
If the *color* of *trafficLight1* has value *Orange* and
the *color* of *trafficLight2* has value *Orange* then an equation like

```cs
if (trafficLight1.color == trafficLight2.color) {
  ...
}
```

return *false* while the programmer expects *true*:
A typo that can have major consequences for the behavior of the software.
To avoid these bugs, we are going to use an Enum with them this time:
By using an *Enum*, the compiler can help detect and
detect and prevent them!
For the *color* (state) of the TrafficLight, we will create an `Enum`:

```cs
public enum TrafficlightColors {
   Red,
   Orange,
   Green
}
```

#### Analysis
- The code is in English.
- I want to have the ability to create multiple `objects` of type *TrafficLight*, but I want to program it only once.
- A *TrafficLight* can have the colors (*states*) `Green`, `Orange`, `Red`: use English names for these states.
- For safety, when creating a TrafficLight, the state is always set to *Red*.
- From *Red*, the state can only become *Green*, then *Orange*, then *Red* again.


#### Design
- A `class` *TrafficLight*.
- This class has a `private Field` *color* of type *TrafficlightColors*.
- Initial value of *color*: *TrafficlightColors.Red*.
- The class gets a `method` *NextState()* that gives the TrafficLight the next value of *color*.
- We also want to be able to ask a TrafficLight what the current color is: `public TrafficlightColors GetCurrentColor()`

#### Realization
- Create the items listed in the design.
- The `method` *NextState* returns the color **after** changing the color: `public TrafficlightColors NextState() {...}`

A Console app has a *main*-method (`public static void Main(string [] args)`)
in which you can put code like:

```cs
TrafficLight trafficLight = new TrafficLight();
// color has to be TrafficlightColors.Red.
Console.WriteLine(trafficLight.GetCurrentcolor());
trafficLight.NextState();
// color has to be TrafficlightColors.Green.
Console.WriteLine(trafficLight.GetCurrentColor());
trafficLight.NextState();
// color has to be TrafficlightColors.Orange.
Console.WriteLine(trafficLight.GetCurentColor());
trafficLight.NextState();
// and TrafficlightColors.Red again!
Console.WriteLine(trafficLight.GetCurentColor());
```

Is this code sloppily put together? Look carefully for errors!
Correct them if necessary and test the program.
Can you think of any improvements to the program?