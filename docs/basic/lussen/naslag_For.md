# Basic knowledge: For

  

  

### for statement

  

This structure is used to have a piece of code execute a  

preknown number of times to be executed.  

Common form:

  

```cs  

for([create counter variable]; [repeat condition]; [modify counter variable])  

{  

[code to be executed repeatedly]]  

}  

```

  

where *[create counter variable]* a `variable` with  

variable name of your choice is created and given a value.  

Commonly used variable names for a for statement are &quot;i&quot;, &quot;j&quot;, &quot;k&quot;  

because these have very short names, which in many cases read comfortably.  

Also &quot;index&quot;, &quot;count&quot; or &quot;counter&quot; are often used.  

The variable type is usually int.  

The value with which the counter is filled depends on what you  

are programming. In many cases it has the value `0`.  

Examples:  

```cs  

int i = 0  

```

  

```cs  

int j = 100  

```

  

Then *[repeat condition]*: this code to be executed is repeated  

repeated for as long as the value `true` comes out of the condition.  

In this, you refer to the *counter* variable.  

Examples:  

```cs  

i < 10  

j > 0  

```

  

[adjust counter variable]  

Increasing or decreasing the counter. It is often increased or decreased by 1, sometimes in larger increments (e.g., `10``).  

Examples:  

```cs  

i = i + 1  

j = j - 10  

```

  

[code to be executed repeatedly]  

The piece of code (this can be several lines of code) to be executed as long as the repeat condition is &quot;true&quot; (true).  

Every `for` statement can be converted to a `while` statement  

that does the same thing, and vice versa.

  

### Examples for statement

  

```cs  

for(int i =0 ; i < 10 ; i = i + 1)  

{  

MessageBox.Show(“Test”);  

}  

```

  

Variable `i` is initially assigned the value 0 and it is immediately stopped when i is assigned the value 10. The code is thus passed with the values 0,1,2,3,4,5,6,7,8 and 9. Therefore, 10 message boxes are displayed with the text &quot;Test&quot;.  

```cs  

for(int i =5;i > 0; i = i - 1)  

{  

MessageBox.Show(“Test”);  

}  

```

  

Variable `i` is initially assigned the value 5 and it is immediately stopped when i is assigned the value 0. The code is thus passed with the values 5,4,3,2,1. Therefore, 5 message boxes are displayed with the text &quot;Test&quot;.  

```cs  

for(int i =0;i < 10;++i)  

{  

MessageBox.Show(“Test”);  

}  

```

  

The same result as the first example,  

but in a shortened notation:  

```cs  

i = i + 1;  

```  

is traditionally also written as  

```cs  

i++;  

```  

or  

```cs  

++i;  

```

  

The same result as the second example,  

but in an abbreviated writing mode:  

```cs  

for(int i =5;i > 0; --i)  

{  

MessageBox.Show(“Test”);  

}  

```

  

```cs  

i=i-1;  

```  

is traditionally also written as  

```cs  

i--;  

```  

or  

```cs  

--i;  

```

  

  

The code  

```cs  

for(int i =0;i < 10; ++i)  

{  

MessageBox.Show("Test ”+i);  

}  

```  

results in *MessageBoxes*  

appear with successively:  

```cs  

“Test 0”  

“Test 1”  

“Test 2”  

“Test 3”  

“Test 4”  

“Test 5”  

“Test 6”  

“Test 7”  

“Test 8”  

“Test 9”  

```

  

The code  

```cs  

for(int i =5;i > 0; i = i - 2)  

{  

MessageBox.Show("Test ”+i);  

}  

```  

make messageboxes appear with sequentially:  

```cs  

“Test 5”  

“Test 3”  

“Test 1”  

```  

and finally gives  

```cs  

for(int y =0;y < 2; ++y)  

{  

for(int x =0;x < 3; ++x)  

{  

MessageBox.Show(“(”+x+“,”+y+“)”);  

}  

}  

```  

as a result *MessageBoxes* appear with:  

```cs  

“(0,0)”  

“(1,0)”  

“(2,0)”  

“(0,1)”  

“(1,1)”  

“(2,1)”  

```