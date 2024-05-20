# Training Bank account

| | |
|---|---|
| Learning Objectives | constructor, this, static |
| Required prior knowledge | Basic understanding of class, object |
| Challenge Type | Realize


In this assignment, you will create an application that represents a (greatly simplified) bank with only a few bank accounts.

This application allows the user to:
- Deposit money into a bank account. Only a positive amount can be deposited. When attempting to deposit anything other than positive numbers, the transaction is not performed and an error message is given.
- Withdrawing money from an account. In the TextBoxes, enter the amount, then click the "Withdraw" Button. If a negative balance would occur, or if anything other than positive numbers is entered, the transaction is not executed and a notification is given to the user.
- Transfer money from left to right (or right to left). The user enters the amount to be transferred and selects the transfer function.  If a negative balance would occur with the paying party, or if anything other than positive numbers are entered, the transaction is not executed and a clear notification is given.
- The displayed balance is neatly adjusted after each transaction.


## Command

Note: In order to demonstrate that you can program with Objects, it is important that you not only "obediently execute" an assignment like this one, but that you also figure out for yourself how to create extensions to your program. So at the end of this document, the challenge really begins!  

Suppose you execute this command in C#. You can do it as Console, as WinForms, as WPF, as UWP, or completely without UI (user interface) and then use unit tests to prove that it works.

## Step 1: The (Graphical) User Interface

Assume that the user of your app is a bank employee, fulfilling customer requests.

A good start in this case is to outline what the app will look like. Then we look at what `classes` are needed and, for example, what `methods` and `properties` are. Below is an example of a (too) simple GUI.


![](figures/bankrekening-simpel.png)



## Step 4: Und jetzt gehts los!

Freely translated: From here on, you can go all the way! So far it was a training task, which allowed you to gain the basic knowledge and ditto skills. From here comes the opportunity to show that you have mastered OOP.

Here are some examples of additional fuctionalities with which you can extend your bank.

### More than 2 accounts
Hopefully you've already thought about this, but a bank with only 2 accounts will make little profit. Make sure that the number of accounts can be greater than 2, and that a user can create a new account. The user of your app is a bank employee.

### Transaction overview
Display a list of `transactions` on the screen showing the transactions by date, time, account number(s) involved and amount. Optionally, display only successful or both successful and unsuccessful transactions. In the latter case it is also indicated whether the transaction was successful or not.

### Amounts
At any bank I can of course transfer amounts in cents. As a Dutchman I am used to using a comma in amounts, but what if it is an international bank? What if I use a period? Can it happen that I want to transfer 1 euro and due to a misunderstanding (because I type 1,000?) it becomes 1000 euro? Or the other way around. Not what you want!