from flask import Flask, jsonify
import requests
import os

# This one is a backup in case i suffer on implementing one of the api for the app, so i have a backup one i can put on the api.py
# Jikan API (I just want recommendation, below is the documentation)
# https://jikan.moe/

# Dog CEO (For dog images)
# https://dog.ceo/dog-api/

# Advice Slip API (For random advice)
# https://api.adviceslip.com/

app = Flask(__name__)

# 1st API Used (Just putting areas like this so i don't get confused on what part am i scrolling to)
###################################################################################################################

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

###################################################################################################################

# 2nd API Used (Dog CEO API Part - Fetching random dog images)
# To get a random dog image.
# - Random dog image URL.
@app.route("/dog/random", methods=["GET"])
def get_random_dog():
    """Fetches a random dog image"""
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# To get a random dog image from a specific breed.
# - Dog image URL for the specific breed.
@app.route("/dog/breed/<breed>/random", methods=["GET"])
def get_dog_by_breed(breed):
    """Fetches a random dog image from a specific breed"""
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# To get a list of all dog breeds.
# - List of all dog breeds available.
@app.route("/dog/breeds/list", methods=["GET"])
def get_all_dog_breeds():
    """Fetches all dog breeds"""
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

###################################################################################################################

# 3rd API Used (Advice Slip API Part - Fetching random advice)
# To get a random piece of advice.
# - Random piece of advice.
@app.route("/advice/random", methods=["GET"])
def get_random_advice():
    """Fetches a random piece of advice"""
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# To get a specific piece of advice by ID.
# - Piece of advice by a specific ID.
@app.route("/advice/<advice_id>", methods=["GET"])
def get_advice_by_id(advice_id):
    """Fetches a specific piece of advice by ID"""
    url = f"https://api.adviceslip.com/advice/{advice_id}"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# To get specific advice by searching
# - Search for specific advice
@app.route("/advice/slips/<query>", methods=["GET"])
def get_advice_by_search(query):
    """Fetches advice by search query"""
    url = f"https://api.adviceslip.com/advice/search/{query}"  # Use f-string to insert the query
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

###################################################################################################################

# Run Flask Server
if __name__ == "__main__":
    app.run(debug=True)
