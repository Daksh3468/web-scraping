import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector
from flask import Flask, render_template


def sandeshnews():
    # Set up Selenium webdriver
    driver = webdriver.Chrome()  # Replace with the path to your Chrome webdriver if needed
    url = "https://sandesh.com/sports"
    driver.get(url)
    time.sleep(2)  # Give the page some time to load
    # Scrape data and insert into the database
    news_elements = driver.find_elements(By.XPATH, '//div[@class="col-lg-6 col-xl-4"]')

    

    # for news_element in news_elements:
    news_element=news_elements[0]
    title_element = news_element.find_element(By.XPATH, './/a[@class="story"]')
    link = title_element.get_attribute('href')
    

    img_element = news_element.find_element(By.XPATH, './/a[@class="story"]/div[@class="caption mb-0"]/img')
    image = img_element.get_attribute('src')
   

    title = news_element.find_element(By.XPATH, './/a[@class="story"]/div[@class="categoty-padding"]/p[@class="ellipsis"]').text

    data={}
    data['title']=title
    data['img_src']=image
    data['link']=link

    return data



# # Insert data into the database
# insert_query = "INSERT INTO news1 (title, image, link) VALUES (%s, %s, %s)"
# values = (title, image, link)
# cursor.execute(insert_query, values)
# db.commit()



# # Connect to MySQL database
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     port='3306',
#     password="",
#     database="tempdb"
# )
# cursor = db.cursor()

# # Create table
# create_table_query = """
#     CREATE TABLE IF NOT EXISTS news1 (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         title VARCHAR(255),
#         image VARCHAR(255),
#         link VARCHAR(255)
#     )
# """
# cursor.execute(create_table_query)


# # Create Flask app
# app = Flask(__name__)

# @app.route('/')
# def index():

#     # Fetch data from the database
#     query = "SELECT title, image, link FROM news1"
#     cursor.execute(query)
#     news_data = cursor.fetchall()

#     # Close the database connection and browser
#     cursor.close()
#     db.close()
#     driver.quit()

#     # Render the HTML template with the data
#     return render_template('news.html', news_data=news_data)


# if __name__ == '__main__':
#     app.run()

