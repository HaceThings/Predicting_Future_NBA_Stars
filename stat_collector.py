from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

# specify the url
quote_page = 'https://www.basketball-reference.com/awards/recruit_rankings_2017.html'

# query the website and return the html to the variable ‘page’
page = uReq(quote_page)

# parse the html using beautiful soup and store in variable `soup`
page_soup = soup(page.read(), 'html.parser')
page.close()

stats = ['player', 'draft_year', 'round', 'pick_overall']

# Take out the <div> of name and get its value
table = page_soup.find_all(name="table")
table_body = table[0].find_all("tbody")
table_rows = table_body[0].find_all("tr")
for row in table:
    cell = table[0].find("td", {"data-stat": stats})
    name = name.text.strip().encode()
    name = name.decode("utf-8")

players = table_body.findAll("tr", {"data-stat", "player"})