| Date | Week 11/12 |
| ------------------- | ---------------------------- |
| Version | 2018 - Marcel V, Inge |
| Learning Objectives | Analysis, Design, Realization |
| Required Prior Knowledge | Analysis |
| Challenge Type | Integral Application |




To: Software development group &quot;The Gurus&quot;
Subject: hotel reservation system specification
Dear developers,
Herewith the specifications for the hotel system to be built as agreed upon:
### Description.
Hotel Reeënrust is currently working with a complicated system of Excel files
to keep track of the reservations. They would like to keep the reservations
in an application, so that the employees at the front desk can
can easily enter the reservations.
Later, a website would also be nice, so customers could
make their reservations, but for now the focus is on the application
for the front desk.
It is important that the application be user-friendly and that the user
gets the right notifications.

### Scenario

A customer calls the front desk to reserve a room.
The receptionist enters the customer information and checks to see which room
room is available for the specified time period.
If the reservation is for more than 4 people,
multiple rooms will need to be reserved.
Furthermore the customer indicates per reserved room
Whether breakfast and/or dinner will be used.
The receptionist can at any time request an overview
of all reservations in the hotel. She can also view a list
which shows per date which rooms participate in breakfast or dinner.
The customer data is stored in a text file.

### Requirements

- The employee can enter customer data (name and address).
- The employee can make a reservation. A reservation can only be made in the future.
- The employee can see which rooms are available for a certain period of time.
- The customer data is stored in a text file.
- The employee can view an overview of all reservations.
- The employee can consult an overview of a certain date showing which rooms participate in breakfast or dinner.


### Properties of the hotel
- There are 120 rooms. Room 13 does not exist.
- All rooms can accommodate up to 4 people (this might change in the future)


### Extra

- It would be nice if reservations could also be saved in a text file. (Hint: For this you need to use "Serialization")


Yours faithfully,

Mr. Drs. P. van Trommelen
Director Hotel Reeënrust
![](figures/logo_hotel.png "logo hotel")