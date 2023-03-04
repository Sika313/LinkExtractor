from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
from openpyxl import Workbook

print('_'*10)
print('\n \n')

print('E.g http://example.com/')
url = input('Enter url:')

print('_'*10)
print('\n \n')
print('E.g demo.xlsx')

name = input('Type name of excel sheet:')
wb = Workbook()
sheet = wb.active
holder = []

def getLinks(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        bs = BeautifulSoup(html, 'html.parser')
        if ( bs.find_all('a', href=re.compile('^(http|https)')) == []):
            print('No links found on this url.')
        else:
            for link in bs.find_all('a', href=re.compile('^(http|https)')):
                sheet.append([link.attrs['href']])
            wb.save(name)

getLinks(url)

'''
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
print(bs.find_all('a', href=re.compile('^(http|https)')))
'''
