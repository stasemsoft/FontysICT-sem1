# DateTime

  

## DateTime input

  

Data and time are often used in applications. For example, consider an appointment application where one can add appointments.

  

Fortunately, in C# there is the **DateTime** struct (a piece of code where there is data and functionality). You can initialize the DateTime this way:

  

```cs  

DateTime datetime = new DateTime();  

Console.WriteLine(datetime.ToString());  

```

  

The result is: 01-01-0001 00:00:00.  

This is because you are not passing in any values. You can do this in several ways.

  

### Change Date.

  

Want to retrieve a specific date? Then use the parameters in the DateTime object:  

```cs  

DateTime datetime = new DateTime(2024, 03, 17);  

Console.WriteLine(datetime.ToString());  

```  

The order of parameters here is year, month and day. This object gives us March 17, 2024.

  

You can also add a time to this:  

```cs  

DateTime datetime = new DateTime(2024, 03, 17, 7, 13, 2);  

Console.WriteLine(datetime.ToString());  

```  

The order in this is year, month and day. This object gives us March 17, 2024 07:13:02. You have several more [opportunities](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.-ctor?view=net-5.0) to modify a date-time via parameters.

  

Furthermore, you have several methods by which you can also adjust the date.

  

Among other things, you can retrieve the current time by using **Now**:

  

```cs  

DateTime today = DateTime.Now;  

Console.WriteLine(today.ToString());  

```

  

Want to know what date it will be in 3 days? Then use **AddDays**:

  

```cs  

DateTime today = DateTime.Now;  

DateTime overThreeDays = today.AddDays(3);  

Console.WriteLine(overThreeDays.ToString());  

```

You also have AddHours, AddMilliseconds, AddMinutes, AddMonths, and many [more](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.add?view=net-5.0).

  

  

## DateTime output

  

Of course, it's great that you can create a DateTime object, but what can you do with it? For example, one useful application is that you can show days, months, years, and so on separately:

```cs

DateTime datetime = new DateTime(2024, 03, 17, 7, 13, 2);

int year = datetime.Year; //2024

int month = datetime.Month; //3

int day = datetime.Day; //17

int hour = datetime.Hour; //7

int minute = datetime.Minute; //13  

int second = datetime.Second; //2  

```

  

## Compare DateTime  

It can also be very useful to check if a date has already passed. For this purpose, the DateTime class has the method **Compare**.

  

```cs

DateTime today = DateTime.Now;

DateTime aDay = new DateTime(2024, 03, 17, 7, 13, 2);

int result = DateTime.Compare(today, aDay);

  

if (result < 0)  

{

//Today is earlier

}

else if (result == 0)

{

//The same time

}

else  

{

//The time is later

}

```

  

There are other possibilities with DateTime. Check out the resources for more information.

  

For more information, see here:

- DateTime Struct](https://docs.microsoft.com/en-us/dotnet/api/system.datetime?view=net-5.0)  

- DateTime in C# C-Sharpcorner](https://www.c-sharpcorner.com/article/datetime-in-c-sharp/)

- DateTime in C#](https://www.youtube.com/watch?v=KKzSQ6r93dY)