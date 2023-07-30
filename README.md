# bus_booking_system_V1_using_python

# Bus Ticket Booking System

This is a simple Bus Ticket Booking System implemented in Python. It includes classes to represent users, buses, and a counter for managing bus operations.
# User Class
The User class represents a user with a username and password.
# Bus Class
The Bus class represents a bus with various attributes like coach number, driver name, arrival and departure times, starting and ending points, and a list of seats.

# Counter Class

The Counter class inherits from the waqas class and acts as the main interface for users and admins. It provides the following functionalities:

1. Create an Account: Users can create an account by providing a username and password.
2. Login: Users can log in to their accounts using their credentials.
3. View Available Buses: Users can check the list of available buses.
4. Show Bus Info: Users can view detailed information about a specific bus.
5. Reservation: Users can reserve seats on a bus by providing their name and seat number.
6. Add Bus (Admin Only): Admins can add new buses to the system.
# Usage
1. Run the script to start the Bus Ticket Booking System.
2. Choose an option to either create an account or log in (Admin login is "Waqas" with password "waqas12").
3. After logging in, you can check available buses, view bus info, reserve seats, and, if you are an admin, add new buses.
# Note
This is a basic implementation of a Bus Ticket Booking System for learning purposes. In a real-world scenario, more robust features like database integration, payment processing, and user authentication mechanisms would be necessary.
