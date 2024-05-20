# Class Diagram

Already you have seen `class diagrams`:
*plots showing classes as rectangles*:


![fig:ClassAenB](figures/ClassDiagram_multiplicity.png "Relation in class diagram")
In figure
[](#fig:ClassAandB)

you always see two `classes`, *A* and *B*.
The relationship between *A* and *B* is always different:
The arrow indicates a relationship between the `classes`,
including direction (`class` *A* knows `class` *B*).
We will now see how these relationships can be translated to C# code:


Possible C# code associated with (a).

```cs
public class A {

	// Fields
	private B b;

}
```

In this, `class` *A* `class` *B* *knows.
The `Field` is often given the name of the `class` but starting with lowercase.
The value of *b* can be
`null` or be an object of type *B*.


In situation (b)

```cs
public class A {

	// Fields
	private B b = new B();

}
```

Here, `class` *A* `class` *B* *know.
The value of *b* is filled in directly, so it will not be `null`.


C# code associated with (c):

```cs
public class A {

	// Fields
	private List<B> bs = new List<B>();

}
```

An `object` of `type` A knows 0 or more (because of the `0..*`)
objects of `type` B.
For the name of the `Field` (here *bs*)
the plural of *b* is usually chosen. So suppose, for example, that `class` *B*
would not be called *B* but *BattleRager*, then the Field *b* would instead be
*battleRager* and the Field *bs* would become *battleRagers*.

Note that instead of a `List`, an `Array` can also be used.