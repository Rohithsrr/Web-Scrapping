from bs4 import BeautifulSoup
import requests
from selenium import webdriver

url = "https://github.com/Rohithsrr/Billing-Software"

# Check if the request was successful
source = requests.get(url)
if source.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

def get_chrome_web_driver(options):
    return webdriver.Chrome("./chromedriver", options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')

# BeautifulSoup is used for getting HTML structure from requests response (create your soup)
soup = BeautifulSoup(source.text, 'html.parser')  # Corrected parser

# Find function is used to find a single element if there are more than once it always returns the first element.
title = soup.find('title')  # place your html tag in parentheses that you want to find from html.
print("this is with html tags :", title)

qwery = soup.find('h1')  # here I find first h1 tag in my website using find operation.

# use .text for extract only text without any html tags
print("this is without html tags:", qwery.text)

links = soup.find('a')  # I extracted link using "a" tag
print(links)

# Extract href data from anchor tag
print(links['href'])

# Extracting href(links) attribute and anchor(<a>) tag from page
for a in soup.find_all('a', href=True):
    print(a['href'])

for i in links:
    print(i.text)

# Similarly I got class details from a anchor tag
print(links['class'])

# Find all operation in Bs4
# find_all function is used to fetch all tags at a single time.
many_link = soup.find_all('a')  # here I extracted all the anchor tags of my website
total_links = len(many_link)  # len function is used to calculate length of your array
print("total links in my website :", total_links)
print()
for i in many_link[:6]:  # here I use slicing to fetch only first 6 links from rest of them.
    print(i)

second_link = many_link[1]  # here I fetch second link which place on 1 index number in many_links.
print(second_link)
print()
print("href is :", second_link['href'])  # only href link is extracted from anchor tag

# Select div tag from second link
nested_div = second_link.find('div')

# Check if nested_div is not None before accessing its attributes
if nested_div is not None:
    # As you can see div element extracted, it also has inner elements
    print(nested_div)
    print()
    # Here I extracted class element from div but it gives us in the form of list
    z = nested_div['class']
    print(z)
    print(type(z))
    print()
    # " ".join() method use to convert list type into string type
    print("class name of div is :", " ".join(nested_div['class']))
else:
    print("No <div> found in the second link.")

# Scrap data from Wikipedia
wiki = requests.get("https://en.wikipedia.org/wiki/World_War_II")
soup = BeautifulSoup(wiki.text, 'html.parser')  # Corrected parser
print(soup.find('title'))

# Find html tags with classes
ww2_contents = soup.find_all("div", class_='toc')
for i in ww2_contents:
    print(i.text)

overview = soup.find_all('table', class_='infobox vevent')
for z in overview:
    print(z.text)

images = soup.find_all('img')

# Print images
print(images)