from bs4 import BeautifulSoup #Beautiful Soup 4 (bs4) is a Python library for parsing HTML and XML documents. It allows you to extract data from web pages by navigating the document’s structure
import requests #Requests library in Python provides a simple API for interacting with HTTP operations such as GET, POST, and more. 
import time #helps you work with time related operations with python

def function():
    #get access to the html document of the website using GET method in requests
    html_text = requests.get('Webpage URL').text #remember to put the '.text' part or this won't work since Beautiful soup expects a string format....You obtain a response object when using get methos with the URL..
    soup = BeautifulSoup(html_text, 'lxml') #This is where you define the content you are going to parse and the html parsing technique that you are going to use.
    tag_List = soup.find_all('HTML tag', 'attribute to distinguish')#This return the div tags with the relevant class as a list
    
    for tag in tag_List: #iterate through the list of apprentiships
        variable1 = tag_List.find('HTML tag', 'attribute to distinguish').text #This is the annoying bit since you have to through the html to get the piece of info that you need
        variable2 = tag_List.find('HTML tag', 'attribute to distinguish').text
        variable3 = tag_List.find('HTML tag', 'attribute to distinguish').text #'.text' seperates the text from the html tags and returns them
        Link = tag_List.a['href'] #'href' in square brackets return the value of the attribute href of tag <a>
        with open('Scrape_data.txt', 'a') as records: #This is the whole process of writing the relevant info to the Text file. 'a' appends data to the file without overwriting it each time the loop runs.
            records.write(f"ITEM....")
            records.write(f"Value: {variable1}")
            records.write(f"Value:{variable2} \n")
            records.write(f"Value:{variable3} \n")
            records.write(f"Link:{Link} \n")
            records.write(f"--------------------------------\n")

            print("Scraped item!!")
        
            


if __name__ == "__main__":
    while True:
        function()
        print("Waiting 1 day")
        time.sleep(86400)



        



