# Basics afterthought: Variables

This chapter is written as a *naslag work*,
it is not specifically written to teach how to program with variables.

### Types of variables

A variable is a piece of memory in which temporarily
a value can be stored. The common types of variables are:

| Content           | Name   | Examples           |
| ----------------- | ------ | ------------------ |
| Stukje tekst      | String | "abcde"            |
|                   |        | "dit is een tekst" |
|                   |        | ""                 |
|                   |        | etc.               |
| Geheel getal      | Int    | 12                 |
|                   |        | -1337              |
|                   |        | 0                  |
|                   |        | etc.               |
| Komma getal       | Double | 10.2               |
|                   |        | -12.3              |
|                   |        | 5.0                |
|                   |        | etc.               |
| Waar of niet waar | Bool   | true, false        |


### Create variable (declare)
Variables can be created in different ways,
some examples are listed below. Note that:
- You can choose the variable name yourself
- The line must be ended with a &quot;;&quot;-character

There are several ways to create variables. Program on a blank line the type of the variable (see above), the name you want to give the variable (you choose it yourself) and an &quot;;&quot; character to end the programming command.

| Example            | Effect                                               |
| ------------------ | ---------------------------------------------------- |
| String s;          | Variabele met de naam s wordt aangemaakt.            |
|                    | De default waarde is "".                             |
| int i;             | Variabele met de naam i wordt aangemaakt.            |
|                    | De default waarde is 0.                              |
| double d;          | Variabele met de naam "d" wordt aangemaakt.          |
|                    | De default waarde is 0.0                             |
| Bool b;            | Variabele met de naam "b" wordt aangemaakt.          |
|                    | De default waarde is false                           |
| String mijnString; | Variabele met de naam "mijnString" wordt aangemaakt. |
|                    | De default waarde is ""                              |
| int getal;         | Variabele met de naam "getal" wordt aangemaakt.      |
|                    | De default waarde is 0                               |
| double straal;     | Variabele met de naam "straal" wordt aangemaakt.     |
|                    | De default waarde is 0.0                             |


Immediately after creation, a `variable` has a `value` that we
call the `default value`. This may vary slightly from one programming language to another
different. Therefore, it is good practice to make variables that you
want to have a specific value explicitly assign this value.
assign this value.

### Give value to variable (assignment or assignment)

Once a variable is created, a value can be assigned to it.
Notice:

- Only valid values can be assigned (string values to strings, numbers to int, etc.), programming a non-valid assignment results in an error that prevents the program from executing.
- The variable to which a value is to be assigned is on the left side of the &quot;=&quot; sign, and the value to be put into the variable is on the right side of the &quot;=&quot; sign.
- The line of code is again terminated with the &quot;;&quot; sign.

Here are some examples. In comments it is explained
what it means.

```cs
String s; // create a variable named "s".
s = "test"; // Variable named "s" gets the value "test".
```

```cs
int i;
i = 10; // create variable named "i" and give it value 10
```

```cs
double d;
d = 1.52; // New variable named "d" is given the value 1.52
```

```cs
bool b;
b = true; // New variable "b" gets the value true
```

```cs
String string1;
string 1 = "abc";
String string2;
string2 = string1; // Variable named "string2" gets
                    // the value of "string1", namely "abc"
```

````cs
int numberA;
numberA = 5;
int numberB;
numberB = numberA; // Variable named "numberB" gets
                  // the value of "numberA", namely 5
```

````cs
double commaGetalA;
commaGetalA = 1.32;
double commaGetalB;
commaGetalB = commaGetalA; // Variable named "commaGetalB" gets
                            // the value of "commaGetalA."
                            // namely 1.32
```

````cs
String s;
s = textBox1.Text;
    // Variable named "s" gets
    // as the value the text contained in the
    // TextBox named "textBox1".
```

This works because the `Text property` of the *TextBox* is also
is of the `type` `string`.

### Create variable and give it a value directly (declare and initialize)

Create variable named *s* and assign value &quot;test&quot;:

```cs
String s = "test";
```

Create variable named *i* and assign value `10`:
```cs
int i =10;
```

Create variable named *d* and assign value `1.52`:
```cs
double d = 1.52;
```

Create variable named *b* and assign value `true`:
```cs
bool b = true;
```

### Convert values to other types (convert)

Note: converting an `int` or `double` to a `String` always succeeds, the other way around does not always succeed and may produce an error message during program execution (`crash` or `Unhandled Exception`).

A `bool` variable cannot be converted.

Convert the value of *i*
to a text with the same value. The
result of the last line is that variable *s* is given the value `81`.

```cs
int i = 81;
String s;
s = Convert.ToString(i);
```

Convert the value of *d* to text of the same value.
The result of the last line is that variable *s*
is given the value `"12.33"`:

```cs
double d =12.33;
String s;
s = Convert.ToString(d);
```

Convert the value of *s* to an integer (`integer`)
with the same value if it succeeds (otherwise you get an error message).
The result of the last line is that variable *i* gets the
value `7`:

```cs
int i;
String s = "7";
i = Convert.ToInt32(s);
```

Convert the value of *s* to a *comma number* with
the same value if you can (otherwise you will get an error message).
The result of the last line is that variable *d* gets the
value `12,129`:

```cs
double d;
String s = "12.129."
d = Convert.ToDouble(s);
```