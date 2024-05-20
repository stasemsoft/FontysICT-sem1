# What classes shall I create?

Programming implies that you think about how to *model* the reality or
*the world* your program is going to (partially) *model*.
What concepts are needed within the program
(often these are the `classes` to be created)
and what behavior is expected (typically the `methods` to be programmed)?

In the previously described program about the hero going to fight monsters
we created a `class` *Monster* in which the behavior of each monster was
described, and a
`class` *Hero* containing `methods` that described the
behavior of the one hero (but it could have been more than one).

If you write a program for a *mortgage advisor* there will
probably have `classes` like *Mortgage* and *LendingPart* with
`fields` like *interest Rate*, *maturity* and *amount* and there will be
`methods` like
*CalculateRenteOverXYear* (with the parameter of how many years are involved) and so on.

The trick when starting a new piece of software is to get these kinds of concepts
to the surface. The software developer must almost always
Delve into the *matter* the program is about
(a Game or a Mortgage or whatever). One possible step here is the use of `CRC cards`.

When reading a description of what the program is supposed to do
usually the `nouns` (mortgage, monster, hero) are used.
which of these are going to be a `class` and the `verbs`
(compute, attack) are potential methods. The programmer or
software engineer will often create a diagram (often a `diagram` containing
the `classes`) to determine what the program will look like.