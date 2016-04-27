
"""****************Technopark Job Search Crawler************
The requirements for the program to work is that you have python(3.5.1)
installed. You will have to import BeautifulSoup and re modules. You can type
"pip install bs4" and "pip install re" respectively in the command prompt and
python would automatically download them.

The jobs are posted in a doc format on the desktop. 

The crawler parses Job Title, Company Name and the job link.
Any questions, you can email me at sharpeyekool@gmail.com
--------------------------------------------------------------------------------------------------------
Created by Roni Rengit"""

#!/usr/local/bin/python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os

#Console
print("Webcrawler for www.technopark.org job site")

#Check for OS support
import sys
if(sys.platform=='win32'):
  print("Windows platform 32 bit\n")
elif(sys.platform=='win64'):
  print("Windows platform 64 bit\n")
else:
  print("Sorry, I have not checked the program for non-Windows systems\n")

#Open file
option =input("Ths site has been scrapped.The file will be saved with a default name in the current directory. Do you want to change it? ('Y' or 'N'): ")

if (option=='Y') or (option=='y'):
  file_location=input("Enter URL: ")
  filename=input("File Name: ")
else:
  file_location=os.getcwd()
  filename="TP Joblisting"

try:
  file=open(file_location+"\\"+filename+'.doc', 'w', encoding='utf-8')
except:
  print("Please close the document and try again")
  input("")
  
#Parsing function
def parser(soup_html):
    JobTitle=soup.tbody.findAll("a", {"class":"jobTitleLink"})
    JobLink=soup.tbody.findAll("a", {"href":re.compile("job-detail")})
    CompanyName=soup.tbody.findAll("a",{"href":re.compile("/company-details")})
    
    #initializing lists 
    jobslist=[]
    companieslist=[]
    linkslist=[]

    for jobs in JobTitle:
      jobslist.append(str(jobs.get_text()))
      
    for companies in CompanyName:
      companieslist.append(str(companies.get_text()))

    for links in JobLink:
      linkslist.append(links.get('href'))

      
    for  i in range(len(jobslist)):

      #Uncomment below to see job postings on console
      """print('Job Title:'+jobslist[i])
      print('Company Name: '+companieslist[i])
      print("Links: "+r"http://www.technopark.org/job-search"+linkslist[i]+"\n")"""
      
      file.write("Job Title: "+jobslist[i]+"\n") 
      file.write("Company Name: "+companieslist[i]+"\n")
      file.write(r"http://www.technopark.org/"+linkslist[i]+"\n")
      file.write("\n")
    print("Done. Please check "+file_location+"\\"+filename+'.doc')
    print("Thank you")
    file.close()
      
#Checks for any errors due to site issues such as web page not found or server issues, etc
try:
  URL=r"http://www.technopark.org/job-search"
  URL_test=r"File:\C:\Users\ferdinand-pc\Desktop\technopark.html"
  html=urlopen(URL)
  status="Successful"
except:
  print("Could not open website. Check for connectivity issues.\n")
  status='error'

#if site is read then html is passed on to BeautifulSoup for processing
if(status=='Successful'):
  soup=BeautifulSoup(html, "html.parser")
  parser(soup)
else:
  print("Try again")
  
input("")