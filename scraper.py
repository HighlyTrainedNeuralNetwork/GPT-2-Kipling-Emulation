import requests
from bs4 import BeautifulSoup
url = "http://www.poetryloverspage.com/poets/kipling/kipling_ind.html"
page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")
links = ["https://www.poetryloverspage.com/poets/kipling/" + link["href"] for link in soup.find_all(href=True)][23:548]

with open("Training Input.txt", "w", encoding="UTF-8") as file:
    for link in links:
        try:
            page = requests.get(link)
            page.encoding = "UTF-8"
            soup = BeautifulSoup(page.text, "html.parser")
            poem = soup.find("pre").text
            title = soup.find(id="h1_poem_title").text
            file.write(title + "\n")
            file.write(poem)
            file.write("<|endoftext|>" + "\n")
        except:
            pass
