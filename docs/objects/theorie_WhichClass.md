# What Classes Should I Create?

Programming involves thinking about how to *model* the reality or
*the world* that your program will (partially) *model*.
What concepts are needed within the program
(often these become the `classes` to be created)
and what behavior is expected (typically the `methods` to be programmed)?

In the previously described program about a hero fighting monsters,
we created a `class` *Monster* that described the behavior of each monster,
and a `class` *Hero* containing `methods` that described
the behavior of the hero (though it could have been designed for multiple heroes).

If you write a program for a *mortgage advisor*, you would likely have
`classes` like *Mortgage* and *LendingPart* with
`fields` like *interestRate*, *maturity*, and *amount*, and there would be
`methods` like
*CalculateInterestOverXYears* (with a parameter for the number of years involved) and so on.

The key when starting a new piece of software is to identify these concepts.
The software developer must almost always
understand the *domain* the program is about
(a Game, a Mortgage system, or whatever). One possible step here is the use of `CRC cards`.

When reading a description of what the program is supposed to do,
usually the `nouns` (mortgage, monster, hero) indicate potential classes,
and the `verbs` (compute, attack) suggest potential methods. The programmer or
software engineer will often create a diagram (often a `class diagram`) to determine
the program's structure.