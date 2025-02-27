# The plugins i used
from flask import Flask, jsonify
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
