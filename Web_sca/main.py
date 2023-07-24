import requests
from bs4 import BeautifulSoup 
import time
def timer(function):
    def tim(*args):    
        start=time.time()
        function(*args)
        end=time.time()
        duration=end-start
        print(f'Execution time is: {duration} Seconds')
    return tim
    
@timer
def downer(site,write_path):
    try:
        source=requests.get(site)
        source.raise_for_status()
        with open(write_path,'w',encoding='utf-8') as write_file:
            write_file.write(source.text)
        
        print(f'saved to {write_path} as {write_path}')
        print('Executed withour Error')
    except requests.exceptions.RequestException as error:
        print(f'Error: {error}')

downer('https://en.wikipedia.org/wiki/Gun','jupyter\Web_sca\output.html')

@timer
def finder(read_path,write_path,to_find):
    with open(read_path,'r',encoding='utf-8') as read_file:
        content=read_file.read()
    with open(write_path,'w',encoding='utf-8') as write_file:
        write_file.write(str(BeautifulSoup(content,'lxml').find_all(to_find)))
    print('Executed withour Error') 

finder('jupyter\Web_sca\output.html',r'jupyter\Web_sca\found.html','ul')