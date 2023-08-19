import os
import sqlite3

working_directory = os.getcwd()

database_path = os.path.join(working_directory, 'pizza.sqlite')

conn = sqlite3.connect(database_path)
cursor = conn.cursor()
