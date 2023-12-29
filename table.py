

class Table:

    def __init__(self, table, users, times, places, axis_x_len, axis_y_len,valus_num, time_gap):
        self.table = table
        self.users = users
        self.times = times
        self.places = places
        self.axis_x_len = axis_x_len
        self.axis_y_len = axis_y_len
        self.valus_num = valus_num
        self.time_gap = time_gap
        

    def table_placer(self):
        count_of_places = 0
        count_of_places = 0
        table_structure = self.table
        valus_num = self.axis_x_len * self.axis_y_len + self.axis_x_len + self.axis_y_len + 1
        time_position = self.axis_x_len + self.axis_x_len + 1
        start_position = self.axis_x_len + 1
        end_position = self.axis_x_len + 1
        # place placer
        for axis_x in self.places:
            table_structure[count_of_places] = axis_x
            count_of_places += 1
            if count_of_places == self.axis_x_len:
                table_structure[count_of_places] = "  "
            else:
                continue
        # time placer
        if table_structure[count_of_places] == "  ":
            for axis_y in self.times:
                      
                if time_position < valus_num: 
                    table_structure[time_position] = axis_y
                    time_position += self.axis_x_len + 1
                else:
                    continue
        # user placer 
        if self.time_gap == 3:
            
        
            pass
        return table_structure
        
    def ensure_value_not_in_ranges(table, forbidden_value, *ranges):
    # Check and modify the array for each specified range
        for start, end in ranges:
            for i in range(start - 1, end):
             if table[i] == forbidden_value:
                table[i] = None 
                return table
