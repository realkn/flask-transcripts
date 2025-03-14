from flask import Flask, render_template
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# MongoDB Connection (Replace with your actual Mongo URI)
MONGO_URI = "mongodb://mongo:cOYgsQfGSjjbgWAAJUzgAoIkITbPcEGA@tramway.proxy.rlwy.net:28168"
client = MongoClient(MONGO_URI)
db = client["ticket_bot"]
tickets_collection = db["tickets"]

# Route to fetch and display a transcript
@app.route("/transcript/<transcript_id>")
def view_transcript(transcript_id):
    transcript = None

    # Try fetching by ObjectId first
    try:
        transcript = tickets_collection.find_one({"_id": ObjectId(transcript_id)})
    except:
        pass  # If it's not an ObjectId, ignore the error

    # If not found, try fetching by string ID
    if not transcript:
        transcript = tickets_collection.find_one({"_id": transcript_id})

    if transcript:
        return render_template("transcript.html", transcript=transcript["transcript"])
    
    return "Transcript not found.", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
