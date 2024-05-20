# Casus: Bank

|                    |                                     |     |
| ------------------ | ----------------------------------- | --- |
| Learning Outcomes  | constructor, this, static           |     |
| Required Knowledge | Basisbegrip class, object           |     |
| Challenge Type     | Workshop, Realise, Working together |     |



In this assignment, you will create an application for a bank. For clarity: a financial, with bank accounts, where customers know their money is safe.

This application allows you to:
- **Deposit money** into a bank account. The user can only deposit a positive amount. When attempting to deposit anything other than positive numbers, the transaction is not performed and an error message is given.
- **Withdraw money** from an account. The user wants to withdraw money. Note that only positive amounts may be transferred! If a negative balance would occur, or if something other than positive numbers is entered, the transaction will not be executed and an error message will be issued through a MessageBox.
- **Money Transfer** from left to right (or right to left). In the TextBoxes on the left (right), enter the amount to be transferred then click the Button &gt;&gt; (&lt;&lt;).  If there would be a negative balance at the paying party, or if something other than positive numbers is entered, the transaction will not be executed and an error message will be given through a MessageBox.
The displayed balance is of course neatly adjusted after each transaction.

## Command

Note: To demonstrate that you can program with Objects, it is important that you not only "obediently execute" an assignment like this one, but that you also figure out how to create extensions to your program on your own. So at the end of this document, the challenge really begins!  

Suppose you execute this command in C#. You can do it as Console, as WinForms, as WPF, as UWP, or completely without UI (user interface) and then use unit tests to prove that it works.

### Step 1: Think before you start!

What comes first? You can approach a development like this from at least two sides: you can work `Top Down` or `Bottom Up`, below are brief descriptions of both. Read them and choose what you would prefer to do with this project.
#### Top Down 

At `Top Down` you might then start with a sketch of what a screen might look like. You then talk about that with your client and with potential users. Make a sketch on a whiteboard and talk about this with your peers: is this clear to a user?


If there is consensus on that, that GUI is built in a development environment (IDE: Integrated Development Environment). From there, it is examined what `classes` are needed and, for example, what `methods` and `properties` there are.

To see what our
Create a new Windows Forms project that you call Banking, for example. Give the automatically created Form1 form a more meaningful name, for example, Bank AccountForm. Also modify the Property Text of the form so that a better name appears in the application title bar.

#### Bottom Up


### STEP 2: The (Graphical) User Interface

Drag and drop the required components onto the form. It does not have to be exactly as shown in the example, but think about how you will link the required functionality to the components beforehand. Give the components a meaningful name, for example, btnDepositLeft and txtEuroRight.


### STEP 3: THE CLASS BANK ACCOUNT
Add a new class and name it Bank Account. Each bank account has an account number, is in a person's name and has a balance. Make sure the class has Bank Account Fields to store the required data and further has the following fields:

```cs
// Fields
private int account number;
private string name;
private int balance; // the balance in whole cents
private static int nextFreeAccountNumber = 2001;
```

### Properties
Program the following attributes as properties:
- Account number (type int)
- Name (type string)
- Balance (type int)

```cs
// Methods
public void TakeOp(int amount)
{
    // amount in whole cents, negative amounts are ignored.
    // fill in your own
}

public void Deposit(int amount)
{
    // amount in whole cents, negative amounts are ignored.
    // enter your own
}

public void CreateOver(Bank account otherAccount, int amount)
{
    // amount in whole cents, negative amounts are ignored.
    // enter your own
}
```

Complete the implementation of the methods that say "fill in yourself" by yourself.

### Static variable

Notice that it says `static` for the variable nextFreeAccountNumber and that this variable is initialized at 2001. That it says static means that this is a so-called class variable. A class variable exists even before an instance of the class is created and is initialized when the application is started, rather than when the object of that class is instantiated (created), as normal variables are. The advantage of a class variable is that it has the same value for all instances of that class. Thus, the same class variable is used by all instances of this class.
Each new bank account must, of course, have a unique account number. For this bank, these are the numbers starting in 2001. The first bank account, which is created, will have account number 2001, the next account number 2002, etc. Determining the next free account number is done in the Constructor.
### Constructors

A Constructor is a special method with the same name as the class that is executed when an object of that is created and serves to initialize the Fields or Properties of the class. We need two Constructors. One to create a Bank account when the account holder's name is known and the initial balance is 0 and one for the case when there is an initial balance, for example, as part of a bank recruitment campaign.

```cs
// Constructors
public Bank account(string name)
{
    this.name = name;
    balance = 0;
    account number = nextFreeAccount;

    // we raise the next free account number by 1 so that the
    // next bank account gets a number 1 higher than
    // this bank account.
    ++nextFreeAccountNumber;
}

public Bank account(string name, int balance)
{
    // fill in yourself
}
```


It is common in many C# teams to put the Contructors after the Properties and before the Methods.

### STEP 4: THE CLASS BANK ACCOUNTFORM
Within the Bank AccountForm, declare two Fields, for the 2 bank accounts. Then initialize these two Fields in the Constructor of the form.

```cs
public partial class BankaccountForm : Form
{
    // Fields
    private Bank account bank accountLeft;
    private Bank account bank accountRight;

    // Constructor
    public Bank accountForm()
    {
        InitializeComponent();
        bank accountLeft = new Bank account("Duck, Dagobert");
        bank accountRight = new Bank account("Goose, Gus");
    }
```

Now create the EventHandlers for the buttons. Remember? Double-clicking on the Button in the design screen automatically creates the default EventHandler (Click). Now populate the EventHandlers for all Buttons to achieve the requested functionality and error handling. In doing so, use the methods of the Bank Account class you have already created. Check for valid entries and also don't forget to update the Labels with balance information. You can use the method ToString for this, specifying that you want the balance as currency.
<p class="note">If you want a numeric value to be displayed as currency you can use the method `ToString()`. You then pass a capital C as a parameter to indicate that it is currency:</p>

```cs
double balance = 120.55;
lblSaldo.Text = balance.ToString("C");
```



When you are done, test that all functions and error handling are working properly. Also use the list of desired functionality on the first pages of this assignment for this purpose.

#### TryParse
If you want to check whether a typed text is an integer, you can use the method below.

```cs
bool int.TryParse(string text, out int result);
```

As you can see, the declaration of the second parameter specifies out. This means that this method may modify the value of result. When calling the method, out must also be mentioned. The value of the result parameter may have changed after calling TryParse. If true is returned, text contains a whole number and result has the value. If not, something other than an integer was entered and result does not contain a valid value. Note that a negative integer is also an integer.

```cs
if (int.TryParse(txtEuroLinks.Text, out number))
{
    // the entry in txtEuroLinks is an integer and
    // the value is now in the variable 'number'.
}
```

See MSDN for more information.

## Und jetzt gehts los!

Freely translated: From now on you may go all the way! Up to this point it was a training assignment, which allowed you to gain basic knowledge and skills. From here comes the opportunity to show that you have mastered OOP.

Here are some examples of additional fuctionalities with which you can extend your bank.

###

Show a list of `transactions` on the screen in which the transactions are displayed indicating date, time, account number(s) involved and amount. Optionally, you can display only successful or both successful and unsuccessful transactions. In the latter case, it is also indicated whether the transaction was successful or not.