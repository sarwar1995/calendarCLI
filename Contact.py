
from Event import Event
import functools

@functools.total_ordering
class Contact:
    def __init__ (self, name=None, list_of_meetings=None):
        if list_of_meetings == None:
            list_of_meetings = []
        self.name = name
        self.list_of_meetings = list_of_meetings

    # def __del__(self):
    #     print('Contact deleted.')

    def __lt__ (self, other):
        return self.name < other.name

    def __eq__ (self, other):
        return self.name == other.name

    def __str__ (self):
        return str(self.name)

    def add_meeting (self, meeting): 
        meeting.add_event (self.list_of_meetings)

    def delete_meeting(self, meeting):
        ind_to_remove = [ind for ind, m in enumerate(self.list_of_meetings) if m==meeting]
        if ind_to_remove:
            self.list_of_meetings.pop(ind_to_remove[0])
        else:
            pass


    def print_meetings(self):
        for meeting_i in self.list_of_meetings:
            meeting_i.print_event()
            print('\n')
    
    def print_contact(self):
        print(self.name)

