<!-- TRANSLATED by md-translate -->
# How To ...  (problem oriented)

How can I open from one Form in a WinForm app with multiple Forms?
The answer to these and many more questions:
[How to...](howto)

## WinForms

### Multiple Forms in an App

When you open a WinForms app, you see a code similar to:

```cs
static void Main()
{
    Application.EnableVisualStyles();
    Application.SetCompatibleTextRenderingDefault(false);
    Application.Run(new MyMainForm());
}
```

where "MyMainForm" is the name of your Form. When you start your app, a form will be created with the new MyMainForm. From this form, you can create the mainform itself. Then create a different form and invoke the method "ShowDialog":

```cs
this.hide();  
   SecondForm otherForm = new SecondForm();
   otherForm.ShowDialog();
```

### Passing information between Forms

This video explains:
[Fox Learn]https://www.youtube.com/watch?v=dWHE7mx_U14)

## Source

[how-to-open-a-second-form](https://www.c-sharpcorner.com/UploadFile/5d065a/how-to-open-a-second-form-using-first-form-in-window-form/)