# The plugins i used
from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
load_dotenv() 

# Links for the API I've used here lmao just to be sure
# Youtube API (don't you save my api key, that shit will cost me money baoninam, just don't do it or i'll find you)
# https://www.googleapis.com/youtube/v3/playlists

# ZenQuotes (For motivational stuff i dunno, wala nakong maisip na ibang API, probably a placeholder for now)
# https://zenquotes.io/

# The Meal DB (So y'all can cook, also me lmao i suck at cooking)
# https://www.themealdb.com/

app = Flask(__name__)
CORS(app)

# Jikan API Part (Fetching anime data)
# To get random anime recommendation.
# - Random anime details including title, image URL, and MyAnimeList link.
@app.route("/anime/random", methods=["GET"])
def get_random_anime():
    """Fetches a random anime recommendation"""
    url = "https://api.jikan.moe/v4/random/anime"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# To get currently airing anime.
# - List of anime that are airing in the current season.
@app.route("/anime/season/now", methods=["GET"])
def get_current_season_anime():
    """Fetches currently airing anime"""
    url = "https://api.jikan.moe/v4/seasons/now"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# To search for anime by title.
# - List of anime matching the search term.
@app.route("/anime/search/<title>", methods=["GET"])
def search_anime(title):
    """Searches for anime by title"""
    url = f"https://api.jikan.moe/v4/anime?q={title}"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# To get anime details by ID
@app.route("/anime/<int:anime_id>", methods=["GET"])
def get_anime_by_id(anime_id):
    """Fetches anime details by ID"""
    url = f"https://api.jikan.moe/v4/anime/{anime_id}"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# 2nd API Used (Just putting areas like this so i don't get confused on what part am i scrolling to)
###################################################################################################################

# ZenQuotes API Part (Just found this random motivation api)
# To get a random motivational quote.
# - A random quote text and the author of the quote.
@app.route("/quotes/random", methods=["GET"])
def get_random_quote():
    """Fetches a random motivational quote"""
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    return jsonify(response.json())

# To get today's motivational quote.
# - Today's quote text and the author of the quote.
@app.route("/quotes/today", methods=["GET"])
def get_daily_quote():
    """Fetches today's motivational quote"""
    url = "https://zenquotes.io/api/today"
    response = requests.get(url)
    return jsonify(response.json())

# To get quotes from a specific author.
# - list of quotes from the specified author.
@app.route("/quotes/author/<author>", methods=["GET"])
def get_quotes_by_author(author):
    """Fetches quotes from a specific author"""
    url = f"https://zenquotes.io/api/quotes/{author}"
    response = requests.get(url)
    return jsonify(response.json())


# 3rd API Used (Just putting areas like this so i don't get confused on what part am i scrolling to)
###################################################################################################################

# TheMealDB API Part (Figured we can check for some cooking recipe like it's breaking bad)
# To get a random meal recipe.
# - Meal details including name, cooking instructions, and image URL.
@app.route("/meals/random", methods=["GET"])
def get_random_meal():
    """Fetches a random meal recipe"""
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    return jsonify(response.json())

# To get meals from a specific category (e.g., "Vegetarian").
# - list of meals in the specified category with meal names and image URLs.
@app.route("/meals/category/<category>", methods=["GET"])
def get_meals_by_category(category):
    """Fetches meals from a specific category"""
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
    response = requests.get(url)
    return jsonify(response.json())

# To search for a meal by its name.
# - list of meals matching the search term, with meal names, IDs, instructions, and images.
@app.route("/meals/search/<meal>", methods=["GET"])
def search_meal(meal):
    """Searches for a meal by name"""
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal}"
    response = requests.get(url)
    return jsonify(response.json())

# Run Flask Server
if __name__ == "__main__":
    app.run(debug=True)
