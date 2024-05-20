# Training Car Day Value

| Level | 2 of 5 |
| ------------------- | -------------------------- |
| Learning Objectives | Class, property.           |
| Prior knowledge required | Basic knowledge about objects. |
| Challenge Type | Realize.                |

---
You have been hired as a software engineer to program a tool to determine the daily value of cars. This daily value may be calculated in this Challenge using the formula

```cs
(500000/mileage) * factor
```

but especially look on the Internet for the real calculation: maybe you'll come up with something more realistic.
The factor is a value that depends on the fuel type:
- 100 for a gasoline car is
- 150 for a diesel car is.
- 90 for an LPG car is.
- 130 for an electric car.

Technical Design
- Define an enum FuelType with the above values.
- A class Car.
- This class gets a constructor.
- Car has a public property Mileage (private setter).
- Car has a property Registration number (a String) that is passed to the constructor as a parameter.
- Car has a method DriveKilometers with an integer as parameter.
- DriveKilometers checks if the parameter is a positive number. If so, the KmStand is incremented by that amount.
- In the constructor, KmStand is given the value 1.
- Car has a property Fuel of type FuelType.
- The constructor gets the fuel type as parameter.
- Class Auto also has a property Day value. It performs the calculation and returns the correct answer.
- Override the ToString() method of Auto so something like AB-12-CD electric car 12345 km on the odometer has a daily value of 12345 euros.

Create a Console app or a GUI app (your own choice). Create a List<Auto> with at least 4 cars. At startup, the app shows the information of each car (use ToString()).

Then let each car drive a random number of miles between 1000 and 20000. For each car, show the information again. Repeat several times until each car has driven at least 100000 kilometers.