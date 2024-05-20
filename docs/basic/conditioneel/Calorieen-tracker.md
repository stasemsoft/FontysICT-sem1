# Training Calorie Tracker

For your health, it is important to keep track of how many calories you need daily. Your task is to create an application that calculates how many calories the user needs daily.

## Analysis
Your colleague has conducted a preliminary study and collected the following information:

- On average, a woman needs 2,000 kilocalories (kcal) per day. For a man, it is 2,500 kcal per day (source: Voedingscentrum).
- But if you have a sedentary lifestyle (if you move less than 30 minutes a day), then you need 10% fewer calories.
- And if you are over 50, you need 200 kilocalories less.

*Tip: you see the word IF twice in this analysis. These are likely if statements in C#.*

## Design
The design for the user interface has already been done. The user can indicate their gender and lifestyle with a radiobutton, enter their age, and click the **Calculate** button. After clicking that button, the calorie requirement will appear on the screen (how you do that is up to you: with a messagebox or by adding a label to the form).

![Supplied design of the user interface](figures/Calorieen-tracker-ui.png)

## Implementation
Program the application. Try to make a plan beforehand on how you will approach this. For example:
1. First, I will create the screen (the form) with the group boxes, radiobuttons, etc.
2. Then I will program an application that checks if someone is a man or a woman and shows 2000 or 2500 as the answer.
3. I now have the outcome (2000 or 2500) stored in a variable. Now I will look at the radiobuttons for the lifestyle. If (if statement) he chooses **Not Active**, I will subtract 10% from the outcome. And then I will show that outcome.
4. Now I will check what his age is. I will get the age from the textbox and store it in a variable. If it is over 50, I will subtract another 200 from the outcome.

*Tip: the advantage of this plan is that from step 2 onwards, you will have a working application each time.*

You now have a working application and can deliver it to the customer.

## Maintenance
After six months, the customer comes back and wants to see a number of new features added to your application.
- If the user's age is less than 12, the number of calories should be reduced by another 180.
- Pregnant women aged up to 30 need 2600 calories and pregnant women over 30 need 2500 calories. Make sure the user can indicate if they are pregnant or not and adjust the calculation.
- Testing: test if with your application you can also be a pregnant man. If not, then you have programmed it correctly.