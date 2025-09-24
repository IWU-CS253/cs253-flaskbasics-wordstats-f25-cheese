from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/counting", method=["GET", "POST"])
def counting():
    sentence = request.form.get("sentence")

    words = sentence.split()
    word_count = len(words)
    character_count = 0
    for word in words:
        character_count += len(word)
    average = character_count / word_count

    if not sentence:
        return render_template("default.html")

    return render_template("counting.html", word_count=word_count, character_count=character_count, average=average)