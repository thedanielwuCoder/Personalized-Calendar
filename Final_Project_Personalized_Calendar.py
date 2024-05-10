#import necessary libraries
import json
from datetime import datetime, timedelta

#Event Management for both Event and Calendar Classes to add edit delete display save and load events with attributes of name date, time, description, and reminder
#Define Event Class to represent different events
class Event:
    def __init__(self, name, date, time, description, reminder):
        self.name = name
        self.date = date
        self.time = time
        self.description = description
        #reminder system
        self.reminder = reminder

#Define Calendar Class to manage and view events like a normal calendar
#also view options as well
class Calendar:
     #intialize empty list to store events
    def __init__(self):
        self.events = []

    #add new event to list 
    def add_event(self, event):
        self.events.append(event)

    #edit a current event
    def edit_event(self, event_name, new_event):
        for event in self.events:
            if event.name == event_name:
                event.__dict__.update(new_event.__dict__)
                break
    
    #delete an event
    def delete_event(self, event_name):
        self.events = [event for event in self.events if event.name != event_name]

    #display an event that was recently added or was there prior 
    def display_events(self):
        for event in self.events:
            print(f"Event: {event.name}\nDate: {event.date}\nTime: {event.time}\nDescription: {event.description}\nReminder: {event.reminder}\n")

    #Save Event (Data Storage)
    def save_to_file(self):
        with open("calendar_data.json", "w") as file:
            json.dump([event.__dict__ for event in self.events], file)

    #load saved event (Data Storage)
    def load_from_file(self):
        try:
            with open("calendar_data.json", "r") as file:
                data = json.load(file)
                self.events = [Event(**event_data) for event_data in data]
        except FileNotFoundError:
            pass

# Example usage of the Calendar Class
def main():
    calendar = Calendar()
    calendar.load_from_file()

    while True:
        #display user menu
        print("1. Add Event")
        print("2. Edit Event")
        print("3. Delete Event")
        print("4. View Events")
        print("5. Save and Quit")

        #get the input that the user selected or the choices 
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time: ")
            description = input("Enter event description: ")
            reminder = input("Enter reminder time before the event: ")

            event = Event(name, date, time, description, reminder)
            calendar.add_event(event)
            print("Event added successfully!\n")

        elif choice == "2":
            event_name = input("Enter the name of the event to edit: ")
            new_name = input("Enter new event name: ")
            new_date = input("Enter new event date (YYYY-MM-DD): ")
            new_time = input("Enter new event time: ")
            new_description = input("Enter new event description: ")
            new_reminder = input("Enter new reminder time before the event: ")

            new_event = Event(new_name, new_date, new_time, new_description, new_reminder)
            calendar.edit_event(event_name, new_event)
            print("Event edited successfully!\n")

        elif choice == "3":
            event_name = input("Enter the name of the event to delete: ")
            calendar.delete_event(event_name)
            print("Event deleted successfully!\n")

        elif choice == "4":
            calendar.display_events()

        elif choice == "5":
            calendar.save_to_file()
            print("Calendar saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

#execute the main function
if __name__ == "__main__":
    main()

