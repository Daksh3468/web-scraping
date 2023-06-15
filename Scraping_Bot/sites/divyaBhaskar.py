import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def divyabhaskar():
    # Set up Selenium webdriver
    driver = webdriver.Chrome() 
    url = "https://www.divyabhaskar.co.in/sports/"
    driver.get(url)
    time.sleep(2)  # Give the page some time to load



    # Scrape data and insert into the database
    news_elements = driver.find_elements(By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[2]/div/div[2]/ul/div')

    print(len(news_elements))

    news_element=news_elements[0]
    # print(news_element)
    title = news_element.find_element(By.XPATH, './/div[2]/li/a/div').get_attribute('title')
    link = news_element.find_element(By.XPATH, './/div[@class="efb7defa"]/li/a').get_attribute('href')
    # print("Link =", link)

    img_element = news_element.find_element(By.XPATH, './/div[@class="efb7defa"]/li/a/div/figure/picture/img')
    image = img_element.get_attribute('src')
    # print("Image Link =", image)

    # title = title.text
    # print("Title =", title)


    # Create a dictionary to store the data
    news_data = {
        'title': title,
        'image': image,
        'link': link
    }

    driver.quit()
    return news_data
