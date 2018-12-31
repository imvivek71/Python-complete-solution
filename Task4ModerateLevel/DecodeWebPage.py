import requests
from bs4 import BeautifulSoup
base_url = input("Enter the url to be decoded in this format - binplus.in")
url = "http://"+base_url
class_name = input("Input the class")
count=0
r = requests.get(url)
soup = BeautifulSoup('features="html.parser"',r.text)
for class_name in soup.find_all(class_="class_name"):
    if class_name.a:
        print(class_name.a.text.replace("\n", " ").strip())
    else:
        print(class_name.contents[0].strip())
for class_name in soup:
    count= count+1
print("Total no. of occurance {}".format(count))
