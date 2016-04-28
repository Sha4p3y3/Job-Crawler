# -*- coding: utf8 -*-

"""****************Technopark Job Search Crawler************
The requirements for the program to work is that you have python(3.5.1)
installed. You will have to import BeautifulSoup and re modules. You can type
"pip install bs4" respectively in the command prompt and
python would automatically download/install them.

The jobs are posted in a doc format on the desktop.

The crawler parses Job Title, Company Name and the job link.
Any questions, you can email me at sharpeyekool@gmail.com
-------------------------------------------------------------------------------
Created by Roni Rengit"""

from bs4 import BeautifulSoup
import re
from os import path, getcwd
from sys import platform, version_info, exit

# compatible import urlopen in both python3 and python2
try:
    from urllib.request import urlopen
except ImportError:
    try:
        from urllib import urlopen
    except Exception, e:
        raise e

# Console
print("Webcrawler for www.technopark.org job site")

"""# Check for OS support
if(sys.platform == 'win32'):
    print("Windows platform 32 bit\n")
elif(sys.platform == 'win64'):
    print("Windows platform 64 bit\n")
else:
    print("Sorry, I have not checked the program for non-Windows systems\n")
"""


# compatible input function
def minput(notice=""):
    if version_info.major == 2:
        return raw_input(notice)
    elif version_info.major == 3:
        return input(notice)

# Open file
option = minput(
    "Ths site has been scrapped.The file will be saved with a default name in the current directory.\nDo you want to change it? ('Y' or 'N'): ")

if (option in ["Y", 'y']):
    file_location = minput("Enter URL: ")
    filename = minput("File Name: ")
else:
    file_location = getcwd()
    filename = "TP Joblisting"

filename = path.join(file_location, filename + '.doc')

try:
    with open(filename, 'w') as file:
        pass

except Exception as e:
    print e
    print("Please close the document and try again")
    minput("")


# Parsing function
def parser(soup):
    JobTitle = soup.tbody.findAll("a", {"class": "jobTitleLink"})
    JobLink = soup.tbody.findAll("a", {"href": re.compile("job-detail")})
    CompanyName = soup.tbody.findAll(
        "a", {"href": re.compile("/company-details")})

    # initializing lists
    jobslist = []
    companieslist = []
    linkslist = []

    for jobs in JobTitle:
        jobslist.append(jobs.get_text().encode("utf-8"))

    for companies in CompanyName:
        companieslist.append(str(companies.get_text()))

    for links in JobLink:
        linkslist.append(str(links.get('href')))

    with open(filename, 'w') as file:
        for i in range(len(jobslist)):
            # Uncomment below to see job postings on console
            # print('Job Title:'+jobslist[i])
            # print('Company Name: '+companieslist[i])
            # print("Links:
            # "+r"http://www.technopark.org/job-search"+linkslist[i]+"\n")

            file.write("Job Title: " + jobslist[i] + "\n")
            file.write("Company Name: " + companieslist[i] + "\n")
            file.write(r"http://www.technopark.org/" + linkslist[i] + "\n")
            file.write("\n")
        print("Done. Please check " + filename)
        print("Thank you")

# Checks for any errors due to site issues such as web page not found or
# server issues, etc
try:
    URL = r"http://www.technopark.org/job-search"
    URL_test = path.join(file_location, "technopark.html")
    resp = urlopen(URL)

    # if site is read then html is passed on to BeautifulSoup for processing
    if resp.code == 200:
        html = resp.read()
        html = html.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        parser(soup)
    else:
        print("Try again")
except Exception as e:
    print e

minput("")
