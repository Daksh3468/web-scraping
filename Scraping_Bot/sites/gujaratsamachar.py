# This file contains all methods regarding gujaratsamachar
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi



# import os
# from dotenv import load_dotenv,dotenv_values

# load_dotenv()
# username=os.getenv("USERNAME")
# password=os.getenv("PASSWORD")

# dburl = f"mongodb+srv://{username}:{password}@cluster0.eze3gip.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(dburl, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
#     db= client.get_database('News-Catcher')
#     records=db.gujaratsamachars

# except Exception as e:
#     print(e)
data= {}
class GujaratSamachar(webdriver.Chrome):
    def __init__(self, keeprunning):
        # Blocking Notifications
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-notifications")
        self.chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})

        # Setting up drivers
        self.service = Service("./drivers/chromedriver")
        super().__init__(service=self.service,options=self.chrome_options)

        # To keep it running
        self.keeprunning = keeprunning

        # Waiting time for each element
        self.implicitly_wait(5)

        self.maximize_window()  # Maximizes Window
        

    # Exit setup after main ends
    def __exit__(self, exc_type, exc_val, exc_tb):
        while self.keeprunning:
            pass
    
    def landing_page(self):
        self.get('https://www.gujaratsamachar.com/category/sports/1')

    def news_title(self):
        time.sleep(5)
        self.parent_container= self.find_elements(By.CLASS_NAME,'col-12')
        title= self.parent_container[0].find_element(By.CSS_SELECTOR,'a[data-toggle="tooltip"]')

        data["title"]=title.get_attribute('title').strip()
    
    def img(self):
        title= self.parent_container[0].find_element(By.CSS_SELECTOR,'a[data-toggle="tooltip"]').get_attribute('title').strip()
        picture= self.parent_container[0].find_element(By.TAG_NAME,'picture')
        img= picture.find_element(By.CSS_SELECTOR,f'img[alt="{title}"]')
        
        data["img_src"]=img.get_attribute('src')

    def date_and_time(self):
        container= self.parent_container[0].find_element(By.CLASS_NAME,'news-box')
        container2= container.find_element(By.CLASS_NAME,'d-flex')
        container3= container2.find_element(By.TAG_NAME,'div')
        date=container3.find_element(By.TAG_NAME,'span')
        
        data["date_and_time"]=date.text.strip()


    def article(self):
        title=self.parent_container[0].find_element(By.CSS_SELECTOR,'a[data-toggle="tooltip"]')
        link=title.get_attribute('href')
        data['link']=link
        self.quit()
        return data
        






            
            
    



        
        

    