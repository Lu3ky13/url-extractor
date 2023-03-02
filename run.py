import requests
from bs4 import BeautifulSoup

# Set the URL of the web page to scrape
url = "https://hackerone.com"

# Make a request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all links in the page
links = soup.find_all("a")

# Create a list to store all links
all_links = []

# Loop through each link in the page
for link in links:
    href = link.get("href")
    if href is not None and href not in all_links:
        all_links.append(href)

# Loop through each link in the list and extract all links in the response
for link in all_links:
    try:
        response = requests.get(link)
        soup = BeautifulSoup(open(html_path, 'r'),"html.parser",from_encoding="iso-8859-1")
        links = soup.find_all("a")
        for l in links:
            href = l.get("href")
            if href is not None and href not in all_links:
                all_links.append(href)
    except:
        pass

# Save the list of all links to a file
with open("output.txt", "w", encoding="utf-8") as file:
    for link in all_links:
        file.write(link + "\n")
