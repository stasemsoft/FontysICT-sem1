# Training - Array - Television

We are going to create a television application. In this television application, you should be able to see whether the TV is on or off and see which channels can be viewed.


## Part 1 - Turning the television on and off
The first step is to create a form with two radio buttons with the values "on" and "off" (rbOn and rbOff). Additionally, add a picture box with a television image and a label above it (tbStatus). When the radio button "on" is selected, the label should display "On", and when the radio button "off" is selected, the label should display "Off". Remember this status somewhere using a boolean.

![Part 1](figures/Televisie-ui-deel-1.png)

## Part 2 - Adding channels
When watching television, it is important to know which channels you can view. The television can have a maximum of 100 channels. Since the maximum number of channels is fixed, you will use an array of strings. To do this, create an empty array with space for 100 items. This way, you have enough room for additional channels in the future. How do you do this?

```csharp
string[] channels = new string[100];
```

You can now add channels to this array:
```csharp
string[] channels = new string[100];
channels[0] = "NPO1";
channels[1] = "NPO2";
channels[2] = "NPO3";
```
You can see that it starts at position 0 (channels[0]).

## Part 3 - Displaying channels in a listbox
The next step is to display this in your application using a listbox. Use the example below and add a listbox lbChannels to display the channels from the array.

![Televisie-ui-deel-2](figures/Televisie-ui-deel-2.png)
## Part 4 - Adding channels via a textbox
Once you have done this, it is time to add some functionality. The user of the application should be able to add channels. First, create a textbox (tbChannel) and a button (btnAdd).

![Televisie-ui-deel-3](figures/Televisie-ui-deel-3.png)

Then, create the method **public void AddChannel(string channel)**. This method allows you to add a channel to your array where all channels will be stored. Think about how to ensure that the channel can be stored at the correct position in the array.

## Part 5 - Channel surfing and displaying current channel
If you have succeeded, create two additional buttons that allow you to surf to the next channel (btnNext) and the previous channel (btnPrevious), and a label (lblChannel) that shows which channel the television is currently on.

![Televisie-ui-deel-4](figures/Televisie-ui-deel-4.png)

Create **two methods** to navigate to the next and previous channel. It is useful to create an integer variable called currentChannel to keep track of the current channel. Also, create a method called **public string GetCurrentChannel()**. This method displays the name of the current channel.


### Extension
Now create the graphical part of the application where you will link the above functionality to the GUI. For example, use an image as a television program. Each channel displays a different image.