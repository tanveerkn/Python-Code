import requests

from bs4 import BeautifulSoup

def paper_spider(max_page):
    page=1
    while page <= max_page:
        url = 'https://scholar.google.com.pk/scholar?hl=en&as_sdt=0%2C5&q=garbled+circuit&btnG=' + str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html5lib")
        for h3 in soup.findAll('h3', {'class':'gs_rt'}):
            link = h3.findAll('a')[0]
            href = link.get('href')
            data_clk=link.get('data-clk')
            title = link.string
            # print(link.text)
            # print(href)
            # print(data_clk)
            # print(title)

            single_page_search(href)
        page += 1
#
def single_page_search(item_url):   # dyanmic web crawler
    print(item_url)
    if 'springer' in item_url and 'pdf' not in item_url:
        source_code = requests.get(item_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html5lib")
        print(soup)
        # for item_name in soup.findAll('h1',{"class":"ChapterTitle"}):
            # print(item_name.text)
            # print(item_name.string)
    # else:
    #     print("none")


paper_spider(1)

