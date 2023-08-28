# Wedding Booking System by Salmz
This wedding booking app allowsthe user to book a wedding venue at one of three wedding venues in the West London radius. Its easy to use allowing the bride, groom and family to focus on other things.

Users are able to book in the venue view the booking as well as update the booking only after creating an account with us. After booking in the preferred venue users are encouraged to leave a review at the bottom of the page 

## User Experience (UX)
A user to Wedding Booking By Salmz would be the couple getting married and their families looking for an easy way to help their loved ones book a venue for their special day.
# 1.1 Strategy
## Project goals 
The main goal of this website is to allow the user to create an account  then have the authorisation to create a booking,view the booking, update and delete the booking.


## User Goals
First time visitor goals
As a first-time visitor i wanted to book a nearby venue in west London and the starting time of the event.
As a first timke user i want the ability to contact the venue with ease to get updates on how the venue is being prepared for the wedding.
As a first user i want the ability to view my booking after it has been made.

Returning visitor goals
As a returning user i want the ability to update the wedding date and time.
As a returning user i want the ability to cancel/delete the booking i have made.

Frequesnt user Goals
As a frequesnt user I want to check if any new nearby locations have been added to the list of venues.

## User expectations
The system should be easy to use and navigate around with each section being clear with each section being concise and easy to read.

The Menue is easy to read
The nav bar only displays the create and view booking options only once i have logged in.
The phone numbers of the 3 venues are listed on the footer and the bottom of the page.

### Strategy Table
Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Display a Booking Form | 5 | 5
Account signup | 5 | 5
User profile | 5 | 5
Responsive design | 5 | 5
Contact form | 3 | 4
Ability to create a booking | 5 | 4
Ability to update a booking | 5 | 4
Ability to cancel a booking | 3 | 4
Multiple table occupancies | 4 | 1
Avoid double bookings | 4 | 1

Total | 45 | 39

## Scope 

## Phase 1
In my scope I have identified the products that I believe make up my minimum viable product:
The ability to create an account.
The ability to create a booking
The ability to view booking after being created.
The ability to update the booking after it has been created.
Deleting bookings
Responsive design for accessibility 

## Phase 2 
Avoiding others from booking at the same time
One booking per account
Customerise django forms to make them more appealing.

# Structure 



### Database Model

This is my final database structure from models.py file 

class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    venue = models.CharField(max_length=100, blank=False)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    phone_number = models.CharField(max_length=20)
    theme = models.CharField(max_length=100, blank=True)
    group_size = models.PositiveIntegerField(default=100, validators=[MinValueValidator(100), MaxValueValidator(500)])
    # Other fields of the Booking model
    
class Register(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)

