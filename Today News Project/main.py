import requests
from bs4 import BeautifulSoup

# Gather information
bbc_list =[ "https://www.bbc.com/news/technology"]
exp_list = ["https://www.expressen.se/"]
# Request information from website


# Check request error
# -----

# Parse the request using BeautifulSoup
class BBC:
    def __init__(self) -> None:
        # class tags
        self.c_tag_article = "e1xue1i86"
        self.c_tag_title = "ssrcss-15xko80-StyledHeading"

    def find_article_category(self, soup):
        tag = "gs-o-list-ui__item--flush gel-long-primer gs-u-display-block gs-u-float-left nw-c-nav__wide-menuitem-container"
        li_tag = soup.find(class_=tag)
        print(li_tag.text)

    def find_article_title(self, soup):
        title = soup.find(class_=self.c_tag_title)
        print("\n**********" + title.text + "**********\n")

    def find_article_text(self, soup):
        
        text_components = soup.find_all(class_=self.c_tag_article)
        print("The Title of this ")
        for text_component in text_components:
            paragraph = text_component.find("p")
            if paragraph:
                print(paragraph.text + "\n")

    def find_article_information(self, url_):
        r = requests.get(url_)
        soup = BeautifulSoup(r.text, "html.parser")
        self.find_article_category(soup)
        # self.find_article_title(soup)
        # self.find_article_text(soup)

class Exp:
    def __init__(self) -> None:
        # class tags
        self.c_tag_title = "teaser"
        

    def find_article_title(self, soup, url_):
        all_articles = soup.find_all(class_=self.c_tag_title)
        for article in all_articles:
            a_tag = article.find("a")
            title = a_tag.find("h2")
            print("\n**********" + title.text + "**********\n" + url_ + a_tag["href"])
            if input("continue?").strip().lower() == "no":
                break

    def find_article_text(self, soup):
        
        text_components = soup.find_all(class_=self.c_tag_article)
        print("The Title of this ")
        for text_component in text_components:
            paragraph = text_component.find("p")
            if paragraph:
                print(paragraph.text + "\n")
        
    def find_article_information(self, url_):
        r = requests.get(url_)
        soup = BeautifulSoup(r.text, "html.parser")
        # self.find_article_title(soup, url_)
        #self.find_article_text(soup)


if __name__ == "__main__":

    bbc_news = BBC()
    exp_news = Exp()
    for url in bbc_list:
        bbc_news.find_article_information(url)