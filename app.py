import random
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define a list of past life names and funny stories
past_lives = [
    {"name": "Sir Quackington", "story": "Once a noble duck knight who jousted with breadsticks."},
    {"name": "Princess Fuzzball", "story": "A royal feline with a penchant for stealing tuna from the court."},
    {"name": "Professor Bubbles", "story": "A mad scientist who invented the first talking fishbowl."},
    {"name": "Countess Snugglepaws", "story": "A vampire cat who only fed on warm, fluffy blankets."},
    {"name": "General Jumpy", "story": "A rabbit who led an army of carrot-loving soldiers."}
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        dob = request.form["dob"]
        gender = request.form["gender"]
        selected_past_life = random.choice(past_lives)
        return render_template("result.html", past_life=selected_past_life)
    return render_template("home.html")

@app.route("/postcard", methods=["POST"])
def postcard():
    past_life_name = request.form["past_life_name"]
    past_life_story = request.form["past_life_story"]
    return render_template("postcard.html", name=past_life_name, story=past_life_story)

if __name__ == "__main__":
    app.run(debug=True)
    