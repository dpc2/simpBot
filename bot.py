from mastodon import Mastodon
import urllib.request
from bs4 import BeautifulSoup
import re
import webbrowser


#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space/'
)


class Scraper:

    # __init__ method takes a url to scrape as
    # a parameter.
    def __init__(self, site):
        self.site = site
        self.flag = False

    def scrape(self):
        while self.flag == False:
        # urlopen() makes a request and returns
        # a Response object. read() is used to
        # return the HTML from the Return object.
            r = urllib.request.urlopen(self.site)
            html = r.read()

            parser = 'html.parser'
            sp = BeautifulSoup(html, parser)

        # find_all returns an interable containing
        # the tag objects it found
            for tag in sp.find_all('img'):
                # We get the 'href' tags by calling
                # the get method and passing 'href'
                #url = tag.get('img')
                #if url is None:
                    #continue
                if 'src="https://i.redd.it/' in str(tag):
                    output = tag
                    return tag
                    flag = True


simps = 'https://www.reddit.com/r/simpsonsshitposting/'
scrapedTag = Scraper(simps).scrape()

myRegex = re.search("src=[\"\']([a-zA-Z0-9_\.\/\-:]+)[\"\']", str(scrapedTag))
imageLink = myRegex.group()

imageLink = imageLink[5:-1]
print(imageLink)

webbrowser.open(imageLink)

#mastodon.status_post("hello world!")
