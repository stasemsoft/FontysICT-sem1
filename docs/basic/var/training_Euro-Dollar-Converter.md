# Euro-Dollar Converter

## Objectives.
 + Dealing with different types (int, double, string).
 + Using variables.
 + Converting types.
  
## Introduction
Travel agency "FLUX vacations" organizes tours in countries of all continents. Many of the trips booked go to countries where payment is not with euros but with dollars. To make travel preparations a little easier for customers, FLUX vacations therefore wants to have an application developed to easily convert euros to dollars and vice versa.
 
## Resources
Examples about working with variables in C#: see 'Reference: variable'.

## Assignment
You could use a user interface like this (but feel free to improve!):


![Aangeleverd ontwerp user interface](figures/euro-dollar-conv.png)

+ Build this user interface.
+ Make sure that the rate per cent increases/decreases when the up/down arrows are clicked (this is a Property of the NumericUpDown), and set the default value to 2.00 (or 2.00?). Check that it works by running the project.
+ Program the functionality behind the Button "<" and Button ">":
	+ When ">" is clicked, the Euros in the left TextBox are converted to dollars, and these dollars are displayed in the right TextBox.
	+ If "<" is clicked, the dollars in the right TextBox are converted to Euros, and these Euros are displayed in the left TextBox.
	+ In both cases, the set rate is used.
	
	```
	It is not possible to calculate with variables of a text type. It is possible with variables of a number type. Therefore, make sure you first convert the text in the text boxes to numbers. You can then easily perform the calculation and finally convert the result of the calculation back to text.
	```
	
## Extension (level 3 of 5)

Add a check on the input of amounts: if the input is valid, the calculation should be performed. If the input is not valid, a clear error message is displayed and nothing is calculated.

## Extension (level 4 of 5)

Add the ability to choose between two foreign currencies in a user-friendly way: Dollar or Yen. However, there will always be conversion from or to Euros. The user interface obviously needs to be adapted to this.

## Checklist
If you have done the job correctly you have fulfilled the following points:
+ Enter 1.50 at rate, enter 3 at Euros and press the ">" button. The number of dollars should now become 4.5.
+ Enter at rate 1.50, enter at dollars 2 and press the "<" button. The number of euros should now become 1.333....
+ Check whether the rate can be increased and decreased by cents.

Is everything in order? Ask for feedback but...

## Versions 
+ Mei 2015 Marcel Veldhuijzen (KAL, standaard uitwerking verwijderd) 
+ 2014-01-10 Bas Michielsen (Template) 
+ 2014-01-09 Lindy Hutz (VS 2013) 
+ 2012 Sjaak Verwaaijen 
+ 2011 Tom Broumels

