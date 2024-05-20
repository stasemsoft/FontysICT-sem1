# Challenge Electronic Patient Record

If you are copying code from the Internet, mention the source (copy-paste the url in comments in your code) and make sure you understand that code.

If you make a class diagram, preferably do it on whiteboard (or paper) and attach a picture of it.

You can choose that this program does not store anything in a File (create some objects from code, so you do have some data),
use casting and Exceptions only when relevant. When in doubt, consult your teacher!

## Assignment: Electronic Patient Record
Here you may choose whether to create a WinForm application or a Console app.   
However, do not spend unnecessary time on the GUI side.

In the example, classes have Dutch names, but you may also give the classes English names if you like. Dots on letters are left out: in this description and also in your program!

## What is the electronic patient record?
For the name of a person you may use 1 string, so you don't have to take into account first name, last name, middle name.

A healthcare provider (think of a general practitioner, hospital, physical therapist) stores data about patients. This includes so-called NAW data (Name, Address, Place of residence), date of birth, but also data about the times the patient has visited, when that was, what the complaint was, the diagnosis and whether medication was prescribed at that time.

A general practice stores all such data digitally. In practice, data on patients is often exchanged between, for example, GP and pharmacy. This raises all sorts of privacy challenges, but we won't go into that now.

What we want to see is that you create a number of classes with methods, constructors, fields, properties and whatever else is needed.

First there is a chapter 'Warm-up': you get a class diagram, we want to see those classes (if you can come up with a smarter structure yourself, that's allowed too!). The text next to it tells something about the expected functionality.

After that (chapter 'And now what...') you will read what functionality could be added. You may choose one or more topics or invent your own functionality and make a design (preferably on paper!). Bear in mind that your teacher will want you to put the learning objectives from the different layers together in a somewhat larger application.
## Warmer
View the class diagram (paste the url into a browser of your choice). Attach the classes:


```
http://yuml.me/diagram/scruffy/class/edit/OIS12,[Patient|naam:string;geboortejaar:int|GetLeeftijd();]&lt;*-arts-[Afspraak],[Afspraak|dagEnTijd:DateTime],[Afspraak]patient-*&gt;[Huisarts|naam:string], [Patient]
```

[class diagram](figures/patientdossier_cd)

Nothing needs to be saved, so when the program is closed and restarted we start again with the same initial situation as always!

After starting the application, make sure that at least 2 GPs and at least 25 Patients exist.
This can be done with code like:

```cs
GP GP1 = new GP("Anna");
GP GP2 = new GP("Barend");
```

But maybe smarter to create a List of GPs?

I can create a new Patient using:

```cs
new Patient("Joris", 1999) // name and year of birth
```

Create a list of patients:

```cs
List<Patient>
```

and add at least 25 patients to it.

The name of both GP and Patient can be retrieved but not changed (except when creating the Patient).

I want to be able to ask the age of a Patient. You can do this with a property or with a method GetLife(). We keep the calculation of the age simple: 2019 - year of birth.

The constructor of the class Appointment gets 3 parameters for now: a GP, a Patient and a DateTime (when the appointment is). As a value for DateTime, you may use DateTime.Now() anywhere.
Finally, at least 50 appointments are created at program startup.

Keep these in a list.

And now on...
From this, choose some items to add to:

A general practice usually employs several doctors. Create a class Practice that has a list of GPs and also a list of patients.

The GP Practice gets its own list of Appointments. Therefore, an object of type Practice gets a method AddApointment(GP GP, Patient patient, DateTime dateTime) that creates a new Appointment and adds it to that list.

## Salary Calculation
Assume that each appointment costs $63. Create a method that calculates for each GP how much he/she earns from the Appointments.

It would be even nicer (programmatically at least) if each doctor had his own rate: to this end you could give the constructor of GP an extra parameter 'rate' which would then of course also have to be stored somewhere.

If someone cannot come to the practice (practice visit) the doctor should make a home visit.
Add to Appointment an option to indicate that it is a home visit.
(Perhaps you can suggest that there are other types of appointments).

Create a class Recipe. A prescription has a description and a price. There are different types of medications, such as: ointment, tablet, spray.
A doctor may prescribe a prescription at a visit that the patient can take to a Pharmacy.