from flask import Flask, request, jsonify
from pymongo import MongoClient 
import os 

app = Flask(__name__)

client = MongoClient(
    f"mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mangodb-service:27017/"
)

db = client.notesdb 
collection = db.motes 


@app.route("/") 
def home():
    return "Flask + MongoDB Kubernetes Project"

@app.route("/add", methods=["POST"])
def add_note():
    data = request.json 
    collection.insert_one(data) 
    return jsonify({"message": "Note Added"})

@app.route("/notes")
def get_notes():
    notes = [] 

    for note in collection.find({}, {"_id": O}):
        notes.append(note)

    return jsonify(notes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)