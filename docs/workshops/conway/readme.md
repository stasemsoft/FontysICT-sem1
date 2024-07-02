# Workshop Conway's Game of Life

![](figures/1g3_o_02.gif "example")


As an introduction, watch the explanation of what the Game of Life is:
[https://www.youtube.com/watch?v=ouipbDkwHWA](https://www.youtube.com/watch?v=ouipbDkwHWA)

Professor John Conway, developer of the Game of Life, died of Covid-19 in April 2020.

Although the rules are very simple, you can build complex things with it.

![](figures/Galaxy_Conways_Game_of_Life.gif "galaxy")

If you really want to go wild, of course you can.

![](figures/Conway_Game_of_Life_Trefoil_Knot.gif "knot")


In the workshop we look at a simple variation:
1-dimensional.

The description:
`The evolution rule is based on a five-cell neighborhood, YYXYY, where the next generation of the center cell X depends on its own state and those of the four Y cells. The rule is: (1) a cell is born if it has 2 or 3 Y-neighbors alive, and (2) a living cell survives if it has 2 or 4 Y-neighbors.`

Given an array or string of bits, we can calculate a next generation.

Rules:
- neighbors: 2 cells to the left and 2 to the right of current position.
- 0 becomes 1 if there are 2 or 3 neighbors 1, remains 0 otherwise.
- 1 remains 1 if 2 or 4 neighbors are 1, 0 becomes different.


Starting with the string:

'000000010111111000000', the next generations are: 

'000000001001101100000', after that:

'000000000110101010000', than

'000000001011111100000' and so on. 


It looks a little nicer if you work with space and "X," for example:

"       X XXXXXX      "
"        X  XX XX     "
"         XX X X X    "
"        X XXXXXX     "
"         X  XX XX    "
"          XX X X X   "
"         X XXXXXX    "
"          X  XX XX   "
"           XX X X X  "
"          X XXXXXX   "


You can see that there is a shifting but repeating pattern in this.


## The assignment
Create a program that given an input calculates the next generations and puts them on the screen one below the other, as happened above.


Once that's done and you've got the hang of it, you can try making up your own variation on the rules, or you can go for the "real" Game of Life with a 2d array!


## Resources

+ [video](https://www.youtube.com/watch?v=C2vgICfQawE)

+ [conwaylife.com](https://conwaylife.com/)

+ [LifeWiki](https://conwaylife.com/wiki/Main_Page)

+ [Numberphile: Inventing the Game of Life](https://www.youtube.com/watch?v=ouipbDkwHWAf)

+ [Princeton announces that Conway died](https://www.princeton.edu/news/2020/04/14/mathematician-john-horton-conway-magical-genius-known-inventing-game-life-dies-age)

+ [Conway's lesser known results](https://mathoverflow.net/questions/357197/conways-lesser-known-results?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=4-22-20)

+ [wiki:Conway](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

+ [Coding Challenge #85: The Game of Life](https://www.youtube.com/watch?v=ouipbDkwHWAf)

+ [wikimedia](https://commons.wikimedia.org/wiki/Category:Animations_of_the_Game_of_Life)
