import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('products.db')  # Connect to the database (creates the file if it doesn't exist)
        cursor = conn.cursor()

        # Create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        # Insert data
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')

        conn.commit()  # Commit the transaction
        conn.close()  # Close the connection
        print("Database created and populated successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    create_database()
