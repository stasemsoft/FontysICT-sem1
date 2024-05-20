# Basic knowledge: while

  

#### while statement

  

This structure is used to execute a piece of code  

as long as certain conditions are met.  

This ranges from executing the code `0` times to the  

in infinity number of times executing the code).  

General form:

  

```cs  

while ([condition])  

{  

[Code to be executed as long as the condition is true]]  

}  

```

  

<p class=“note”>After the first line there is no &quot;;&quot; character.</p>  

<p class=“note”>First it checks if a condition is met, only then any code is executed.</p>

#### do while statement

  

This structure is used to execute a piece of code. Each time after the piece of code is executed, it is checked whether certain conditions are still met, if so, the code is executed again. The number of times the code is executed varies from executing the code 1 time to executing the code in infinity number of times.  

General form:

  

```cs

do

{

[Code to be executed as long as the condition is true]]  

} while ([condition]);

```

  

After the last line is an &quot;;&quot; character.

First, the code is executed once, only then is it checked whether the code may need to be executed more often.

  

### Examples while and do while statements

  

```cs

int i = 0;

while(i < 10)

{

MessageBox.Show(“Test”);

i = i + 1;  

}

```

  

Variable *i* is initially given the value `0`

and *MessageBoxes* are continued to be displayed

until *i* is less than `10`.

The code is thus passed through with successively

the values `0` , `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` and `9`.

Therefore, `10` *Messageboxes* are displayed with the text `“Test”`.

```cs

int i = 5;

while(i > 0)

{  

MessageBox.Show(“Test”);  

i = i - 1;

}

```

  

Variable *i* is initially assigned the value `5` and it is

stopped immediately when *i* is assigned the value `0`.

The code is thus passed through with  

the values `5`, `4`, `3`, `2`, `1`.  

Therefore, `5` *Messageboxes* are displayed with the text `“Test”`.

  

```cs

int i = 10;

do

{

MessageBox.Show(“Test”);

i = i + 1;

}  

while (i < 5);  

```

  

Variable *i* is initially given the value `10`,

the code is executed, and then  

*Messageboxes* are displayed until  

until *i* is less than `5`.  

Thus, the code is continued with the value `10`.  

Therefore, `1` *Messagebox* is displayed with the text `“Test”`.