from selenium import webdriver
import csv
from bs4 import BeautifulSoup

# Set the URL to scrape
url = "https://www.freecodecamp.org/news/"

# Use Chrome to open the website
driver = webdriver.Chrome(executable_path='C:/Users/munam/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(url)

# Get the HTML of the website
html = driver.page_source

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the title element and store it in a variable
title = soup.find_all(class_="post-card-title")

# Find the publication date element and store it in a variable
date = soup.find_all(class_="data-test-label")

# Store the data in a dictionary
data = {"title": "", "date": ""}

for t in title:
    data["title"] += t.text

for d in date:
    data["date"] += d.text

# Write the data to a CSV file
with open("webscps.csv", "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["title", "date"])
    writer.writeheader()
    writer.writerow(data)

# Close the web driver
driver.quit()
