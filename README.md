# Wedding Booking System by Salmz
This wedding booking app allowsthe user to book a wedding venue at one of three wedding venues in the West London radius. Its easy to use allowing the bride, groom and family to focus on other things.

Users are able to book in the venue view the booking as well as update the booking only after creating an account with us. After booking in the preferred venue users are encouraged to leave a review at the bottom of the page 

## User Experience (UX)
A user to Wedding Booking By Salmz would be the couple getting married and their families looking for an easy way to help their loved ones book a venue for their special day.
### User stories
I used github as my method of agile methodology. To keep track of tasks so i knew which tasks i had to prioritise and what I had left to do. When working on something I will move it to in progress. When finished the task would be moved to the completed section.

![USER STORIES](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/741beb45-d513-44be-ad99-71c086cfd9eb)




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

Total | 44 | 38

## Scope 
The main functions iused are listed in phase 1 and 2 phase 1 being the more important features like the CRUD functionality.

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
### Database plan
Initially i had this model for the database, which is what I followed to make the database models. Though the register one was not used
![database model](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/6bc2e260-d2a2-45a6-a042-006cc775beaa)


### Database Model

This is my final database structure from models.py file 

![database](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/576a73f1-0db1-43bd-8fc5-12eae578dcfb)

The register model was not used as I used Djangos Aullauth for the registering accounts functioning.

# Skeleton 
## Wireframes
Homepage:

https://wireframe.cc/5kcdOL

Booking form:

https://wireframe.cc/fRG08J

The wireframes above are for the homepage as well as the create bookings page. I initially did not know how I wanted the booking form to look like which is why the wireframe only has the contents of whats to be written on the form instead of the design.

