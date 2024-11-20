import sqlite3

# Establishing a connection to the database
connection = sqlite3.connect('db/DataBase.db')
cursor = connection.cursor()


"-1:14:01"
cursor.execute("SELECT * FROM Subjects, Students, Achievements")
Subjects = cursor.fetchall()
print(Subjects)
#for subject in Subjects:
    #print(subject[1])
 #   print("ID:",Subjects[0])
  #  print("Name:", Subjects[1])
"""
achivment_list=[]
# Displaying results
for achivment in Achivments:
    cursor.execute('SELECT * FROM Students WHERE id='+str(achivment[1]))
    student_name = cursor.fetchall()
    cursor.execute('SELECT * FROM Subjects WHERE id='+str(achivment[2]))
    subject_name = cursor.fetchall()
    achivment_list.append([student_name,subject_name,achivment[3]])

for item in achivment_list:
    print(item)
# Closing the connection
connection.close()
"""