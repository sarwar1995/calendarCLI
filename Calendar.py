#Sarwar Hussain

from Event import Event
from Meeting import Meeting
from Contact import Contact
class Calendar:
    """ Top level calendar class that manages the creation and deletion of events and the saving and loading of calendars to and from a csv file """
    """ list_of_events and list_of_contacts are the global calendar lists that are already sorted based on date/time and alphabetically, respectively"""
    def __init__ (self, list_of_events=None, list_of_contacts=None):
        if list_of_events==None:
            list_of_events = []
        if list_of_contacts==None:
            list_of_contacts = []
        self.__list_of_events = list_of_events
        self.__list_of_contacts = list_of_contacts

    def create_event (self, title=None, date=None, start_time=None, end_time=None, event_contacts=None): #This list of contacts is the local list
        """ Member function of the calendar class that creates an event or meeting if no conflicting events are present 
            and adds it to the list of events. It also adds the contacts of the newly created meeting to the list of existing contacts
            and adds the newly created meeting to the "meeting_lists" of all the contacts for that meeting """
        
        if(event_contacts):
            for ind, contact in enumerate(event_contacts):
                contIsPresent = self.contact_present(contact)
                if(not contIsPresent): 
                    pass
                else:
                    event_contacts[ind] = self.__list_of_contacts[contIsPresent[0]]
            Event_created = Meeting(title, date, start_time, end_time, event_contacts)
        else:
            Event_created = Event(title, date, start_time, end_time)

        #Checking for conflicts in this loop. The event class has a check_conflict function that does this.
        noConflict = 1
        if self.__list_of_events:
            for event_i in self.__list_of_events:
                isConflict = event_i.check_conflict(Event_created)
                if isConflict:
                    print ('Cannot add this event because it conflicts with this event...')
                    self.__list_of_events[isConflict[0]].print_event()
                    noConflict = 0
                    break
                else:
                    pass
            if noConflict:
                Event_created.add_event(self.__list_of_events) 
                if(event_contacts):
                    self.__add_contacts (event_contacts) # Calendar contact list is updated
            else:
                pass
        else: # When no conflicts are found with already present events, the event is "created" i.e. added to the list
            Event_created.add_event(self.__list_of_events) 
            if event_contacts:
                self.__add_contacts (event_contacts)


    def delete_event(self, index):
        """ Deletes the event from the list of events of the calendar class and from the list of events
        of the contacts associated with that event """
        meeting_to_be_deleted = self.__list_of_events[index-1]
        print('Deleted this event')
        meeting_to_be_deleted.print_event()
        for c in self.__list_of_contacts:
            c.delete_meeting(meeting_to_be_deleted)
        self.__list_of_events.pop(index-1)
    
    # def extract_event(self, index):
    #     """ Returns the event present at index-1 position in the list_of_events """
    #     return self.__list_of_events[index-1]
        

    def contact_present (self, new_contact):
        """ Checks if an input contact is present in the list of contacts """

        present = 0
        for ind, c in enumerate(self.__list_of_contacts):
            if(c == new_contact):
                index = ind
                present = 1
                return [index, present]
            else:
                pass
        return []


    def __add_contacts (self, event_contact_list):
        """ private method that adds new contacts from the event_contact_list to the Calendar's list of contacts """
        for event_contact in event_contact_list:
            if not event_contact in self.__list_of_contacts:
                self.__list_of_contacts.append(event_contact)
            else:
                pass
    
            
    def print_all_events (self):
        """ Print all events in sorted fashion """
        for event_i in self.__list_of_events:
            event_i.print_event()
            print('\n')
    
    def sort_contacts (self):
        """ Sorts all contacts and returns the sorted list """
        sorted_contacts = sorted(self.__list_of_contacts)
        if not sorted_contacts:
            print ('sorted contacts is empty')
        return sorted_contacts

    def print_all_contacts (self):
        """ Prints the sorted list of all contacts """
        sorted_contacts = self.sort_contacts()
        for contact_i in sorted_contacts:
            contact_i.print_contact()
            print('\n')

    def print_contact_meetings(self,name):
        """ Prints the sorted list of events associated with a particular contact with name=name """
        thecontact = Contact(name)
        check_contact = self.contact_present (thecontact)
        if not check_contact:
            return 0
        else:
            self.__list_of_contacts[check_contact[0]].print_meetings()
            return 1

    def reset(self):
        """ Resets the calendar to empty i.e. clears the list of all events and contacts """
        self.__list_of_contacts.clear()
        self.__list_of_events.clear()

    def save(self, file):
        """ Writes events to the file (default = 'calendar.csv') """
        for e in self.__list_of_events:
            e.write_to_file(file)

    def load(self, file):
        """ Loads list of events and contacts from the file after resetting the calendar i.e. overwriting it"""
        self.reset()
        for line in file:
            event_i = line.split(',')
            if len(event_i) == 4:
                self.create_event (event_i[0], event_i[1], event_i[2], event_i[3], [])
            elif len(event_i) > 4:
                event_i_contact_names = event_i[4:]
                event_i_contacts = []
                for name in event_i_contact_names:
                    if '\n' in name:
                        name=name.replace('\n','')
                    event_i_contacts.append(Contact(name))
                self.create_event (event_i[0], event_i[1], event_i[2], event_i[3], event_i_contacts)
            else:
                print('Missing information. Cannot load event.')

    

    