# Surface 
 This is the colour scheme I used for the website:

 https://coolors.co/b4c1d3-ffffff-fefefe-d9d8d9

 For the font i used Oswald from google fonts which can be found [here](https://fonts.google.com/specimen/Oswald)

 ## Features
 ### Nav Bar
 The nav bar is at the top of every page allowing the user to navigate between pages and is dynamic so the users have access to the CRUD functionality once thry have created an account and logged in with us.

 When logged in the nav bar looks like this:
 ![logged in](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/aa9ccbc9-90d9-438e-94c6-d82d99677184)

 When logged out the nav bar looks like this:
 ![logged out](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/c7c14e7e-6f9a-45da-970b-2e5b32ef8bff)

 The nav bar contains a basic logo so users can click and return back to the homepage.

 ## Register Page
 Sign in page is very simple user is prompted to enter in their username and password and they have the option of remember me if they want their PC to keep a recording of their details.

 ![sign in ](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/fa6130c3-aaa6-490f-bfec-e2863d876592)

 ![sign up p](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/671d611b-fce7-4e2b-a7d3-b34157b6721f)

 Signup form  prompts the user to enter a unique email address and a password. The password must be entered again for confirmation, this must match the already entered password above.

 A message to prompt the user if an account is already been created they can click the sign-in hyperlink to be redirected to the sign-in page.
 If the user enters an email address that has already been registered, the user is prompted by an error message.

For validation when the user is signing up and they enter in an email which has been previously registered it will say "A user is already registered with this email".

Moreover if the password entered doesnt match the previously entered one it will say "You must type the same password each time"

![SIGN UP VALIDATION](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/5a8e2fed-b06f-476f-bef0-bf107c5d086b)

When the user enters in the wrong details whilst logging in it will look like this:

![sign in validation](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/be13272e-0501-4009-ba13-f0ed5434d5e9)

## Log out page
When logging out it will say are you sure you want to sign out just incase the user incorrectly pressed the button.

## Landing page

Once the user enters the website they will be presented with a blue button which says create a booking with us. Once pressed the user would be directed to the create bookings page but if not authenticated they will be directed to the login/signup page.

## About us page

Has little text about the history of the business and why we started it.

## Create Booking Page
When clicking the create booking page the user is presented with a form asking for them to enter their desired venue of the 3 provided, their name, what their booking time is, their email, phone number, Desired theme/colour of venue and the Group Size.
![create booking p](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/788710bf-94c7-44c8-9b92-a80ad9c8096f)

## View Booking Page
When clicked, this allows the user to see their booking details just incase they want to make changes in the future.

## Update Booking Page
This is where the user can update their booking times,group sizes or date if something hasnt gone to plan and they are able to change just the group size without any errors ocurring.

## Delete Booking Page 
When clicked, the user will be able to see their booking details and a confirm delete button for convinience just incase the delete button was pressed by accident.

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project uses HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project uses Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project uses JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project uses Python.
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -   The project uses Bootstrap 5.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project uses PostgreSQL as a database.
-   [Gitpod](https://www.gitpod.io/)
    -   The project uses Gitpod.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project uses Chrome to debug and test the source code using HTML5.  
-   [Google Fonts](https://fonts.google.com/)
    -   Google fonts were used to import the "Be Vietnam Pro" font into the style.css file which is used on all pages throughout the project.
-   [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.


# Testing

For css testing i used [W3C](https://jigsaw.w3.org/css-validator/)

I got no errors for my CSS 
![css validator](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/228c3a50-b3ff-4ab4-b67d-2a3666b4ad58)

My HTML initially had a warning to do with the h1 being the main title and not the logo so i changed it to h2. So no more HTML errors.

![html validation](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/3825f646-5649-4315-b9b6-8caf06f2e264)

For the main python files i used there are no longer any errors though on one of them it says line too long but there is no way to change the length as the form contains all of my fields and therefore the line cannot be shortened.

![forms pytesting](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/001554d8-afcc-4b85-beae-ec478978e301)

![views py validation](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/70e29a69-2d94-4274-b1cf-e3cd1fd2fecb)

As i used a bit of javascript I used JS Hint to test the code which resulted in it saying that $ wasnt defined. As this was in a script tag i left the code how it was.

![JS ](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/f8cd9f92-217c-43eb-9e3d-fe757790df9f)

## Manual testing
I have tested my site on Safari and Microsoft Edge on multiple devices.

These include:
-   iPhone 12 pro
-   hp laptop
-   Desktop
-   i pad

Please find below my testing process for all pages via mobile and web:

### Navigation Bar

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home page | When clicking the "home" button in the navigation bar, the browser redirects me to the home page.  | PASS
About page | When clicking the "About Us" button in the navigation bar, the browser redirects me to the About page.  | PASS
Create Booking page | When clicking the "create booking" button in the navigation bar, the browser redirects me to the create booking page and i was able to make a booking | PASS

Manage booking page | When clicking the "manage bookings" button in the navigation bar, the browser redirects me to the manage booking page. The user will know they are on this page by the heading. | PASS

Edit profile page | Checked foreground information is not distracted by backgrounds| PASS


Login / Logout page | When clicking the "login" or "logout button in the navigation bar, the browser redirects me to the login or logout page. The user will know they are on this page by the heading. | PASS

Foreground & background colour | Checked foreground information is not distracted by background animation. | PASS
Text | Checked that all fonts and colours used are consistent. | PASS

### Footer
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Facebook | When clicking the Facebook icon, a new tab opens and redirects to the Facebook website. | PASS
Twitter | When clicking the Twitter icon, a new tab opens and redirects to the Twitter website. | PASS
Instagram | When clicking the Instagram icon, a new tab opens and redirects to the Instagram website. | PASS

### Home page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
![light house test for homepage](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/0620a3b8-9900-418d-ac0e-a66a70cd163b)



### about page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page.But this is only when the user is logged in | PASS

Accessibility | Checked the accessibility of the page using lighthouse| PASS
![about us test](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/dd4d3af4-880d-4434-8dc6-1705dc6d3ea2)

## View Booking page
The view booking page works fine on all devices it correctly shows the bookings.
![view booking test](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/c97248f2-0b76-4525-9369-819e4308fd3d)

## Update/Delete booking 
Both of these links are working correctly when clicked on and the user can successfully delete and update their booking. There are no problemswith how they look and responsiveness.

![update booking test](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/9c35d79d-8d4d-44f5-b191-6415c0b610a5)

![delete booking test](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/cd8c2bef-fca8-4044-957c-df6eb4356bac)

# Known Bugs
 - there is one bug where the the success messages bring the padding of everything else down until they disappear.

 - When the user is updating their booking and they press update booking without making any changes it still says updated booking instead of something like "No changes made".
 - When running my code through a pylinter on the forms.py file there is a line that is said to be too long but there is not much i can do in order to make it shorter i attempted it and I beleive its ok now


 ## Content 
  Greenford hall picture: https://i.pinimg.com/originals/61/7e/79/617e79acb4346547953dbdec5f1a5fe4.jpg

  Hownslow hall pic: https://th.bing.com/th/id/OIP.GzHwjWB706KfnJkhXw4QuAAAAA?pid=ImgDet&rs=1

  slough hall picture: https://th.bing.com/th/id/OIP.2gMm1iIxcx8fLC6CVFTdhQHaE7?pid=ImgDet&w=180&h=180&c=7&dpr=1.3

  social media icons: https://fontawesome.com/

  ## References

  I used this project for inspiration which helped me build the backend of my app i used this for my view.py as well as an idea for my database models: https://github.com/iKelvvv/MS4/tree/main

  This project gave me an idea on how to set up my form as well as the idea of the small images going across the page
  : https://github.com/AliOKeeffe/mindyoga

  w3schools: https://www.w3schools.com/

  Bootsrap : https://getbootstrap.com/

## Log in/ signup pages
The functionality of these pages are up to par they are both responsive. The validation for both are working. The sign up page is also responsive the validation is in check and the colours are contrasting therefore improving accessibility.
Log In Page:
![log in page test](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/90f76f59-4f0e-4965-af89-071083d3e6b8)
Log Out Page:
![log out test](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/1af6496c-5b9c-4f4e-b8cd-a901db280e79)

Sign Up Page:
![sign up page test](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/1217b161-3dd9-404d-9574-8b06f1875950)

# Final Product


![main page](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/50ebee36-fbb6-40b8-a930-8c57a170ec60)


![view bookings page](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/ec81570c-4f75-4571-aa0a-69b662434e90)


![About Us page](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/6af20ac7-37f0-4370-843f-dd9c6df396bf)


![create booking page](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/507f095a-b391-4ec5-923a-b58462324ed7)

![signup page](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/305e6bdd-8356-486f-b60d-9b94e8ffafa4)


![sign in page](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/8f3a191f-a896-4684-b6b2-24a986afc10c)


![signout page](https://github.com/salms358/Wedding-Booking-By-Salmz/assets/119611403/ec8f9472-7d81-4048-ada7-0ee43d8cc112)

# Developmental cycle 
## Project Checklist
- Install Django and the supporting libraries
    -  Install Django and Gunicorn. Gunicorn is the server I am using to run Django on Heroku.
    - Install support libraries including psycopg2, this is used to connect the PostgreSQL database
    - Install Cloudinary libraries, this is a host provider service that stores images
    - Create the requirements.txt file. This includes the project's dependencies allowing us to run the project in Heroku.

- Create a new, blank Django Project
    - Create a new project
    - Create the app
    - Add restaurant_booking to the installed apps in settings.py
    - Migrate all new changes to the database
    - Run the server to test

- Setup project to use Cloudinary and PostgreSQL
    - Create new Heroku app
        - Sign into Heroku
        - Select New
        - Select create new app
        - Enter a relevant app name
        - Select appropriate region
        - Select the create app button

    - Attach PostgreSQL database
        - In Heroku go to resources
        - Search for Postgres in the add-ons box
        - Select Heroku Postgres
        - Submit order form

    - Prepare the environment and settings.py file
        - Create env.py file
        - Add DATABASE_URL with the Postgres URL from Heroku
        - Add SECRET_KEY with a randomly generated key
        - Add SECRET_KEY and generated key to the config vars in Heroku
        - Add if statement to settings.py to prevent the production server from erroring
        - Replace insecure key with the environment variable for the SECRET_KEY
        - Add Heroku database as the back end
        - Migrate changes to new database

    - Get static media files stored on Cloudinary
        - Create a Cloudinary account
        - From the dashboard, copy the API Environment variable
        - In the settings.py file create a new environment variable for CLOUDINARY_URL
        - Add the CLOUDINARY_URL variable to Heroku
        - Add a temporary config var for DISABLE_COLLECTSTATIC
        - In settings.py add Cloudinary as an installed app
        - Add static and media file variables
        - Add templates directory
        - Change DIR's key to point to TEMPALTES_DIR
        - Add Heroku hostname to allowed hosts
        - Create directories for media, static and templates in the project workspace
        - Create a Procfile

- Deploy new empty project to Heroku




# Deployment

[Go to the top](#table-of-contents)

I used the terminal to deploy my project locally. To do this I had to:
1. Create a repository on GitHub.
2. Clone the repository on your chosen source code editor (GitPod in my case) using the clone link.
3. Open the terminal within GitPod
4. Enter "python3 manage.py runserver into the terminal.
5. Go to local host address on my web browser.
6. All locally saved changes will show up here.

For the final deployment to Heroku, I had to:
1. Uncomment the PostgreSQL databse from my settings.py file.
2. Set debug = False in my settings.py file.
3. Commit and push all files to GitHub
3. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
4. In the deploy tab, go to the manual deploy sections and click deploy branch.

I had an issue with the deployed site and the CSS was not showing on my screen.
This was rectified by restarting all dynos in Heroku.