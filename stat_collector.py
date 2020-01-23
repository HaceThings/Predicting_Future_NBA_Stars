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

players = {}

stats = ['player', 'rank', 'draft_year', 'round', 'pick_overall']

# Take out the <div> of name and get its value
table = page_soup.find_all(name="table")
table_body = table[0].find_all("tbody")
table_rows = table_body[0].find_all("tr")

for row in table_rows:
    # TODO: How do I want to structure my data? Nested dictionaries? Nested lists? Definitely use pandas once it is collected.
    for stat in stats:
        a[stat] = (row.find("td", {"data-stat": stat}))
    # Strips the leading and trailing characters
    name = name.text.strip().encode()

    # Decodes the string using the codec registered for encoding
    name = name.decode("utf-8")

    # Parse for (college)
    if "(college)" in text:
        length = len(text)
        text = text[0:length-9]
        print(text)
    players[]