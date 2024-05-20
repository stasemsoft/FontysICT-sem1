# Explanation: Methods in C#

### General structure methods

A method is a piece of code that can be called from another piece of code.
that can be called from another piece of code. If a method returns a value
which is going to be used in the piece of code from which
It is called a method that returns a value.
A method can also be given one or more values.
These are called arguments.

### Main advantages of using methods:

1. Clarity: If all code is placed in a single event handler (e.g. *ButtonX_Click*) your code quickly becomes very clear.
2. Distributing work: If you want to divide the programming work before programming, you can divide the code to be created into methods and program them with several programmers at the same time.
3. Maintainability &amp; reusability: If you want to execute the same piece of code more than once at different places in your program, you can call a method from the different places and program it only once.  This saves code and is easier to maintain than copying and pasting code several times in your program.

A method has the following structure:
```cs
private [returnType] [methodName]([parameters])
{
  ...
  [returnValue]
}
```

<dl><dt>`private`</dt>
<dd>indicates that the `method` can only be called within the current file (read: `Form1`). Exactly what this means is of no interest to this course, this will be discussed later.</dd>
<dt>[returnType]</dt>
<dd>The type of the value returned by the method. If the method returns no value, this is `void` (*nothing*). Examples: `int`, `double`, `bool`, `string`, `void`.</dd>
<dt>[methodName]</dt>
<dd>Self-chosen name for the method, similar to a self-chosen name for a variable.Examples: *Count*, *Demonstration*, *Method1*, *Abc*.</dd>
<dt>[parameters]</dt>
<dd>Optional Component. Specifies the type(s) of value(s) to be passed to the method and the name under which this value can be used within the method. Multiple parameters are separated with an &quot;,&quot;-sign. Examples: `int divisor`, `int numberA`, `int numberB`, `bool isLogged`, `double aCommaGetal`.</dd>
<dt>[returnValue]</dt>
<dd>With `return`&quot; followed by a value that satisfies the *[returnType]*, a value is returned from the method to the piece of code that called the method. If *[returnType]* is `void` no return needs to be used. Examples: `return outcome;`, `return 10;`, `return myText;`, `return "Hello "+" there!";`, `return number > 10;`</dd>
</dl>


### Examples Methods

Some example methods:
```cs
    private int AddTwoNumbers(int number1, int number2)
    {
        int sum;
        sum = number1 + number2;
        return sum;
    }

    private int SquareANumber(int number)
    {
        return number * number;
    }
```

The above methods can be called as follows:
```cs
int sum = AddTwoNumbers(8765, 287);
```
or:
```cs
int squared = SquareANumber(63);
```
or, both:
```cs
int total = SquareANumber(AddTwoNumbers(1, 2));
```

#### Text and explanation (in English) about methods and parameters

See for example
[C-sharpcorner about methods](http://www.c-sharpcorner.com/UploadFile/myoussef/CSharpMethodsP_111152005003025AM/CSharpMethodsP_1.aspx)
for more explanation.