# Training - Filling a bucket

Use the repetition structure **while** to fill a bucket by repeatedly adding a cup of water until it is full. Visualize the bucket with an included custom control **VerticalProgressBar** (see Resources)**.** You can simply add this class to your Project via RMB on your Project > Add > Existing Item or by dragging the file into your project (+ must appear while dragging). Then when you Build your Project you will find the control in your ToolBox.

The user can set how big the bucket is (in liters) and how big the cup is (in centiliters).

![Userinterface](figures/Emmer-vol-laten-lopen-ui.png)

Tip: To ensure that the bucket is not immediately full (due to the computer executing the loop too quickly) as well as to update the UI while executing the loop, place the following code **in** the loop structure:

```csharp
Thread.Sleep(100); //don't do anything for 100 ms
Application.DoEvents(); //update UI
```

Just be sure to place the following line at the top of the other using's to use the **Thread** class:

```csharp
using System.Threading;
```

## Resources.
- Vertical Progress Bar](https://www.codeproject.com/Articles/8422/Vertical-ProgressBar)