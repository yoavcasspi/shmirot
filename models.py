# db controller
import mysql.connector
import json
from table import Table

connection = mysql.connector.connect(
   host = "127.0.0.1",
   user = "root",
   password = "yoav1303",
   database = 'shmirot',
   port=5000
)
# Create a connection string

cursor = connection.cursor()

# queries
queries = {
"select_all_users": "SELECT * from users",
"select_all_times": "SELECT * from times",
"select_all_places": "SELECT * from places"
}



class Methods:
     def __init__(self):
        # Initialize your class attributes here if needed
        pass
     
     def get_all_users(self): 
         cursor.execute(queries["select_all_users"])
         rows = cursor.fetchall()
         names_table = []
         for names in rows:
             names_table.append(f"{names[2]} {names[3]}")
             
         return names_table
     
     def get_all_times(self):
         cursor.execute(queries["select_all_times"])
         rows = cursor.fetchall()
         times_table = []
         time_gap = []
         for times in rows:
             times_table.append(times[2])
             time_gap.append(times[3])
         
         return {"times_table": times_table, "time_gap": time_gap[0]}
     
     def get_all_places(self):
         cursor.execute(queries["select_all_places"])
         rows = cursor.fetchall()
         names_table = []
         for names in rows:
             names_table.append(names[2])
             
         return names_table
     

     def generate_table_api(self):
            users = self.get_all_users()
            times = self.get_all_times()
            time_table = times["times_table"]
            time_gap = int(times["time_gap"])
            places = self.get_all_places()
            axis_x_len = len(places)
            axis_y_len = len(time_table)
            valus_num = axis_x_len * axis_y_len + axis_x_len + axis_y_len + 1
            table_creator = Table([i for i in range(1, valus_num +1)], users, time_table, places, axis_x_len, axis_y_len,valus_num, time_gap)

            if places and times and users:
              table = table_creator.table_placer()
              return table


            