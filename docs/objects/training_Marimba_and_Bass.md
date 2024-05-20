# Training The Marimba and the Bass

Introductory assignment working with classes and objects.

Create a Console app. In it, create a class Marimba with a method `void PlayNote(string note){}`. To understand the principle, it is good enough (and fastest) to realize the `playing' of notes by `Console.WriteLine("marimba plays note: "+note);` You can now create a marimba in your program and have it play notes.

```cs
Marimba marimba = new Marimba();
marimba.PlayNote("e");
marimba.PlayNote("d#");
marimba.PlayNote("e");
marimba.PlayNote("d#");
marimba.PlayNote("e");
```


Now if you also create a class BassGuitar you can create multiple instruments and have them play notes in turn:

```cs
Marimba marimba = new Marimba();
BassGuitar bassGuitar = new BassGuitar();
bassGuitar.PlayNote("a");
marimba.PlayNote("e");
bassGuitar.PlayNote("g");
marimba.PlayNote("d#");
bassGuitar.PlayNote("f");
marimba.PlayNote("e");
marimba.PlayNote("d#");
bassGuitar.PlayNote("e");
marimba.PlayNote("e");
```

Make up your own ideas on how to extend this program further and have fun.