#Sarwar Hussain
from tabulate import tabulate
from Event import Event
from Contact import Contact
class Meeting (Event):
    def __init__(self, title='default event', date='01-01-2020', start_time='00:00', end_time='24:00', list_of_contacts=None):
        super().__init__(title, date, start_time, end_time)
        if list_of_contacts == None:
            list_of_contacts = []
        self.list_of_contacts = list_of_contacts
        for participant in list_of_contacts:
            participant.add_meeting(self)

    def print_event(self):
        list_of_names = [c.name for c in self.list_of_contacts]
        joined_names = ', '.join(list_of_names)
        table = [[str(self.title)],["Date: "+str(self.date)],["Time: "+str(self.start)+" - "+str(self.end)],["Participants: "+str(joined_names)]]
        print(tabulate(table, tablefmt='grid'))

    def write_to_file(self, file):
        file.write(str(self.title)+",")
        file.write(str(self.date)+",")
        file.write(str(self.start)+",")
        file.write(str(self.end)+",")
        for ind, p in enumerate(self.list_of_contacts):
            if ind==(len(self.list_of_contacts)-1):
                file.write(str(p)+"\n")
            else:
                file.write(str(p)+",")
        