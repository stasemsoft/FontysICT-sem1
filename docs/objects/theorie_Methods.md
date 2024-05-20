# Reference: Methods in classes

As you know from the orientation part of this course, a method is a piece of code that can be called from another piece of code. An example of the method CalcInterest:

```cs
public double CalcInterest(double interest, double investment)
{
	return investment * ( 1 + interest);
}

double interest = CalcInterest(0.03, 1000);//1030.00
```

With this method you calculate the interest of an investment. These numbers are passed through the parameters **interest** and **investment**.

Methods are also often used in classes. What could it look like?

```cs
public BankAccount
{
	//fields
	private double investment;
	
	public double Investment
	{
		get { return investment; }
	}
	   
	//constructor
	public BankAccount(double investment)
	{
		this.investment = investment;
	}
	   
	//HERE IS THE METHOD
	public double CalcInterest(double interest)
	{
		return this.Investment * ( 1 + interest);
	}
}
	
public Form
{
	public Form()
	{
		BankAccount bank account = new BankAccount(1000);//declare bank account object
		double interest = bankaccount.CalcInterest(0.03);
	}
}

```

As you can see, all sorts of things have been added. First, the class **BankAccount** has been created. The **CalcInterest** method belongs to this class. With this method the interest of your bank account can be calculated.
The method still looks a lot like the old method, but there are some small adjustments.
1. The parameter Investment has disappeared. We no longer give it in the method, but get it from the property (public double Investment) of the class. Therefore we do not have to give it every time.
2. The calling is slightly different. You must first declare a bank account object and then you can call the method (bankaccount.CalcInterest).
3. You see **this** a few times. What does that refer to? **this** always refers to a field or method in the class itself.