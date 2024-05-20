# Training Computer Math

If the computer is such a powerful calculator, let's use it as such...


## Straightforward

+ 100 x 0.7 - 25 x 0.6 = ...
+ 18.0 / 5.0 = ...
+ 100 / 30 = ...

Write a program that calculates these answers.

If you calculate it on a calculator (for example, the calculator app on your laptop): does it come up with the same result?
If not, try to figure out why that is.

## While walking...

Patrick takes a walk from A to B. The distance is 20 km.

He starts in A and when he has covered 1/4 part of the distance, he rests for a while (rest point 1).
After a short time he resumes the walk and walks 1/4 part of the remaining part, There he rests again for a while (rest point 2).
In the same way he continues walking. Each time he rests for a while when he has again walked 1/4 of the remaining portion.

The distance from rest point 5 to end point B is meters.
(Enter a whole number, rounding if necessary.)

After rest point 5, he makes no more stops, otherwise he will never reach the end point."


(source: question 28aug2020, better math)

Hint:
First, draw a picture.
Pause point 1 is 3/4 of 20km from point B.
Pause point 2 is at 3/4 of the number on the previous line....
And so on...



## I a little more than you....

You divide an amount of money among four people (A, B, C and D). Each person gets a different amount: A gets 20% more than the average of the four people. For clarity: in the end, the four people together get the whole amount. A gets a quarter of that + 20% of such a quarter. Then person A leaves the room.

Three people remain, with whom a similar distribution takes place:
B gets 20% more than the average of the 3 remaining persons and leaves the room. C receives 20% more than the average of the 2 remaining persons. D receives the remaining 168 euros.

The original, distributable amount is ... euro.

Write a computer program that calculates this number.

Below is part of the solution, but first try it yourself!
(Retrieved from beterreken.nl, 12aug2020; a sum by Henk van Huffelen)

## I a little more than you.... impetus to a solution

If you do it in C#:
Create a Console app and populate the Main method as follows:

```cs
static void Main(string[] args)
{
    // I a little more than you....
    // ----------- a solution ---------------

    // You divide an amount of money among four people(A, B, C and D). Each person gets a different amount:
    // A gets 20% more than the average of the four people.
    // For clarity, in the end, the four people together get the whole amount.
    // A gets a quarter of that + 20 % of such a quarter. Then person A leaves the room.

    // Three people remain, with whom a similar distribution takes place:
    // B gets 20 % more than the average of the 3 remaining people and leaves the room. C receives 20 % more than the average of the 2 remaining persons. D receives the remaining 168 euros.

    // The original, distributable amount is ... euro.

    // Write a computer program that calculates this number.

    // ----------- a solution ---------------
    // "Reverse reasoning:"
    // The amount that person D gets we call 'd', c is the amount that person C, gets and so on....
    // For amounts, we recommend the 'decimal' type:
    decimal d = 168;
            Console.WriteLine("d: {0}",d);

    // c got 20% more than the average of the last 2 people: c and d.
    // The average of c and d is (c + d) / 2
    // c is 20% more or 1.2 * that average:
    // There is: c == 1.2 * ((c + d) / 2)
    // or: c == 0.6 * c + 0.6 * d
    // or: 0.4 * c == 0.6 * d
    // so c = 0.6 / 0.4 * d
    decimal c = 3 / 2 * 168;
            Console.WriteLine("c: {0}", c);

    // b is 20% more than (b + c + d) / 3,
    // either: b == 1.2 * ((b + c + d) / 3),
    // either:

    finish this program yourself!


    decimal b = 0; // modify this....
    Console.WriteLine("b: {0}", b);

    decimal a = 0; // modify this...
    Console.WriteLine("a: {0}", a);
    Console.WriteLine("Hello World!");
}
```

Complete the program after this.
## A 1-2-3

In the store there are 3 items next to each other, each with a different price in whole euros. The prices are listed without a comma, so for example, "32 euros".

The price of the most expensive item is a 3-digit amount. If you omit the first digit of that amount, you have the price of the second item. If you omit the first digit of that again, you have the price of the third item.

The articles together cost 589 euros. The middle article is less than 30 times more expensive than the cheapest article. The difference in price between the most expensive and cheapest item is ... euro.

Write a computer program that calculates this number. (Or can you do it even without a computer program?)

## How many palindromes can I make with ...?
![](figures/trainingHoeveelPalindromen.png "hoeveel palindromen")

A `palindrome` is a word or number written backwards that is the same. For example, the word `LEPEL` or the number `121`.

You have at your disposal once the digits 3, 5 and 7 and twice the digits 2, 6 and 8 (see picture).

With these you can ... different palindromes of 7 digits.

(taken from beterrekenen.nl, 10aug2020, a sum by Henk van Huffelen).

### Sources

Some of these tasks come from
[www.beterrekenen.nl](www.beterrekenen.nl) (also as a mobile app): A few minutes of challenges every day, sometimes easy, sometimes harder, some straightforward, sometimes really needing to draw a picture or call a laptop to the rescue.... brain gym in other words.... highly recommended!

## Spoilers...

Some answers:
+ `Walking...`: 4746 meters