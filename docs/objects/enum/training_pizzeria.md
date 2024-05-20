#Training - Enums - Pizzeria

## Part 1

You have been asked to create a cash register system for a local pizzeria. The pizzeria has a number of pizzas on the menu. The pizzas have the following characteristics:

Type: Margherita, Salami, Hawaii, Quattro Formaggi, Tonno

In a DropDownBox, the types of pizzas should be listed. A cashier can select a pizza and add it to a ListBox. The ListBox should then show all the pizzas for the order, and be able to "checkout". (You may just empty the list here).

## Part 2

The pizzeria is very happy with your system, but they want to expand it slightly. Namely, they have 3 sizes of pizza:
Size: Small, Medium, Large

The standard price for a pizza is 8 euros. For a medium pizza you pay 2 euros extra, and for a large pizza you pay 4 euros extra. The cashier should now also be able to select the size of the pizza. The ListBox should now also show the size of the pizza, and below the listbox should show the total price of the order.

Use the following code to support this:

```C#

struct Pizza
{
    public PizzaType Type { get; set; }
    public PizzaSize Size { get; set; } // Tip, name your new enum PizzaSize

    public Pizza(PizzaType type, PizzaSize size)
    {
        Type = type;
        Size = size;
    }

    public override string ToString()
    {
        return $"{Type} - {Size}"
    }
}

```