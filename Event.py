#Sarwar Hussain

from tabulate import tabulate

class Event:
    def __init__ (self, title='default event', date='01-01-2020', start_time='00:00:00', end_time='24:00:00'):
        self._title = title
        self._date = date
        self._start = start_time
        self._end = end_time
    
    def get_linear_start(self):
        """ Obtain the linearized value of start time i.e. linear_start = 60*start_min + 60*60*start_hour
        This and get_linear_end are used for the __lt__ function """

        start_hour = int(self._start[0:2])
        start_min = int(self._start[3:5])
        linear_start = 60*start_min + 60*60*start_hour
        return linear_start
    
    def get_linear_end(self):
        """ Obtain the linearized value of end time """

        end_hour = int(self._end[0:2])
        end_min = int(self._end[3:5])
        linear_end = 60*end_min + 60*60*end_hour
        return linear_end


    def get_linear_range(self):
        """ Obtain the linearized range i.e. [start, end] """

        linear_range = [self.get_linear_start(), self.get_linear_end()]
        return linear_range

    def check_conflict(self, event):
        """ Check conflict of self with event. If the range of self intersects with range of event than a conflict is present """
        check = []
        date = event._date
        slot = event.get_linear_range()
        if self._date == date: # Assuming that all events start and end b/w 00:00 and 23:59. Date matches
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
        date_list.append(int(self._date[0:4])) # Year
        date_list.append(int(self._date[5:7])) # Month
        date_list.append(int(self._date[9:]))  # Day
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
        return (self._title == other._title and self._date == other._date and self._start == other._start and self._end == other._end)

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
        table = [[str(self._title)],["Date: " + str(self._date)],["Time: " + str(self._start)+" - " + str(self._end)]]
        print(tabulate(table, tablefmt='grid'))

    def write_to_file(self, file):
        file.write(str(self._title)+",")
        file.write(str(self._date)+",")
        file.write(str(self._start)+",")
        file.write(str(self._end)+"\n")

        

        


    






