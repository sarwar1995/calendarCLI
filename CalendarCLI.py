#Sarwar Hussain

import sys, getopt
from Calendar import Calendar
from Contact import Contact

class CLI:
    def __init__ (self):
        self.NewCalendar = Calendar()    # Initialise a new instance of the calendar object
    

    def prompt(self):
        """ Prompt the user to enter a command via the CLI """

        print ('Enter Command:')
        print ('view, contacts, create, delete, load, save, quit')  
        cmd_entered = input()
        return cmd_entered

    def quit(self):
        """ Exit the calendar application """

        print ('Calendar application closed')
        sys.exit(0)

    def create_engine(self):
        """ Create a meeting or an event in the calendar and check for conflict with existing events """

        title = input('Title ?\n')
        date = input('Date ?\n')
        start_time = input('Start Time ?\n')
        end_time = input('End Time ?\n')
        isInvite = input('Invite others ? "Yes/yes" or "No/no" \n')
        if isInvite=="Yes" or isInvite=="yes":
            event_contacts = []
            name_i = input('"<Contact Name>" or "done"\n')
            while (name_i != 'done'):
                contact_i = Contact(name_i, [])
                event_contacts.append(contact_i)
                name_i = input('"<Contact Name>" or "done"\n')
            self.NewCalendar.create_event(title, date, start_time, end_time, event_contacts)
        elif isInvite=="No" or isInvite=="no":
            self.NewCalendar.create_event(title, date, start_time, end_time, [])
        else:
            print ('Enter either Yes/yes or No/no. Quitting...')
            self.quit()
        return None

    def view_engine(self):
        """ View either all events or all events associated with a particular contact in a sorted order """

        cmd_entered = input('"all" or "<contact name>"\n')
        if cmd_entered == 'all':
            self.NewCalendar.print_all_events()
        else:
            status = self.NewCalendar.print_contact_meetings(cmd_entered)
            if not status:
                print('No such contact present. Quitting... \n')
                self.quit()

    def contact_engine(self):
        """ View all contacts present in the calendar """

        sorted_contacts = self.NewCalendar.sort_contacts()
        for c in sorted_contacts:
            c.print_contact()

    def delete_engine(self, index):
        """ Deletes/removes the event at index (starting at 1) of the sorted list of events. Uses the __eq__ definition of
        the Event class to identify the meeting to be deleted in the Contact class's list_of_meetings and removes it.
        Does not remove the contacts associated with the removed event """        
        self.NewCalendar.delete_event(index)

        
    def save_engine (self, file='calendar.csv'):
        """ Saves the calendar in file """

        with open(file, 'w') as f:
            self.NewCalendar.save(f)
        print(f"Saved to {file}")

    def load_engine (self, file='calendar.csv'):
        """ Loads the calendar from file """

        with open(file, 'r') as f:
            self.NewCalendar.load(f)
        print(f"Loaded from {file}")

    def run(self):
        """ Run the CLI """

        cmd_entered = self.prompt()
        while (cmd_entered != 'quit'):
            if cmd_entered == 'create': # Creating a new event
                self.create_engine()
                cmd_entered = self.prompt()
            elif cmd_entered == 'delete':  # Deleting an existing event
                index_to_delete = input('Which event ? \n Enter an index 1..n to identify the event from the sorted list\n')
                self.delete_engine(int(index_to_delete))
                cmd_entered = self.prompt()
            elif cmd_entered == 'view':
                self.view_engine()
                cmd_entered = self.prompt()
            elif cmd_entered == 'contacts':
                self.contact_engine()
                cmd_entered = self.prompt()
            elif cmd_entered == 'save':
                self.save_engine()
                cmd_entered = self.prompt()
            elif cmd_entered == 'load':
                self.load_engine()
                cmd_entered = self.prompt()
            else:
                #If none of the valid command is enetered the CLI will ask again
                print('Not a valid command. Re-enter')
                cmd_entered = self.prompt()
        self.quit()
            
            

if __name__ == "__main__":
    CLI().run()
