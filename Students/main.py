import os
from classes.main import Main
from classes.db import DataBase

# Assuming this script is in the root directory of your project
current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, 'db')
db_file = os.path.join(db_dir, 'students.db')

main = Main('Students', '1000x500+10+10')
main.CreateMenu()

# Ensure the db directory exists
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Initialize the database connection string
DataBase.initialize(db_file)
connectionString = DataBase.getDbConnection()

if not os.path.exists(db_file):
    DataBase.createDB(connectionString)

main.run()
