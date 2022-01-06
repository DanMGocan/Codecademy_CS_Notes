import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

# This will return the first <div> tag found in the HTML string #
print(soup.div)

# Will return the name of the tag #
print(soup.div.name)

# Will return a dictionary with the attributes of the tag #
print(soup.div.attrs)

# Will return the content of the string inside #
print(soup.div.string)

# Will print out all the children / parents of an HTML tag #
print(soup.div.parents)
print(soup.div.children)

# Will print as a list, all the h1 tags in the HTML object # 
print(soup.find_all("h1"))

# Using regular expressions to return a list of all h1-h9 tags #
import re
soup.find_all(re.compile("h[1-9]"))

# Will return all the tags from the supplied list #
soup.find_all(['h1', 'a', 'p'])

# Passing a dictionary as a search parameter
soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})

# Using a function as a search parameter #
def has_banner_class_and_hello_world(tag):
    return tag.attr('class') == "banner" and tag.string == "Hello world"
 
soup.find_all(has_banner_class_and_hello_world)
