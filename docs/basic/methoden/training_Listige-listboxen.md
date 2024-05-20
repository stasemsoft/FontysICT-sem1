# Training - List Boxes

Create a screen containing **2 listboxes**, **1 button** and **a textbox**. The screen would then look like this, for example.

<img src="figures/Listy-listboxes-ui.png" alt="onion" width="300" />

Fill the listboxes with 10 random numbers. To do this, use the **random generator** and the **listbox.items.add** method.

After clicking the button, make sure an event is started that performs the actions below:
1. Go through the 1st listbox in a **method** with a **FOR** run and add the numbers into a variable. So you need to program this method and call it from the button-click event. Return the value of the variable (return statement in the method).
2. Program a 2nd method (also called from the button-click) as follows: in that 2nd **method**, go through the 2nd listbox with a **WHILE** loop and sum the numbers into a 2nd variable. The method returns the sum of all the numbers of listbox2.
3. Depending on which variable has the highest result show a text in the result textbox ('Listbox ?? has the highest value namely: ????'). If listbox1 has the highest value you make that listbox **green** and the other **red** and vice versa.