# Separation between GUI and Domain

In this chapter, we will discuss some of the principles involved in separating
between GUI classes and domain classes (domain classes).
Before presenting these principles, we first explain what a domain class is.
We end this chapter with illustrations where the intended separation is
has been implemented well or poorly (read: less well).

## Domain
Every application (or app) is a tool to make certain processes faster,
more pleasant or otherwise better.
These processes involve creating, inspecting,
modifying or deleting information.
For example, applying for a new bank account, requesting a bank account balance, transferring money from one bank account to another, or saying goodbye as a customer of a bank. These cases always involve Information from the application domain of financial traffic. The Information is related to objects from this application domain: such as Bank Account, Bank, Client and Transaction. We call these objects of domain classes. Opposed to these are objects that provide a means
+ to be able to visualize domain objects in a GUI, or
+ to be able to store information in objects in a database or file, or
+ to be able to send information in objects over a network or ...

The latter three objects do not belong to the domain.
We have for the domain of financial traffic the domain classes.
Bank Account, Bank, Client, Transaction introduced.
For a game with heroes and monsters, the
domain classes Hero, Monster, Player and Game could play a similar central role.
These classes house the important information to make such a game in a GUI
be able to make it visible.
In summary, Domain classes house the relevant information from the intended application domain.

### Challenge1
Which domain classes would you like to introduce within the context of the game gallows?

##### Challenge2
What domain classes would you like to introduce within the context of sending, viewing and deleting emails?

## Principles
We recommend adhering to the four principles below, for the sake of proper separation between the program code in a GUI and the program code in the domain classes. This list of principles is not complete, but will be expanded and further refined as you study.
1. Do not use GUI objects in domain classes. Because then you cannot easily switch to another GUI (e.g. WindowsForm, Web GUI, smart phone, different design of GUI, differences in GUI by type of user) that way. Also, within a domain object, don't include images (later jewel will want to use a different image).  This will make your software more flexible and maintainable.
2. Be careful about including self-defined calculation or validation methods within a GUI class (see 3.)
3. Restriction rules (such as the balance of a bank account may not fall below the credit limit) and calculations (such as how much interest you get credited per month) should be 100% secured within the appropriate domain class that has all the required information.
4. If you want to be able to include a text representation of domain objects in the GUI, it is convenient to 'override' the ToString method of the respective domain class.

## Illustrations
We illustrate these four principles using the bank account case study.

### ad 1.
**Error**: Within a ChangeBalance method of the BankAccount class, a messagebox (MessageBox.Show)
activate as soon as an attempt is made to debit too much money from the BankAccount object.

```cs
public class BankAccount {
  private decimal balance;
  private decimal threshold; // not negative
  ...
  public void ChangeBalance(decimal amount) {
    if (balance + amount < -threshold) {
      MessageBox.Show("withdrawal of " + amount + " is not allowed");
      } else {
      balance -= amount;
    }
  }
}
```


**Good**: For example, the ChangeBalance method of the Bankaccount class returns a string. The corresponding string represents whether the withdrawal of the money amount has been accepted or not. Then, this return value can be displayed afterwards in the GUI within a MessageBox as a message.

```cs
public class Bankaccount {
  private decimal balance;
  private decimal threshold;
  ...
  public string ChangeBalance(decimal amount) {
    if (balance + amount < -threshold) {
      return "withdrawal of " + amount + " is not allowed";
    } else {
      balance -= amount;
      return "withdrawal is succeeded";
    }
  }
}
```

Note, instead of the string as return value, a simple bool can be used.
### ad 2.
**Fout**: Binnen de GUI-klasse wordt een hulpmethode CheckValidTransaction gedefinieerd waarbinnen alvast wordt gecontroleerd of het overmaken van geld, van de ene bankrekening naar een andere bankrekening uitvoerbaar is.

```cs
// een methode binnen de GUI-klasse
bool CheckValidTransaction(Bankaccount ba, decimal amount) {
  if (ba.getBalance() + amount < -ba.getTreshold()) {
    return false;
  } else {
    return true;
  }
}
```
**Good**: Forward the transfer request to the appropriate Bank object of the bank account from which the money is to be debited. Later, the Bank object reports whether the transfer was successful, for example by means of a string (see also ad 1.)

```cs
public class Bank {
  ...
  public string Transfer(string from, string to, decimal amount) {
    // check if bankaccount number from exists
    Bankaccount baFrom = GetBankaccount(from);
    if (baFrom==null) {
      return "Bankaccount " + from + " does not exist.";
    } else {
      // check if bankaccount number to exists
      Bankaccount baTo = GetBankaccount(to);
      if (baTo==null) {
        return "Bankaccount " + to + " does not exist.";
      } else {
        string result = baFrom.ChangeBalance(-amount);
        if (result == "withdrawal is succeeded") {
          baTo.ChangeBalance(amount)
        }
        return result;
      }
    }
  }
```


### ad 3.
Assume for a moment that a bank should not have two customers with the same combination of name/address/date of birth.

**Error**: Within the Bank class, once a new customer is added, there is no check if a customer already exists with the same name, address and birth date.

```cs
public class Bank {
  private List<Client> clients;
  ...
  // other client data is ignored for now:
  public void AddClient(string name, string place, DateTime birthdate) {
    Client client = new Client(name, place, birthdate);
    clients.Add(client);
  }
}
```


**Good**: Within an AddClient method of the Bank class, it first checks whether a Client already exists with the same name, address and birth date. If so, the new Client object is not created and registered; otherwise, it is. The AddClient method has as its return value the new Client object. If the return value is null, no Client object has been created.

```cs
public class Bank {
  private List<Client> clients;
  ...
  // other client data is ignored for now:
  public Client AddClient(string name, string place, DateTime birthdate) {
    Client client = GetClient(name, place, birthdate);
    if (client != null) return null;
    client = new Client(name, place, birthdate);
    clients.Add(client);
    return client;
  }
}
```


### ad 4.

Within the GUI, a list of data of all bank accounts of a specific customer is displayed. Then it is convenient if the ToString method of the Bank Account class is redefined; for example, by sufficing with the account number and the name of the owner of the bank account:

```cs
public class Bankaccount {
  private string no;
  private Client owner;
  ...
  public override string ToString() {
    return this.nr + ": " + this.owner.GetName();
  }
}
```

This ToString method can then be called within the GUI.