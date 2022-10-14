from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_website = response.text

soup = BeautifulSoup(movie_website, "html.parser")

all_tags = soup.find_all(name="h3", class_="title")
all_movies = [movie.getText() for movie in all_tags]
# print(all_movies)

with open("movie.txt", "w", encoding="utf-8") as file:
    for movie in reversed(all_movies):
        file.write(f"{movie}\n")
