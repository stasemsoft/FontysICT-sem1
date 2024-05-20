# FileHandling
	   
| Niveau | 5 of 5: integraal |
| --- | --- |
| Leerdoelen | Class, Property, Constructor, private/public, UI separation, algoritme. |
| Vereiste voorkennis | Goed om kunnen gaan met classes en objecten en GUI separation. |
| Challenge Type | Programming. |


#### Assignment
Study the C# classes of the .NET framework that allow you to work with files, folders, directories, etc. C# has a variety of methods for reading and writing text files, moving files, creating folders, etc.
Then work on some of the cases below to practice file handling and get feedback from your instructor:

#### The Assignment
In consultation with your teacher, choose all or some of the cases below to practice file handling.
##### Case 0 - Analysis
A class can be thought of as a structure in C# that has a number of methods that belong together. Write a short document in which you describe the functionalities of the following classes in the .NET framework. Describe what you as a C# programmer can do with these classes, give some short code examples.
- File
- Directory
- DirectoryInfo
- Path

##### Case Study 1 - Text File Finder
Write a Windows Forms C# program that meets the following requirements:
1. A user interface with at least 2 list boxes.
2. After starting the app, listbox1 displays a list of all folders on the root (C:) of your hard drive.
3. If I click on a folder (item in the listbox) then a list of all files with extension .TXT appears in the other listbox.


##### Case 1a - For loop
Extend the application of case 1 with a for loop that does NOT show (skips) all files starting with the letter a in the second listbox.

##### Case Study 2 - Text Processor
Create an application that allows text files to be edited. The minimum user interface is a text field, a Save button and an Open button.
1. From a Windows Forms user interface, the user can neatly select a text file from their computer.
2. After pressing the Open button, the full contents of the file selected by the user are displayed in a multiline text field. The user can change the text in the field if desired.
3. After pressing the Save button, the text currently in the text field is saved to the previously selected file.


##### Case Study 3 - Word light
1. Create case 1 and case 2.
2. Create a third application that contains the functionality of both case 1 and case 2. Use a tab control where the user can select a file on the first tab and edit the file on the second tab.


##### Case Study 4 - Fruit Generator
1. Have the application create a file named &quot;fruit.txt&quot;.
2. Have the application write out on 5 lines the texts &quot;banana&quot;, &quot;orange&quot;, &quot;kiwi&quot;, &quot;tangerine&quot; and &quot;strawberry&quot;. Open the file in Windows Notepad to see if your application works properly.
3. Expand the application such that it displays a message if the file &quot;fruit.txt&quot; already exists.


##### Case Study 5 - My Computer
Create an application that shows all the disks on your computer (like Windows Explorer can) in a simple listbox. See

![fig:mijnComputer](figures/mijnComputer.png "Mijn Computer.")

##### Case Study 5a
Add the following features to the My Computer application:
- Ability to copy a file to another location
- Ability to rename a file


##### Case Study 5b (in-depth)
While copying a file (see Case Study 5a), display a progress bar indicating how long the copying action will take.

##### Case study 6 - Search in file
Create an application that can look up any user-entered word in a file. Display the line number in the file where the word appears on the screen.















