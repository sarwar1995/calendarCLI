#Sarwar Hussain
from tabulate import tabulate

class Event:
    def __init__ (self, title='default event', date='01-01-2020', start_time='00:00:00', end_time='24:00:00'):
        self.title = title
        self.date = date
        self.start = start_time
        self.end = end_time
    
    def get_linear_start(self):
        start_hour = int(self.start[0:2])
        start_min = int(self.start[3:5])
        linear_start = 60*start_min + 60*60*start_hour
        return linear_start
    
    def get_linear_end(self):
        end_hour = int(self.end[0:2])
        end_min = int(self.end[3:5])
        linear_end = 60*end_min + 60*60*end_hour
        return linear_end


    def get_linear_range(self):
        linear_range = [self.get_linear_start(), self.get_linear_end()]
        return linear_range

    def check_conflict(self, event):
        check = []
        date = event.date
        slot = event.get_linear_range()
        if self.date == date: # Assuming that all events start and end b/w 00:00 and 23:59. Date matches
            slot_i = self.get_linear_range()
            if((slot[0] <= slot_i[0] and slot[1] <= slot_i[0]) or (slot[0] >= slot_i[1] and slot[1] >= slot_i[1])):
                check.append(False)
            else:
                check.append(True)
        else:
            check.append(False)
        conflict_index = [counter for counter, checkcomp in enumerate(check) if checkcomp]
        return conflict_index

    def __extract_date (self):
        """ Extracts numerical year, month and day from the string date
        and returns a list containing [year, month , day]"""
        date_list = []
        date_list.append(int(self.date[0:4])) # Year
        date_list.append(int(self.date[5:7])) # Month
        date_list.append(int(self.date[9:]))  # Day
        return date_list

    def __lt__ (self, event):
        """ An event is less than another if it starts before the other event """
        self_date = self.__extract_date()
        event_date = event.__extract_date()
        if self_date[0] < event_date[0]:
            return True
        elif self_date[0] == event_date[0]:
            if self_date[1] < event_date[1]:
                return True
            elif self_date[1] == event_date[1]:
                if self_date[2] < event_date[2]:
                    return True
                elif self_date[2] == event_date[2]:
                    if (self.get_linear_start() < event.get_linear_start()):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__ (self, other):
        """ Two events are equal if their title, date, start and end times match exactly. As such this calendar allows for 
        events with similar titles and dates, as long as they are not conflicting """
        return (self.title == other.title and self.date == other.date and self.start == other.start and self.end == other.end)

    def add_event (self, list_of_events):
        """ A function that adds the event (self) at its correct sorted place in a supplied list of events """

        if (not list_of_events):   # Simply append if list of events is empty
            list_of_events.append(self)
        else:
            check_current_list = [self < event_i for event_i in list_of_events]
            insert_index = [ind for ind, i in enumerate(check_current_list) if i==True]
            if insert_index:
                list_of_events.insert(insert_index[0], self)
            else:
                list_of_events.append(self)


    def print_event(self):
        table = [[str(self.title)],["Date: " + str(self.date)],["Time: " + str(self.start)+" - " + str(self.end)]]
        print(tabulate(table, tablefmt='grid'))

    def write_to_file(self, file):
        file.write(str(self.title)+",")
        file.write(str(self.date)+",")
        file.write(str(self.start)+",")
        file.write(str(self.end)+"\n")

        

        


    






