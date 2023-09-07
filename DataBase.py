import sqlite3

class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.create_table()

    def create_table(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            cursor = self.conn.cursor()
            
            # Create a table with 'country_code' and 'contact' fields
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    country_code TEXT NOT NULL,
                    contact TEXT NOT NULL
                )
            ''')
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            if self.conn:
                self.conn.close()

    def insert_data(self, country_code, contact):
        try:
            self.conn = sqlite3.connect(self.db_name)
            cursor = self.conn.cursor()
            
            # Insert data into the 'contacts' table
            cursor.execute("INSERT INTO contacts (country_code, contact) VALUES (?, ?)", (country_code, contact))
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")
        finally:
            if self.conn:
                self.conn.close()

    def retrieve_data(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            cursor = self.conn.cursor()
            
            # Retrieve all data from the 'contacts' table
            cursor.execute("SELECT * FROM contacts")
            data = cursor.fetchall()
            
            return data
        except sqlite3.Error as e:
            print(f"Error retrieving data: {e}")
            return None
        finally:
            if self.conn:
                self.conn.close()

# # Example usage:
# if __name__ == "__main__":
#     db = MyDatabase("mydatabase.db")

#     # Insert sample data
#     db.insert_data("US", "123-456-7890")
#     db.insert_data("UK", "44-20-1234-5678")

#     # Retrieve and print data
#     data = db.retrieve_data()
#     if data:
        # for row in data:
        #     print(f"ID: {row[0]}, Country Code: {row[1]}, Contact: {row[2]}")
