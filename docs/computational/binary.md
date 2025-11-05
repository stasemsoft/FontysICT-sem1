# Binary01: Fun with Dots

## Introduction

Welcome to this interactive introduction to binary numbers! We'll learn about binary representation through a series of engaging exercises that combine magic tricks with mathematical concepts.

## Part 1: The Magic Trick

### The Setup

We'll start with a magic trick.

Take the cards with numbers (see last page). Give the 6 cards to someone and ask them to:

1. Choose a number that appears on at least one card (without telling you)
2. Select all cards containing that number
3. Give those cards to you

You'll look at them and magically know the chosen number immediately!

### The Secret

How do you know? Take the number in the top-left corner of each selected card and add them together! The sum is the chosen number.

> **Think about it:** How does this work? Will it always work? We'll explore this concept in detail later.

## Part 2: Warm-up Exercise

### Getting Started

Let's begin with something simple. You'll need a set of 5 cards, as shown in the picture below:

![](figures/dots_vertical.png)

(At the end of this file you can find a link to a printable version)

### Exercise 1: Basic Combinations

1. Select some cards so that the total number of dots adds up to 12.
2. Did you manage? Great! Now find a combination that adds up to 13 dots.
3. Then 14 dots?
4. And 15 dots?
5. After doing some more: 16, 17, 18, 19, do you see the pattern for adding 1?

> **Discussion:** Do you see a pattern? Try explaining it to each other!

### Exercise 2: Binary Representation

Now we'll make it more challenging and introduce binary representation!

Below, on the right side, you'll see numbers. Using the same method as before:

- Find which cards you need for each number
- Write it down using binary notation:
  - Put a '1' under the dot if the card is used
  - Put a '0' under the dot if the card is not used
- If you can't make the number with the given cards, cross out the number

## Examples

### Binary Number Representations

```
. . . . .   needed for number         20

. . . . .   needed for number         23

. . . . .   needed for number         7

. . . . .   is the binary representation of number   8

. . . . .   is the binary representation of number   9

. . . . .   is the binary representation of number   10
```

### Observation Exercise

Do you notice anything about the even numbers? Think about:

- What do they have in common?
- How do they differ from odd numbers?
- What pattern emerges in their binary representation?

## Summary

In this exercise, we've:

1. Explored a magic trick that uses binary principles
2. Practiced combining numbers using dot cards
3. Introduced binary representation
4. Observed patterns in number representations

The connection between the magic trick and binary numbers will become clear as you work through these exercises. Each card represents a power of 2, and the pattern of 1s and 0s you create is actually the binary representation of the number!

## Next Steps

- Try creating your own number combinations
- Experiment with different card combinations
- Think about how this relates to computer memory and data storage
- Consider how this connects to the magic trick from the beginning

> **Hint:** The magic trick works because each card's top-left number represents a power of 2, and any number can be uniquely represented as a sum of these powers!

## Resources

- [CS Unplugged](https://www.csunplugged.org/en/)
- [printable 'dot' cards](figures/binary01.prn.pdf)
