from urllib import FancyURLopener
import json
from bs4 import SoupStrainer, BeautifulSoup
import time


#Class to provide custom user header to prevent
#blocking by Google\'s bot watchers.
class MyOpener(FancyURLopener):
  version = 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
openurl = MyOpener().open

data = [] # Empty list used later to create json


nr = 0
base_url = 'http://www.tate.org.uk/search?type=artwork'
#iterate through 8 pages
for i in range(1,201):
    #save progress every 10 pages in case it gets stuck somewhere
    if i%10 == 0:
        with open('databaseArt.json', 'w') as outfile:
            json.dump(data,outfile,sort_keys = True, indent = 2)
        print '~~~~~~~~~~~~~~~~~~saved~~~~~~~~~~~~~~~~~~~~~~'
    #create page url
    page_number = i
    append_url = '&page='+str(page_number)
    print append_url
    page_url = base_url+append_url
    print page_url
    menu = BeautifulSoup(openurl(page_url).read(), "lxml")
    #iterate through hackathons in the page
    for piece in menu.find_all('',{'class':'card-media__inner responsive-container'}):
      #get description
      found = False
      info = {}
      piece_url = 'http://www.tate.org.uk'+ piece.find('a')['href']
      print piece_url
      page = BeautifulSoup(openurl(piece_url).read(), "lxml")
      for item in page.find_all('div',{'class':'tab-section__content'}):
          if item.previousSibling.previousSibling.text.strip() == 'Display caption':
              found = True
              if item.find('p').text.strip() != '':
                  info['description'] = item.find('p').text.strip()

      #get tags
      tags_list=[]
      page = BeautifulSoup(openurl(piece_url).read(), "lxml",parse_only=SoupStrainer('div',{'class':'list-wrapper content-block--columns'}))
      if page:
          for a in page.find_all('a'):
              tags_list.append(a.text.strip())
          if tags_list:
              info['tags'] = tags_list

          if info and found == True:
              nr += 1
              data.append(info)
              print nr


with open('databaseArt.json', 'w') as outfile:
  json.dump(data,outfile,sort_keys = True, indent = 2)
print nr
