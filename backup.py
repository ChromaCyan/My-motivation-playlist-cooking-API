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
