import requests
from bs4 import BeautifulSoup
import time
import colorama
from colorama import Fore, Back
colorama.init()

class Parcer:
    def __init__(self):
        self.url = "none"
        self.element = ""
        self.cls = ""
        self.speed = 0.2
    
    def find_text(self):
   
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text,'lxml')
        dates = soup.find_all(self.element, self.cls)
        
        str_result = ""
        for date in dates:
            
            str_result += str(date) + "\n"
        
        return str_result

    def find_clear(self):
   
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text,'lxml')
        dates = soup.find_all(self.element, self.cls)
        
        str_result = ""
        for date in dates:
            
            str_result += date.text + "\n"
        
        return str_result

    def show_links(self):

        res = requests.get(self.url)
        soup = BeautifulSoup(res.text,'lxml')
        dates = soup.find_all(self.element,self.cls)
        str_result = ""
        for link in dates:
            str_result += str(link.get('href')) + "\n"
        
        return str_result
 

