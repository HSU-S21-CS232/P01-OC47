from urllib.request import urlopen   
from bs4 import BeautifulSoup

url_to_scrape =  "https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/" 

request_page = urlopen(url_to_scrape) #requesting the page
page_html = request_page.read()       #read the request
request_page.close()     #closing the request for us
soup_data = BeautifulSoup(page_html, 'html.parser')
soup_data.title.text
movies = soup_data.find_all('div',{'class':'col-sm-18 col-full-xs countdown-item-content'} )
first_movie = movies[0]
first_movie.find('div', {"class":"countdown-index"}).text #rank
first_movie.h2.a.text #Name of the movie
first_movie.find('span', {"class":"subtle start-year"}).text[1:5] #year
first_movie.find('span', {"class":"tMeterScore"}).text #tmeter
movie_data = []
filename = 'help.csv' #passing it to a csv
f = open(filename, 'w') #open filename with rate permission
headers = 'Rank, Name, Year, tmeta, link \n'
f.write(headers)
for shows in movies:
    Rank = shows.find('div', {"class":"countdown-index"}).text
    Name = shows.h2.a.text
    Year = shows.find('span', {"class":"subtle start-year"}).text[1:5]
    tmeta = shows.find('span', {"class":"tMeterScore"}).text 
    # https://realpython.com/beautiful-soup-web-scraper-python/
    link = shows.find('a')['href']
    movie_data.append(Rank + ',' + Name + ',' + Year + ',' + tmeta + ',' + link + "\n")

#reverse list, write to file
movie_data.reverse()
for movie in movie_data:
    f.write(movie)
f.close()