# Training - Replacing numbers with words

Write a program that picks up the user's text and replaces all digits there with words. So if the user enters _I am 20 years old_ then the output is _I am tweenul years old_. Prerequisites:

1. The user must be able to enter his text with multiple lines (multiline).
2. The functionality that changes one digit must be in a separate method (and that method must NOT interact with the user interface). Call this method **ChangeDigit**.
3. The functionality that parses and modifies the entire text should come in a second method. This second method uses the method **ChangeFigure**.