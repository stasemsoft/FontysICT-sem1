# Training - Array - Word distorter

We are going to create a word distorter. Create an application where the user can enter a word. The user also has the choice between the distortion options "Mirror", "Addition" and "Odd". When the user clicks on the button with the text "Distort!", their entered word should be distorted and they should see the result. Here is an explanation of the different distortion options.

- Mirror: The entered word must be reversed ("Hello" becomes "olleH").
- Addition: An a becomes a b, a b becomes a c, ..., z becomes an a ("Hello" becomes "Ifmmp").
- Odd: Only take the letters at odd positions in the word ("Hello" becomes "Hlo").

There is an additional rule! You are not allowed to use the _Reverse_ or other string-related methods for the Mirror option. Otherwise, it wouldn't be a challenge, of course ;-)

## Tips
- See the strings as arrays and treat them as such. You can convert to and from char\[\] in C#. Don't forget the ASCII table for the addition.
- Create a class for your distorter. What properties and actions would be useful there? See the Classes module for more information on this topic. If you're not ready for that yet, you can always improve it later.