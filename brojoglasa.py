import requests
from lxml import html
import time

# Prompt the user to enter the URL
url = input("Please enter the URL: ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a GET request to the webpage
response = requests.get(url, headers=headers)
response.raise_for_status()
time.sleep(2)

# Parse the content of the webpage
tree = html.fromstring(response.content)

# Define the XPath expression to extract the titles of the articles
# This XPath expression will vary depending on the structure of the webpage
xpath_expression = '//*[@id="__layout"]/div/div[1]/div/div[2]/div/div[2]/div/h1/b/text()'

# Use the XPath expression to extract the data
titles = tree.xpath(xpath_expression)

# Print the extracted titles
for title in titles:
    print(title)
