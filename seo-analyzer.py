import requests
from bs4 import BeautifulSoup
import time

'''
1. Title and description checker
'''

url = input("Enter the URL of the web page: ")
# Make a request to the URL


response = requests.get(url)
# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# Find the meta title tag and get its content
meta_title = soup.find('meta', {'name': 'title'})
if meta_title:
    print('Meta title found: ' + meta_title['content'])
else:
    print('No meta title found')
# Find the meta description tag and get its content
meta_description = soup.find('meta', {'name': 'description'})
if meta_description:
    print('Meta description found: ' + meta_description['content'])
else:
    print('No meta description found')



'''
2. Schema scraper
'''

html_content = response.text
# Use beautifulsoup4 to parse the HTML content and find the schema information
soup = BeautifulSoup(html_content, 'html.parser')

schema_tags = soup.find_all('script', attrs={'type': 'application/ld+json'})
# Print the schema information for each tag found
for schema_tag in schema_tags:
    schema_data = schema_tag.string.strip()
    print(schema_tags)
    print(schema_data)


'''
3. Page speed checker
'''

#def check_page_speed():

# Prompt user to enter the URL to check

# Send a GET request to the given URL and record the start time
start_time = time.time()
response = requests.get(url)
# Record the end time and calculate the page load time
end_time = time.time()
page_load_time = end_time - start_time
# Print the page load time in seconds
print(f"Page load time: {page_load_time:.2f} seconds")
# Example usage:


#check_page_speed()



'''
4. Image alt checker
'''

import requests
from bs4 import BeautifulSoup
# Function to check if an image has an "alt" attribute
def has_alt_attribute(img):
    return "alt" in img.attrs
# Get the URL from the user
#url = input("Enter the URL of the page to check: ")
# Make a request to the URL and get the HTML content
#response = requests.get(url)
html_content = response.content
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
# Find all the image tags on the page
images = soup.find_all('img')
# Check if each image has an "alt" attribute or not
for image in images:
    if has_alt_attribute(image):
        #print(has_alt_attribute(image))
        #print(str(image))
        #print(type(image))
        print(len(str(image['alt'])))


        if 'src' in str(image):
            if len(str(image['alt']))>0:
                #print(f"The image with source '{image['src']}' has an 'alt' attribute.")
                #print('---')
                pass


            elif len(str(image['alt']))==0:
                print(f"The image with source '{image['src']}' does not have an 'alt' attribute.")
