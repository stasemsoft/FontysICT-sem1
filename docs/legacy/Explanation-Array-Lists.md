<!-- TRANSLATED by md-translate -->
# Explanation - Array & Lists

C#, like most other programming languages, has more complex data types in addition to classes. Two examples of this are **array derivatives** and **lists**. Both types are intended to store multiple values of a type. For example, a set of numbers, a list of strings or a number of boats. Sometimes you don't know in advance exactly how many values to remember and sometimes it's just too many to store all as single variables. These are all good reasons to use collections.

First, we're looking at array derivatives. This is the basic type for storing multiple values of one and the same type. This data type also works in the non-object-oriented programming languages, such as C.

## Array's

Look at the following example:

```csharp
double[] getallen = new double[10]; 
getallen[0] = 2.5; 
MessageBox.Show("Getal nummer 1 = " + getallen[0]);
```

An array of doubles is created here. To see exactly an array of exactly 10 doubles. On the second line of code, the first number in the row is equal to 2,5. With the [block hooks] you can give elements a new value. You can also get numbers with the [block hooks]. This is shown on the line below, in the message box. Simple, right? What number sequence is then stored in the array in the piece of code below?

```csharp
int[] getallen = new int[10]; 
for (int i = 0; i < getallen.Length; i++) 
{ 
    getallen[i] = (i + 1) * 5; 
}
```

As you can see, an array always has a fixed size. In both examples above, space is reserved for 10 numbers (doubles or integers). The Length property of an array (also shown in the above piece of code) allows you to retrieve how many elements you can store in the array. Of course you can also save other things than integers and doubles with an array. For example, you can also create an array of strings or your own objects. Try it out! An array can always save only one type (type) variable.

As with classes, you have to create an array with new. If you don't, you'll be notified by Visual Studio.

**Please note**: We start counting at ****. The first element in an array is at position 0. The number on _index_ 5 is the sixth number in the series.

**Breinbreakers**: Did you know that a string is actually a char[] array? And did you know that you can also create an array of array derivatives (2D and 3D array derivatives)? Nice challenges to play with!

## Lists

The disadvantage of an array is that you have to specify in advance How many places you want to reserve for your dates. However, this is not always known in advance. When you have a user add elements to the system you do not know how many will be added. That's why the List was conceived: the co-growing array. When you need more space, the List will automatically grow in maximum size.

```csharp
int[] getallen = new int[10]; 
for (int i = 0; i < 10; i++) 
{ 
    getallen[i] = i * 10; 
} 

getallen[10] = 10 * 10;
```

An array of up to 10 integers is created in the above piece of code. Then the table of 10 number for number is added to the array. After the for-loop, the last element is added to the array, 10 x 10. However, this will not fit anymore. Up to 10 integers in the array and 0 x 10 to 9 x 10 are already added. So there are already 10 in total. The number 100 will no longer fit and then displays an _IndexOutOutOfRangeException_ error message. In the example below an alternative is given with a List.

```csharp
List<int> getallen = new List<int>(); 
for (int i = 0; i < 10; i++) 
{ 
    getallen.Add(i * 10); 
} 

getallen.Add(10 * 10);
```

This piece of code will no longer indicate that there is no room for the number 100. The List grows with demand. So if there's more room needed, the List will clear a space. An array cannot do this on its own!

Below you see an example with a List of strings. Instead of the for-loop, the foreach is used. This is a new kind of repetition structure in which an element is already removed from the collection to work with it. This saves code again! This also works with array derivatives.

```csharp
string s = ""; 
List<string> woorden = new List<string>(); 
woorden.Add("Hallo"); 
woorden.Add("allemaal!"); 
foreach (var woord in woorden) 
{ 
    s = s + woord + " "; 
} 
MessageBox.Show(s);
```

Probably you already see it, but the text "Hello all!" will appear in a MessageBox. At each iteration (every time C# passes through the collection) he takes the following element from the collection. He puts these in the variable word. This variable always contains the element that is current in the repetition at that time. So he takes an element with index 0, then the one with index 1, index 2, and so on. So you don't have to keep track of the index anymore and the element is automatically taken out of the collection.

### List methoden

The fun of saving everything in a List is that you can easily find elements in it. We use two methods, the Contains and IndexOf. With the Contains method you can check if an element is present in the List. So this one returns true or false. The IndexOr method returns the index of the element you are looking for. If the element is not found, -1 will be returned.

```csharp
List<string> talen = new List<string>(); 
talen.Add("Java"); 
... 
if (talen.Contains("C#")) 
{ 
    MessageBox.Show("C# komt voor in de lijst!"); 
}
```

The above example shows the use of the Contains method. Different strings are added to the languages List. First, the string "Java" is added to the List. Other languages may have been added to the three dots.

If you know that a particular element appears in the List, you can use the IndexO or method to see which index the element is on. See the example below.

```csharp
List<string> talen = new List<string>(); 
talen.Add("Java"); 
... 

int index = talen.IndexOf("C#"); 
MessageBox.Show("C# staat op index " + index);
```

If C# was not in the list, the IndexOf method would indicate that the index is equal to -1. That is a code that is used when the element whose index is requested is not found in the List. You can also prevent that by first checking with Contains to see if the element occurs in the List. Try it yourself and see if you can combine the two!

**Tip**: The Contains and IndexOf methods also work for strings!

## Examples

### List en foreach

```csharp
public List<int> GeefTafelVan(int tafelVan) 
{ 
    List<int> getallen = new List<int>(); 
    for (int i = 0; i <= 10; i++) 
    { 
    	getallen.Add(i * tafelVan); 
    } 
    return getallen; 
}
```

In the code above you see a method that returns the table of a number, in the form of a List of integers. You could use these as follows:

```csharp
List<int> tafelVanVijf = GeefTafelVan(5); 
foreach (var getal in tafelVanVijf) 
{ 
    Console.Out.WriteLine(getal); 
}
```

### Array in for-loop

```csharp
char[] woord = { 'H','a','l','l','o','!' }; 
for (int i = 0; i < woord.Length; i++) 
{ 
    Console.Out.Write(woord[i]); 
}

Console.Out.Write(Environment.NewLine);
```

Above you see a piece of code to save an array of characters. With a for-loop you can retrieve the data and print it to the console. Try it yourself!

List in Containers

```csharp
List<double> inworp = new List<double>(); 
inworp.Add(.5); 
inworp.Add(2.0); 
inworp.Add(.5); 

if (inworp.Contains(.5)) 
{ 
    MessageBox.Show("Er is minstens 1 " + "muntstuk van vijftig cent ingeworpen!"); 
}
```

Above you see a piece of code with a list of prizes, stored as a list of doubles. When a user has inserted a 50 cent coin, a MessageBox will be displayed.

### List en IndexOf

```csharp
List<double> inworp = new List<double>(); 
if (inworp.IndexOf(.5) == -1) 
{ 
    MessageBox.Show("Er is geen muntstuk " + "van vijftig cent ingeworpen!"); 
}
```

Almost the same example as above. Here the IndexOf method is used to get the index of the first fifty cents munpiece in the list. If this negative 1 returns, no 50 cent coin was found.