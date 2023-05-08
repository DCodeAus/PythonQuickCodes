#first part of this script is to install the python requeusts library, insert the line below in powershell (you need to ensure you have admin settings)
#python -m pip install requests

import requests
#this imports the package requests
#to use beautiful soup you will need to install another package
#python -mpip install beautifulsoup4
#this package is a library for passing structured data
from bs4 import BeautifulSoup

#pointing at a fake site for this test script
URL="https://realpython.github.io/fake-jobs/"
#uses the HTTP get request from the URL stated above, retreives the data and stores it in a python object
page = requests.get(URL)
#takes page.content, and creates a beautiful soup object as its input.
soup = BeautifulSoup(page.content, "html.parser")
#finds the specific html element by its ID, in this case Results Container
results = soup.find(id="ResultsContainer")
#searching the above results, for card content
job_elements=results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element=job_element.find("h2",class_="title")
    company_element=job_element.find("h3",class_="company")
    location_element=job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print ()
    #print(job_element, end= "\n"*2)
#prints the text
#print(results.prettify())