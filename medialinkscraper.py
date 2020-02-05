import requests, time
from bs4 import BeautifulSoup

try:
    pages = input("Enter page limit: ")
except KeyboardInterrupt:
    sys.exit()

urls=[]
urls.append("http://itdmusic.in/")
output=[]

#url="http://itdmusic.in/"
#url="http://itdmusic.in/page/" + str(2)

i=2
while (i<int(pages)+1):
    url="http://itdmusic.in/page/" + str(i)
    urls.append(url)
    i+=1
i=1    
for url in urls:
    
    result=requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    album_list = soup.find("div", class_="post-listing")
    articles = album_list.find_all("article")
    for article in articles:
        #article[0].find("a")["href"]
        title=article.find("a").text
        link=article.find("a")["href"]
        spacer="---------------------------------------------------------------------------------------------------"
        print(title)
        print(link)
        print(spacer)
        output.append(title)
        output.append(link)
        output.append(spacer)
    print(i)
    i+=1
    time.sleep(1)

with open('metadata.txt', 'w', encoding='utf-8') as f:
    for line in output:
        f.write("%s\n" % line)
print("Done")

