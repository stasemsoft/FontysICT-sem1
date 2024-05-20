### Super-gallery

| Level | 4 or 5
| --- | --- |
| Learning Objectives | Class, Property, Constructor, private/public, UI separation, algorithm |.
| Prior knowledge required | Method, GUI, Basic Types, If. |
| Challenge Type | Programming, Algorithm.

#### Assignment
Gallows is a game where a player must guess the word than the computer has in mind. Assignment: write gallows and use the object-oriented capabilities of `C#`.
1. `classes` to be programmed: `Word` and `Form1` (form).
2. `property` to be programmed in the `class` *Word*: *Number ofLetters*.
3. Programmable `method` in the `class` *Word*: `pool IsGood(string word)`.
4. `classes` to be programmed: *Word*, *PlayStatus*, *Form1*.
5. *Form1* has a reference to 1 *PlayStatus* object and no reference to *Word*.
6. Programmable `properties` in the `class` *Word*: *Number ofLetters* (`read-only property`).
7. Programmable `methods` in the `class` *Word*: `pool IsGood(string word)`.
8. Programmable `property` in the `class` *PlayStatus*: *TheWord* of the `type` *Word* (that is, NOT of the `type string`).
9. Furthermore, in the `class` *PlayStatus* you can add `methods` and/or `properties` that track the status of the game such as the number of letters guessed.

#### Advanced Requirements:
1. Program in another `class` *Player* and make sure that two people can play the game against each other (against the computer).
2. `Class` *Player* has a `property` of the `type` *PlayStatus* and various `methods` that you invent yourself. The form gets 2 *Player* objects and no other objects.