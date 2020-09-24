#Sarwar Hussain

from tabulate import tabulate
from Event import Event
from Contact import Contact
class Meeting (Event):
    def __init__(self, title='default event', date='01-01-2020', start_time='00:00', end_time='24:00', list_of_contacts=None):
        super().__init__(title, date, start_time, end_time)
        if list_of_contacts == None:
            list_of_contacts = []
        self.__list_of_contacts = list_of_contacts
        for participant in list_of_contacts:
            participant.add_meeting(self)

    def print_event(self):
        """ Print a meeting in the format specified in tabulate """

        list_of_names = [str(c) for c in self.__list_of_contacts]
        joined_names = ', '.join(list_of_names)
        table = [[str(self._title)],["Date: "+str(self._date)],["Time: "+str(self._start)+" - "+str(self._end)],["Participants: "+str(joined_names)]]
        print(tabulate(table, tablefmt='grid'))

    def write_to_file(self, file):
        file.write(str(self._title)+",")
        file.write(str(self._date)+",")
        file.write(str(self._start)+",")
        file.write(str(self._end)+",")
        for ind, p in enumerate(self.__list_of_contacts):
            if ind==(len(self.__list_of_contacts)-1):
                file.write(str(p)+"\n")
            else:
                file.write(str(p)+",")
        