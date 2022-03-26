# Pulse Gym Management

Python full-stack web app (CodeClan solo project)

![Pulse Gym Management - home page](/assets/images/home_page_ss.png)

### Introduction & Brief
Pulse Gym Management is a full-stack Python web app that I have designed and built as a solo project as part of my Professional Software Development PDA course at CodeClan. The brief was to build a piece of software to help a local gym to manage memberships, fitness classes and bookings. The app was to allow the gym to:
- Create and edit members and fitness classes
- Book members onto classes
- View a list of all upcoming classes
- View all members that are booked in for a particular class

In addition, the app also has the functionality to:
- Set a maximum capacity for individual fitness classes; users can only be booked onto a class while there is space remaining.
- Enable gym staff to assign Premium or Standard membership to gym members. Standard members can only be signed up for classes during off-peak hours.
- Enable gym staff to mark members and classes as active or inactive. Inactive members and classes are not available when creating bookings.
- Check in members on arrival to pre-booked fitness classes.

### Running Instructions
`flask run` in command line from root folder of project. Home page is accessible via your localhost port.

### Tech Stack
Python, Flask, PostgreSQL with psycopg package, HTML, CSS

![Pulse Gym Management - members page](/assets/images/members_ss.png)
![Pulse Gym Management - fitness classes page](/assets/images/fitness_classes_ss.png)
![Pulse Gym Management - new member page](/assets/images/add_new_member_ss.png)
![Pulse Gym Management - edit member details page](/assets/images/edit_member_details_ss.png)
![Pulse Gym Management - booking details page](/assets/images/booking_details_ss.png)
![Pulse Gym Management - fitness class page](/assets/images/class_details_ss.png)
![Pulse Gym Management - checking in booked members](/assets/images/check_in_booked_members_ss.png)
