#!/usr/bin/python3
# kindleSearch.py - Opens top free book links.

import requests
import sys
import webbrowser
import bs4

print('Searching Kindle Store for currently Free Books...')
# Headers to send with HTML Request so Amazon thinsk we're a people.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}
# Take any arguments in the command line as a single search term variable
searchTerm = ''.join(sys.argv[1:])
# Request search website with the keywords punched in and the headers sent.
res = requests.get('https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Ddigital-text&field-keywords=free+kindle+books+' +
                   searchTerm + '&rh=n%3A133140011%2Ck%3Afree+kindle+books+' + searchTerm + '&ajr=0', headers=headers)
res.raise_for_status()

# Save the parsed webpage as a variable so we can go through it.
soup = bs4.BeautifulSoup(res.text, "html.parser")
books = soup.find_all('a', class_="s-access-detail-page")
numOpen = min(5, len(books))
# Any link with the defined class should be found on the entirety of the page
for i in range(numOpen):
    webbrowser.open(books[i].get('href'))
