# Text File Handling 

In order to write to a Text File or read from
a Text File you must add the following at the top of the C# File:

```cs
using System.IO;
```

### Sample code for reading from a TextFile

To read a `Text File` you need a so-called `Stream`
needed on the File.

The path where the File is stored is relative to the executable, so search (by default) in your *bin* *debug*. With '...' you go one directory higher: '../bloemkool.txt'.

Create a StreamReader on the stream:

```cs
StreamReader reader = new StreamReader(fileStream);
```

and then one line can be read in with

```cs
line = reader.ReadLine();
```

After the last line, *ReadLine()* returns a `null`.
So by making a loop it is possible to read to the end.
Finally, the *reader* and the *stream* must be *Closed*.
Around them we put a `try...catch...finally`.
If when executing the code in the `try` block an
`Exception` occurs (could be that the File does not exist,
or there are no read permissions) the program execution jumps
immediately jumps to the `catch`-block: here you can see
what is wrong. A message can be given to the user
what is wrong, or something is stored in a log.
Finally, the `finally` block: this is ALWAYS executed:
both when there is an Exception and when the `try` block is
has been executed successfully. By putting the *Close* in the `finally` block
you can be sure that after the file is closed.
So that looks like this:

```cs
String line;
try
{
	StreamReader reader = new StreamReader("C:³");
	// read the first line
	line = reader.ReadLine();

	//until you get to the end: read line by line.
	while (line != null)
	{
		// 'Process' you have to program yourself:
		Process(line);
		// read next line:
		line = reader.ReadLine();
	}
}
catch(Exception exc)
{
	// Handle the problem.
	HandleException(exc);
}
finally
{
	// and close the reader.
	reader.Close();
}
```


### Writing a Text File

Writing is similar to reading:
```cs
try
{
	StreamWriter writer = new StreamWriter("C:``sprouts.txt'');
	// Write what you want to the File:
	// WriteLine for a line with so-called EndOfLine (EOL) after it.
	writer.WriteLine("Hello File.");
	// Write to write without EOL.
	writer.Write("Still ");
	writer.WriteLine("more text.");
}
catch(Exception exc)
{
	// Handle the problem.
	HandleException(exc);
}
finally
{
	writer.Close();
}
```

Creating a StreamWriter can also be done with other parameters,
for example:

```cs
new StreamWriter("C:ids.txt", true, Encoding.ASCII);
```

- The encoding indicates how the characters in the File are encoded.
- In the example above, the *true* indicates whether to *append* or overwrite the File.

### Terminology

You can figure this out further if you need to:
- What is the meaning of the following words?
  - File, File
  - Directory, Path, Folder, Folder
  - UNC
  - URL
- What does a path look like in Windows Explorer, Command Prompt, Linux, Mac OSX?


### File handling classes
The .NET framework provides a number of classes* to handle files:
- File
- Directory
- DirectoryInfo
- Path

### Something about Exception Handling.
`FileNotFoundException`, `NullPointerException`, and so on.
All those errors that you see when you test a program the user also sees.
But when the user sees them, his program crashes!
As a software engineer, you need to avoid possible exceptional situations.
C# has the keywords `try`, `catch` and `finally` for this.
Regularly, you do not want to completely change the structure of your code to accommodate
exceptional situations that you want to consider an *exception*.
An example is when your program needs a `connection` to a `database`
or sends `requests` to the Internet:
you don`t want to check every time if the connection to database or internet
still works, but **if** the connection is lost
then your program must be able to deal with that.
In C# you do that by putting a `try-catch-clause` around your code,
as seen above.

#### Other resources on Exception Handling in C#
[Exceptions at CSharp-station](http://www.csharp-station.com/Tutorial/CSharp/Lesson15)  
[Exceptions at MSDN](https://msdn.microsoft.com/en-us/library/ms173162.aspx)  
[MSDN](https://msdn.microsoft.com/en-us/library/2kzb96fk.aspx)  
