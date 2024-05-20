# Training Guru-calc: variables, operations and conversions: A Console app(lication)

(Concepts: int, double, operations and conversions)

## Preparation

Do you know the difference between an int, double and string?

## Introduction

We are going to make a working calculator. It's a minimalist calculator, but it can calculate things for you that you can't do yourself. How much is 655 times 23623? Most people prefer to use a program for that. You can make that program.

## Assignment

We ask the user to type in a number (and press enter), another number (enter again), then we tell the user how much you get when you add the numbers, as well as how much you get when you multiply the numbers.


### Some steps explained...

- Create a Console app and for maintainability, give it a clear name, such as `Calculator'.
- With the command `Console.WriteLine("cauliflower")` you can show the literal text
  between the double quotes (`"`) to user. Ask the user to type in a number.
- After each command (also called `statement`), C# would like to see a semicolon
  `;`.
- A `Console.ReadLine()` waits for the user to type something and then press
  `enter`. By creating a variable of type `String` with
  for example, the name `textTypedByUser` and then using an assignment (`assignment`)
  (identified in C# by the `=` character), the text typed by the
  user typed is stored in that variable.
- The first time you use a new variable is called the
  `declaration`: you must then put the `type` in front of it. After that
  This way C# knows when you create a new variable and when you do not.
  not.
- Note: when you put a text on the screen you use the language (NL?) with which
  the program interacts with the user, but for variable names, English is
  almost always English is used.
- A `String` is a chain of characters. To start computing with it, we have to C#
  tell it that we want to convert the value to an `int` (for
  an integer, also called `integer`). We do that by using the `method`
  `Convert.ToInt32()` and passing in the parentheses the value
  that we want to convert. The result (which we can assign to a variable of type
  `int`) is an integer: `int numberTypedByUser =
  Convert.ToInt32(textTypedByUser);`.  
- To sum the values of two existing integer variables `a` and `b` we can create a
  new integer `int c;` and assign the value of `a + b` to it.
- Finally, we need to convert the `integer` value back to a String
  to put it on the screen.

Here C# code showing the concepts discussed above:
  

```cs
Console.WriteLine("Dear user,");
Console.WriteLine("Please type a number (and press enter)");

String textTypedByUser = Console.ReadLine();
Console.WriteLine("You have typed: "+ textTypedByUser);

int numberTypedByUser = Convert.ToInt32(textTypedByUser);

int a = 42;
int b = 365;
int c = a + b;

String answer = Convert.ToString(c);
Console.WriteLine(answer);
```

It is possible to write this shorter, but keep an eye on whether it
remain readable!

With this knowledge, it is possible to create the aforementioned calculator:
The user can type in integers. For example, you can choose to tell the
tell the user both what the sum and the product of the numbers are.

Did you succeed? Then you have now written yourself a program that can do more than yourself (multiply the numbers 7225 and 5588 within a millisecond, for example) and have taken the first step toward becoming an experienced software engineer.

Stuck? Ask a question of your neighbor! If you can't figure it out together ask your teacher. In the beginning, this programming can be quite difficult.

If the calculator works then you can program the last 2 requirements. These are:
+ The result is shown as "Result: 123", so with the text "Result: " before the actual result.
+ The calculator must work with broken numbers. So 3.14 times 2.0 should yield 6.28. You must then use `double` instead of `int`.

Maybe you already had it, then you are not only good at programming, but you also passed the analysis phase honorably.

Discuss assignments regularly with your teacher and then enter feedback into Feedpulse.

## Extras

To learn it really well, it is good to make extensions to the assignments, and ask for feedback on these as well. This can lead to a higher grade (note: you have to be able to program it yourself, code-copy from the Internet is not enough). Some possible extensions:

+ Extend the calculator with a function for root subtraction (hint: square root
  in English, which helps when using a search engine).
+ If the result is below zero, show it clearly, for example by adding
  putting "CAUTION: is negative" after it.
+ Expand the calculator to include a function for division. Make sure that dividing by 0 is neatly caught and show a neat error message.