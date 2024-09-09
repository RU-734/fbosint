from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os

def download_images_from_facebook(url):
    # Start a Selenium WebDriver
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get(url)
    
    # Get the page content
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Find image tags
    images = soup.find_all('img')
    
    # Download images
    os.makedirs('fb_images', exist_ok=True)
    for idx, img in enumerate(images):
        img_url = img['src']
        img_data = requests.get(img_url).content
        with open(f'fb_images/image_{idx}.jpg', 'wb') as handler:
            handler.write(img_data)
            print(f"Downloaded image_{idx}.jpg")

    driver.quit()

# Replace 'your_facebook_post_url' with the URL of the Facebook post you want to scrape.
download_images_from_facebook('your_facebook_post_url')
