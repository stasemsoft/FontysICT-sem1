# Training - List - Adding Prices

Add some prices in the piece of code below, where the comment is. Rewrite the for-loop to a foreach repetition structure. Check your new code in a C# project.

```csharp
List<double> prices = new List<double>(); 
double totalPrice = 0.0; 
// You still need to add some prices (doubles) to the List here. 

foreach(double price in prices) 
{ 
	totalPrice += price; 
} 

Console.Out.WriteLine("The total price is " + totalPrice.ToString("C"));
```