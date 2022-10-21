import sqlite3

class ExpenseTrackerDatabase():
    def __init__(self):
        self.database = sqlite3.connect("expense_tracker_database.db")
        self.cursor = self.database.cursor()
        #self.create_table()

    def create_table(self):
        self.cursor.execute('''
                CREATE TABLE expenses (
                    id integer,
                    category string,
                    cost integer,
                    date string,
                    details text )
            ''')

    def add_row(self, id, category, cost, date, details):
        self.cursor.execute(f'''
            insert into expenses (id, category, cost, date, details) values ({id}, "{category}", {cost}, "{date}", "{details}")
        ''')
        self.database.commit()

    def sum(self):
        self.cursor.execute('SELECT SUM(cost) FROM expenses')
        total_sum = self.cursor.fetchone()
        if total_sum[0] is None:
            return 0
        else:
            return total_sum[0]

    def reset_database(self):
        self.cursor.execute('DELETE FROM expenses')
        self.database.commit()

    
    def data_for_pie(self):
        sums = []
        self.cursor.execute('SELECT sum(cost) FROM expenses GROUP BY category')
        result = self.cursor.fetchall()
        for element in result:
            sums.append(element[0])
        
        categories = []
        self.cursor.execute('SELECT (category) FROM expenses GROUP BY category')
        result = self.cursor.fetchall()
        for element in result:
            categories.append(element[0])
        
        return (sums, categories)


    def __del__(self):
        self.database.close()

db = ExpenseTrackerDatabase()
db.data_for_pie()
