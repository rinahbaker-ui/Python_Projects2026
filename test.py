import sqlite3  # Import SQLite so we can work with a database

# Create a tuple containing the names of several files
filelist = ('information.dox', 'Hello.txt', 'MyImage.png', 'MyMovie.mpg',
            'World.txt', 'data.pdf', 'myPhoto.jpg')

# Connect to the SQLite database called files.db
# If the database doesn't exist, SQLite will create it
conn = sqlite3.connect('files.db')

# Use the database connection
with conn:
    # Create a cursor to execute SQL commands
    cur = conn.cursor()

    # Create the files_tb table if it doesn't already exist
    # ID is automatically increased for each new record
    # file_name stores the name of the file
    cur.execute("CREATE TABLE IF NOT EXISTS files_tb( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")

    # Save the changes to the database
    conn.commit()

# Go through each file in the filelist
for file in filelist:

    # Check if the file name ends with '.txt'
    # Only text files will be added to the database
    if file.endswith('.txt'):

        # Create a cursor to execute the INSERT command
        cur = conn.cursor()

        # Insert the file name into the files_tb table
        # The ? is replaced safely with the value of file
        cur.execute("INSERT INTO files_tb (file_name) VALUES (?)", (file,))

        # Print the name of the text file that was found
        print(file)

    # Save the changes to the database
    conn.commit()

# Close the connection to the database when finished
conn.close()
