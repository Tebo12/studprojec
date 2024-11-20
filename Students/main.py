import os
from classes.main import Main
from classes.db import DataBase
from classes.Model  import Model

# Initialize the main application
main = Main('Students', '1000x500+10+10')
main.CreateMenu()

# Get the database connection string
dbConnection = DataBase.getDbConnection()

# Ensure the "db" directory exists
if not os.path.isdir("db"):
    os.mkdir("db")

# If the database file does not exist, create tables
if not os.path.exists(dbConnection):
    Model.createTables()
    # Uncomment the next line if you need to explicitly create the database file
    # DataBase.createDB(dbConnection)

# Run the main application
main.run()
