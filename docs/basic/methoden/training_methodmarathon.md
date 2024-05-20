# Training method marathon

Create a console app and program into it the methods listed below. Call them all. Check if you are convinced that the answer is correct!
You might want to use a flow chart or other tool. Then take a picture of that and add it to your Training Assignments.

In between you will find quotes from famous computer scientists here and there.

`Quote: Understand well as I may, my comprehension can only be an infinitesimal fraction of all I want to understand. (Ada Lovelace)`

(i) Create a method *FullName* with the parameters *forename* and *surname* (first and last name, if you prefer to do it in NL).
Call *FullName("Ada", "Lovelace")* returns "Ada Lovelace", She was the first programmer ever! Call *FullName("Alan", "Kay")* returns: "Alan Kay". Also remember that there must be a space between first and last name!  

(ii) Create a method called *Times* with the same parameters as the previous one. The return value is an *int* containing the number of letters in first name times the number of letters in last name.

(iiia) Create a method called *IsIn* with a string parameter `character` and a string parameter `word`. The method returns a boolean: true if the `character` occurs in `word`, false otherwise. If you can't figure this out on your own look at the bottom of this page for 'First Aid for Hanging'.

(iiib) Again, create a method called *InCommon* with the string parameters forename and surname, which returns exactly the characters that appear in both forename and surname (as a String or as a List).

`Quote: Always remember, however, that there's usually a simpler and better way to do something than the first way that pops into your head."  (Donald Knuth)`

(iv) Method *HowMuchLonger*, same parameters, which returns a number: the number of letters the last name is longer than the first name, or 0 if the last name is not longer than the first name.

(v) Method *FirstNameOf* with 1 parameter: the fullName
(e.g. "Donald Knuth", a well-known computer scientist).
The method returns the first name.

(vi) Idem *SurnameOf*.

`Quote: Most software today is very much like an Egyptian pyramid with millions of bricks piled on top of each other, with no structural integrity, but just done by brute force and thousands of slaves. (Alan Kay)`

(vii) Create a method *FirstName Backwards* that takes the first name from the fullName parameter and pastes the letters backwards into a String: this is the return value of this method.

(viii) Create a method *SurnameBackward* that takes from the fullName parameter the last name and pastes the letters backward in a String: this is the return value of this method.

`Quote: If debugging is the process of removing software bugs, then programming must be the process of putting them in (Edsger W. Dijkstra)`.

(ix) Create a method *UmEnUmForeSight*, which from parameter fullName first grabs 1st letter of first name, then 1st of last name, then 2nd letter of first name, 2nd of last name, 3rd of first name, 3rd of last name, 4th ... well, I think you get the idea. If one name is "up" and the other is not yet, paste the remaining letters after it and return the built-up string. Call this method a few times and check the result!
Example: UmEnUmVoorAchter("Edsger Dijkstra") returns: "EDdisjgkesrtra"

`Quote:
The art of programming is the art of organizing complexity. (Edsger W. Dijkstra)`

(x) You guessed it: we also want an *UmEnUmAchterVoor*, which does the same thing as the *UmEnUmVoorVoor*, but the 1st letter comes from the last name instead of the first name.
Example: UmEnUmUmForBefore("Edsger Dijkstra") returns: "DEidjskgsetrra"

`Quote: The best programs are written so that computing machines can perform them quickly and so that human beings can understand them clearly. A programmer is ideally an essayist who works with traditional aesthetic and literary forms as well as mathematical concepts, to communicate the way that an algorithm works and to convince a reader that the results will be correct.(Donald Knuth)`

(xi) Create a method *WordCount* that receives a string containing a text (for example, one of the quotes on this page). The method returns an integer: the number of words in the string.

(xii) Create a method *MeanLength* that receives a string containing text (for example, one of the quotes on this page). The method returns a double: the average number of letters per word.  

(xiii) Create a method *IsLeap* that returns a bool given an int parameter `year`: `true` if it is a leap year, `false` otherwise. Program the calculation yourself.
When is a year a leap year? When it is divisible by 4 (2020 is a leap year), but not when it is divisible by 100 (2100 is not a leap year), except once every 400 years (2000 was a leap year).
For enthusiasts: a lot has been written about calendar calculations, see for example
[The Calender FAQ](https://www.tondering.dk/claus/calendar.html)

(xiv) Create a method *numberDaysInFebruary* that calculates given a year (int) the number of days in February in that year.

(xv) Create a method *numberDaysInYear* that given a year number (int) returns the number of days in that year.

# Have I done it all right?

It is a good idea to review and/or test the following yourself:

- There are no variables defined outside a method: there are only local variables (and names of local variables start with a `small` letter).
- The `Main` method is the only place where `Console.ReadLine()` and `Console.WriteLine()` appear!
- Call each method multiple times! For example, a method that has 2 strings as parameters you call at least once with 2 strings of different length, but also with 2 strings of equal length. Check the answer!
- We usually test the `happy flow` during programming. Try to test exceptional situations too! Pass an empty string to a method that has a string parameter, and a method expecting a List or an array is called with an empty List or array.


# First Aid For Hanging

How do you pull letters out of a string? How do you count the number of letters in a string? How do you check if a string appears as part of another string?
+ [string manipulation (in Toolbox basic)](https://stasemsoft.github.io/softwarematerial/docs/basic/#string-manipulatie-in-c)