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
# - List of meals in the specified category with meal names and image URLs.
@app.route("/meals/category/<category>", methods=["GET"])
def get_meals_by_category(category):
    """Fetches meals from a specific category"""
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
    response = requests.get(url)
    return jsonify(response.json())

# To search for a meal by its name.
# - List of meals matching the search term, with meal names, IDs, instructions, and images.
@app.route("/meals/search/<meal>", methods=["GET"])
def search_meal(meal):
    """Searches for a meal by name"""
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal}"
    response = requests.get(url)
    return jsonify(response.json())

# ✅ NEW: Fetch full meal details by ID.
# - Get full meal details, including category, area, instructions, and YouTube link.
@app.route("/meals/detail/<meal_id>", methods=["GET"])
def get_meal_by_id(meal_id):
    """Fetches full meal details by ID"""
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(url)

    # Check if meal exists
    data = response.json().get("meals")
    if data:
        return jsonify(data[0])  # Return detailed meal
    else:
        return jsonify({"error": "Meal not found"}), 404
    
# Youtube API Part (Please don't check my playlist here, it's just some weeb shit)
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
PLAYLIST_ID = "PLwBM_ksR_HWyD9g1BvD_gH89XqQAsYjCx"

# To get all videos from a YouTube playlist.
# - A list of videos with titles, descriptions, video IDs, and other video details.
@app.route("/youtube/playlist", methods=["GET"])
def get_playlist_videos():
    """Fetches all videos from a YouTube playlist"""
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=5&playlistId={PLAYLIST_ID}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch playlist"}), response.status_code

# To get details of a specific video by video_id.
# - Video details like title, description, tags, published date, and thumbnails.
@app.route("/youtube/video/<video_id>", methods=["GET"])
def get_video_details(video_id):
    """Fetches details of a specific video"""
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch video details"}), response.status_code

# To get information about a YouTube channel by channel_id.
# - Channel information like title, description, and view count.
@app.route("/youtube/channel/<channel_id>", methods=["GET"])
def get_channel_info(channel_id):
    """Fetches details of a specific YouTube channel"""
    url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch channel info"}), response.status_code

###################################################################################################################

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
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=True)
