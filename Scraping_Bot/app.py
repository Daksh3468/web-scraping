from flask import Flask,render_template
import mysql.connector
from sites.SandeshNewsScaper import sandeshnews
from sites.divyaBhaskar import divyabhaskar
#Chrome Driver Version: 113.0.5672.24
from tests.gujaratsamachar import run_gujaratsamachar
import os 

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    port='3306',
    password="",
    database="tempdb"
)
cursor = db.cursor()

# Create table
create_table_query = """
    CREATE TABLE IF NOT EXISTS news1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        image VARCHAR(255),
        link VARCHAR(255)
    )
"""
cursor.execute(create_table_query)


# Data from Gujarat Samachar
data_gs=run_gujaratsamachar()
print("Data From Gujarat Samachar:")
print(data_gs)

# Data from Sandesh
data_ss=sandeshnews()
print("Data From Sandesh News:")
print(data_ss)

# Data from Divya Bhaskar
data_db= divyabhaskar()
print(data_db)


# Insert data into the database
insert_query = "INSERT INTO news1 (title, image, link) VALUES (%s, %s, %s)"
values = (data_ss['title'], data_ss['img_src'], data_ss['link'])
cursor.execute(insert_query, values)
db.commit()

insert_query = "INSERT INTO news1 (title, image, link) VALUES (%s, %s, %s)"
values = (data_gs['title'], data_gs['img_src'], data_gs['link'])
cursor.execute(insert_query, values)
db.commit()

insert_query = "INSERT INTO news1 (title, image, link) VALUES (%s, %s, %s)"
values = (data_db['title'], data_db['image'], data_db['link'])
cursor.execute(insert_query, values)
db.commit()

# Api Setup  
app = Flask(__name__, static_url_path='/static')
@app.route('/',methods=['GET'])
def hello():
     # Fetch data from the database
    query = "SELECT title, image, link FROM news1"
    cursor.execute(query)
    news_data = cursor.fetchall()



    # Close the database connection and browser
    cursor.close()
    db.close()
    print(news_data)
    
     

    # Render the HTML template with the data
    return render_template('index.html', news_data=news_data)
    
   
    
if __name__ == '__main__':
    app.run()