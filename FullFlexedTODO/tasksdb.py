import sqlite3


class SqDB:
    
    def __init__(self) -> None:
        self.conn = sqlite3.connect('tasksdatabase.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks(
                    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_text TEXT NOT NULL,
                    time_created REAL DEFAULT (datetime('now', 'localtime'))
                )
                """)
        

    def add_task_db(self, task_list):
        
        self.cursor.executemany("INSERT INTO tasks(task_text) VALUES (?)", task_list)
        self.conn.commit()
        ...

    def retrieve_tasks(self):
        
        self.cursor.execute("SELECT * from tasks")

        tasks_list = self.cursor.fetchall()

        return tasks_list
    
    def remove_task(self,  remove_item):
        
        delete_query = """DELETE from tasks WHERE task_id = ?"""
        self.cursor.executemany(delete_query, remove_item)
        # print(self.cursor.rowcount())
        self.conn.commit()
    def rearrange_id(self):
        self.cursor.execute("SELECT * FROM tasks ORDER BY task_id")
        records = self.cursor.fetchall()

        # Close the connection
        # conn.close()

        # Determine new primary key values
        new_primary_keys = list(range(1, len(records) + 1))

        # Update the primary key values in the table
        # conn = sqlite3.connect("your_database.db")
        # cursor = conn.cursor()

        for i, record in enumerate(records):
            current_primary_key = record[0]  # Assuming the current primary key is the first column
            new_primary_key = new_primary_keys[i]
            
            self.cursor.execute("UPDATE tasks SET task_id = ? WHERE task_id = ?", (new_primary_key, current_primary_key))

        # Commit the changes and close the connection
        self.conn.commit()
        # conn.close()
        

    # def 

obj = SqDB()
# remove_item = [(2, ), (4,)]
# obj.remove_task(remove_item)
obj.rearrange_id()
print(obj.retrieve_tasks())


