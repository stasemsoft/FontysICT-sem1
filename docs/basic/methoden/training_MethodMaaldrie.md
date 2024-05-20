#Training Method MealThree

This command was once written as a WinForm command, but you may also create a variation of it, such as a Console app.

Given is the following method:

```cs
int GrindThree(int input)
{
  int output = input * 3;
  return output;
}
```

+ Create a program that includes a ListBox that calls the above method with parameter value 2. The return value of the method then becomes 6. Store that return value in a variable named output.
+ Add the value of the return value (6, which you have in the variable output) to the ListBox with `listBoxX.Items.Add(output);` where `listBoxX` is the distinct name you gave the ListBox.
+ Test your program.
+ Extend your program with a loop that is run 10 times. In that loop, call the method GrindThree but now with parameters 1, 2, 3, 4.... to 10. So the method GrindThree is called 10 times.

![listbox](figures/maaldrie.png)
