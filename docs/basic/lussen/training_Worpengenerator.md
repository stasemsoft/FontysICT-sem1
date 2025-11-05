# Training - For - Roll generator

  

In many board games (or digital variants thereof) throws are made with multiple dice (especially in games like Yahtzee, Risk, etc.).

  

If you don't have dice at hand or you're programming a digital variant of a game, a program that can roll x number of dice with y number of pips comes in handy.

  

The program you created at the end of this assignment looks like this:

<img src="figures/Worpengenerator-ui.png" alt="ui" width="300" />
![Worpengenerator-ui](figures/Worpengenerator-ui.png)

## Part 1.
Create a new C# Windows Forms project. Create a user interface which looks like the one below (this is a simplified form of the final result, we will assume dice with 6 pips for now). The boxes (Settings and Results) are **GroupBox** objects. These allow you to put a number of GUI objects that belong together as a group and later, if necessary, move them e.g. as a whole. It is most convenient to create the **GroupBox** objects first so that you can put the other objects on this. The white output area is a **ListBox**.
- Give the Button, NumericUpDown, ListBox, Labels and GroupBox**-en clear names. 
- Make sure the number of rolls that can be chosen is at least 1 and at most 1000. 
- Create the EventHandler for clicking the Button "Throw dice!". 
- Make sure that the ListBox is cleared first. Do this by calling the Items.Clear() method from the ListBox. So: if your ListBox has as name myListBox this goes like this: myListBox.Items.Clear() 
- Next, the EventHandler should contain the code that adds "number of throws" times a random number from 1 to 6 to the ListBox. Create this code.


![ui1](figures/Worpengenerator-ui-deel-1.png)

### Tips

- Start small by executing and displaying just one roll at first, then you can more easily extend the code afterwards by adding a repeat (for loop or while loop).
- You can add a line to a ListBox by using the Items.Add() method. So for the ListBox named myListBox, adding the number ten goes like this: myListBox.Items.Add(10);
- At the beginning of the EventHandler, create a die object once and use it to roll "number of throws" times. This avoids throwing the same number of eyes each time.
- Test if the program works properly by throwing many dice and see if it contains only the values 1 to 6.


## Part 2
Expand the user interface with two **Label** objects like the one below. One contains the text "Total number of eyes:", the other contains the default value "0" and will later contain the total number of eyes for the roll. Give the **Label** objects clear names.

<img src="figures/Worpengenerator-ui-part-2.png" alt="ui" width="300" />

In the EventHandler of the Button, make sure to add the code that tracks the total number of eyes thrown. Use a "totalEyes" variable of type int for this purpose.

### Tips
- If you create a variable inside a for or while loop then it is created during each iteration and cleared at the end of the iteration (i.e. for each roll of each die the variable is created and cleared again). If you create a variable outside, i.e., just before a for or while loop, then this variable remains in existence throughout the execution of the entire for or while loop and can be accessed from within the for or while loop.
- If, after executing the for or while loop, your totalOgen variable always has exactly the value of the last roll, then you have very likely made one of the following mistakes:
	- You didn't increment the totalOgen variable but overwrote it with the number of eyes thrown.
	- You did not declare (create) the totalOgen variable outside the for or while loop, see the tip above for what to do about that.
- Test if the total is added correctly by counting it yourself for a number of different rolls, with a different amount of dice each time.

## Part 3
Expand the user interface with a Label and a NumericUpDown as shown below. The Label will have the text "eyes on die", the NumericUpDown will have a minimum value of 2 and a maximum value of 100. The default value will be 6 (since this is the most common amount of eyes on a die).

<img src="figures/Worpengenerator-ui-part-3.png" alt="ui" width="300" />

Ensure that instead of a value of 1 to 6, a value of 1 to the value in the new NumericUpDown is now generated.

## Extensions
- Level ** - Add two additional Label objects below the total number of eyes and keep the "Height of throw so far" in this. Do the same for the lowest number of throws so far.

## Checklist
If you have completed the task correctly you have fulfilled the points below: 
- The NumericUpDown number-throws has a minimum value of 1 and a maximum value of 1000. 
- The NumericUpDown number-of-eyes-on-dice has a minimum value of 2, a maximum value of 100 and a default value of 6. 
- The Label total-number-of-eyes is set to '0' at startup. 
- The values generated match the possible values you specified in the NumericUpDown number-of-eyes-on-dice. The maximum and minimum values appear in the list (if you roll dice long enough). Test this with a small amount of eyes, otherwise you'll be in for a long time. 
- The number of values generated corresponds exactly to the value in the NumericUpDown number throw (e.g., you're not exactly wrong by one). 
- Extension: Check if the maximum and minimum are correct after many different throws. 
- Is everything correct? Then check your elaboration using the standard elaboration on the next page. Did you get everything right? Then give yourself a **shrug** or ask your favorite classmate to give you one, because you've earned it.
