# Afterword basics: Choice structures in C#

  

If a piece of code should be executed sometimes and sometimes not,  

then you need an `if` or `if ... else` `statement`.  

If a piece of code should sometimes be repeated once and sometimes more often,  

then you need a `for` or `while` `statement`.

  

### if-statement

  

This structure is used to execute a piece of code  

depending on a particular situation (called the `condition`).  

Common form:

  

```cs  

if ([condition])  

{  

[Code to be executed if condition is true]]  

}  

```

  

Where `condition` is a statement that has the value  

`true` (*true*) or `false` (*not true*).

  

Examples of conditions:

  


| Condition | Meaning |  

| --- | --- |  

| true | True |  

| false | not true  

| i > 5 | Is i greater than 5?  

| i < 7 | Is i smaller than 7?  

| i >= 1 | Is i greater than or equal to 1?  

| i <= 2 | Is i less than or equal to 2?  

| i == 3 | Is i exactly equal to 3?  

| i != 3 | Is i unequal to 3?  

| pieceText == “abcde” | Is pieceText exactly equal to “abcde”? |  

| pieceText < “abcde” | Is pieceText earlier in the alphabet than “abcde”? |  

| etc. |.



  

  

Furthermore, *[Code to be output if condition is true]* represents  

A piece of code (this can be several lines of code)  

to be executed if the condition is `true` (*true*).  

If exactly one line of code is to be executed, you could choose to  

choose to omit the open and close curly braces,  

but this increases the chance of bugs,  

so we advise against it.

  

### if ... else ... statement

  

An if statement can be extended with an &quot;else&quot; block. If the condition does not return &quot;true&quot; then the code in the else block is executed.  

Common form:  

```cs  

if ([condition])  

{  

[Code to be executed if condition is true]]  

}  

else  

{  

[Code to execute if condition is not true] }  

}  

```

  

Note: whether the condition is true or false, one of the two pieces of code is always executed.

  

### Examples “if ...” statement and “if ... else ...” statement

  

```cs  

if (true)  

{  

TextBox1.Text = “test”;  

}  

```

  

The bit of code between { and } is always executed,  

so the `Text` of the *TextBox* is always made &quot;test&quot;.  

```cs  

if (false)  

{  

TextBox1.Text = “test.”  

}  

```

  

The bit of code between { and } is never executed.  

```cs  

bool b = true;  

if (b)  

{  

TextBox1.Text = “test”;  

}  

```

  

If `b` has the value `true` (= *true*)  

has, the `Text` in the *TextBox* is created &quot;test&quot;.  

This is always the case here now because in this piece of code  

variable `b` is only assigned the value &quot;true&quot;.  

```cs  

int i = 10;  

if (i < 5)  

{  

i = i + 1;  

}  

```

  

If number `i` is less than 5,  

then one is added to the value of `i`,  

otherwise nothing happens.  

```cs  

TextBox1.Text = “test2”;  

if (TextBox1.Text != “test”)  

{  

TextBox1.Text = “test3”;  

}  

```

  

If the text in the textbox is not equal to &quot;test&quot; (which is the case here) then the text of the textbox is changed to &quot;test3&quot;.  

```cs  

if (true)  

{  

TextBox1.Text = “test”;  

}  

else  

{  

TextBox1.Text = “test2”;  

}  

```

  

The piece of code between the first { and } is always executed,  

so the `Text` of the `TextBox` is always made &quot;test&quot;.  

The piece of code between the second { and } is never executed.  

```cs  

int i = 5;  

if (i >= 10)  

{  

i = i + 1;  

}  

else  

{  

i = i + 5;  

}  

```

  

If number *i* is greater than or equal to `10  

then to number *i* `1` is added.  

This is not the case here, so to *i* `5` is added.  

Result: *i* is given the value `10`.  

```cs  

int i = 5;  

if (i >= 10)  

{  

i = i + 1;  

}  

else  

{  

i = i + 5;  

if (i >= 10)  

{  

i = 20;  

}  

}  

```

  

If number *i* is greater than or equal to `10`  

then to number *i* `1` is added.  

This is not the case here, so to *i* `5` is added.  

Result: *i* is given the value `10`,  

then we check whether `i >= 10`,  

which is now the case so *i* is finally assigned the value `20`.