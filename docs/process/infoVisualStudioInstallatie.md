# Visual Studio installation

## What do I need?

A development environment (IDE for short). If you have no experience yet, we recommend the `default`:

### Default: `VS for MS-Windows`.

Visual Studio (abbreviated: VS). The default is
`VS for MS-Windows`. In some commands, you see screenshots of WinForms apps (still), which you can create only in this version. In other environments, you must first figure out how to achieve the same effect. Also, a teacher or fellow student may be demonstrating something with WinForms: In that case, it's easiest if you use the same version.

You can use the Community Edition (free license): everything we do in the starting semester can be done in it.



### Alternative: `FHICT online workplace`.

FHICT also offers an `Online FHICT workplace`. See `studentenplein` at `portal.fhict.nl`.

+ This is `VS for windows` without having to have MS-Windows installed locally.
+ You have to stay logged in continuously then, though.
+ You must also copy created stuff to local, otherwise you will lose it!


### Alternative: `Visual Studio Code`.

If you do not have programming experience yet, we do not recommend this, because some things just work differently from your fellow students and teachers: you may have to figure some things out yourself.

+ Installation is more difficult.
+ WinForms is not supported in 'VS Code'.
+ Otherwise an excellent programming environment.
+ Also used at Technology Deepening.

### And on a Mac?


+ Default: We recommend running Bootcamp or possibly a Virtual Machine (e.g. VMWare or Parallels) with MS-Windows and in it `VS for Windows`. This does eat up disk space and may be a bit slower from time to time, but you will have the same IDE as fellow students under Windows.
  + [https://support.apple.com/nl-nl/boot-camp](https://support.apple.com/nl-nl/boot-camp)
+ `VS for Mac`: does not support WinForms; short-cut keys are different; otherwise a fine programming environment.
+ `Rider: Fast & powerful cross-platform .NET IDE`: supports WinForms. It is part of Jetbrains and through your student account you can use this software for free.
+ `Visual Studio Code`: see above.
+ The `Online FHICT workspace`: see above.

For both bootcamp and VM solution you need additional software. This can be found for free in the webshop linked above.


## Installation

### One Way
You search the Internet for &quot;Visual Studio 2017 community&quot;.
[For example, here](https://visualstudio.microsoft.com/vs/)

They call the free version of VS the Community Edition.
When installing, choose &quot;.NET desktop development&quot;.
This version is sufficient for the starting semester. But....

#### Another way: Through Student Square
It can also be done through [student square](https://portal.fhict.nl/Studentenplein/SitePages/Home.aspx)
on the
[FHICT portal](https://portal.fhict.nl),
under the heading 'Software'.


## Your first program (WinForm, works only in VS for MS-Windows)

Want to know if your VS works? Start up Visual Studio. We will first create a new project and then start typing C# source code. Next, we'll launch the C# source code. Your first program!


![fig:visualstudio](figures/VS080-done.png "Dit is Visual Studio")

If you
[this]()
you see after installation, then you are ready to start the next step.

### Windows Forms App C#

From the File menu, choose New and then Project.
See

[New Project]().
![fig:vsprojectnew](figures/VS090-newproject.png "Dit is Visual Studio")


Make sure you show the blue part exactly the same as yours on the screen.
Keywords: &quot;Visual C#&quot; is selected on the left and it says
&quot;Windows Forms App (.NET Framework) Visual C#&quot;.
Give the project a self-selected name at &quot;Name&quot; and then click &quot;OK&quot;.

### Tapping C# Sourcecode
To get to the source code of your first (empty) program
we need to make it visible. Right click on 'Form1' and choose 'View Code F7'.


![](figures/viewcode.png "View Code")

You now see C# source code in the middle.
Copy the line below and paste it under the line already there.
Make it so that your screen looks the same as below.
The point is to add just this line.
Some of the names in the lines above and below are named a little differently.
This is because in the example program the names
may have been chosen slightly differently. That's not a big deal.

```cs
MessageBox.Show(System.Text.Encoding.UTF8.GetString(System.Convert.FromBase64String("SGVsbG8gV29ybGQh")));
```


![](figures/vspasswordcodehello.png "password code")

Essentially, then, you just add &quot;MessageBox...&quot;line under the &quot;InitializeComponent()&quot;line.
This line contains a secret code that displays a message to you at startup.

### Start up first program

After you have typed C# source code, you must instruct Visual Studio
to create (compile) and execute (run) the program.
You do that with the &quot;Start&quot; button. You will see a message after execution.


![](figures/runstop_run.png "run")
![](figures/runstop_stop.png "stop")

You notice that Visual Studio has two &quot;faces&quot;.
An editing mode and an execution mode.

- We use the `editing mode` the most. There you can program buttons and type C# source code. Visual Studio starts up in this mode and in this mode we just added that line of C# source code. In this mode we can start our new program with &quot;Start&quot;.
- After you click &quot;Start&quot; all icons will jump. Sometimes your C# source code remains, sometimes not. You see Visual Studio start up your program and draw graphs of your CPU/Memory. Visual Studio is running your program in this mode. Click the stop block (see image above) to stop executing and return to edit mode.

### It's not working?

Now you may have made a typo in your C# source code. Visual Studio shows that with this screen:

![](figures/vsbuilderror.png "build error")  

Always choose &quot;No&quot;! Then you can go back to your Visual Studio to see where your typo is.

![](figures/vstikfout.png "tikfout")

Typographical errors are indicated by Visual Studio with red circles under the words.
Just like in Word. These are sometimes difficult to understand.
If so, remove the line and type it again.
You can also close the program and revert
to a last working version. (Do not save.)

### How to proceed?

Try opening the designer from Form1 (right-click on Form1 again,
just like opening the code).
Drag some buttons (buttons), text (labels), and so on onto your Form1.
Adjust the color and text. Make it something pretty!
If you double-click a button you can use this code to put down
that then becomes visible when you press the button.
(Paste this code on the empty line between the { and }.

```cs
MessageBox.Show("Thank you for clicking!");
```