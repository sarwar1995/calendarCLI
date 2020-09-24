#Sarwar Hussain

from Event import Event
import functools

@functools.total_ordering
class Contact:
    def __init__ (self, name=None, list_of_meetings=None):
        if list_of_meetings == None:
            list_of_meetings = []
        self.__name = name
        self.__list_of_meetings = list_of_meetings

    # def __del__(self):
    #     print('Contact deleted.')

    def __lt__ (self, other):
        return self.__name < other.__name

    def __eq__ (self, other):
        return self.__name == other.__name

    def __str__ (self):
        return str(self.__name)

    def add_meeting (self, meeting): 
        """ Use the add_event function of Event class to add a new "meeting" to the list_of_meetings of self"""
        meeting.add_event (self.__list_of_meetings)

    def delete_meeting(self, meeting):
        """ Delete a meeting by finding it in the list_of_meetings using the overridden __eq__ function"""
        ind_to_remove = [ind for ind, m in enumerate(self.__list_of_meetings) if m==meeting]
        if ind_to_remove:
            self.__list_of_meetings.pop(ind_to_remove[0])
        else:
            pass


    def print_meetings(self):
        for meeting_i in self.__list_of_meetings:
            meeting_i.print_event()
            print('\n')
    
    def print_contact(self):
        print(self.__name)

