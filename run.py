from flask import Flask, render_template


app = Flask(__name__)

# Defines the routes to the webpages.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/gallery.html")
def gallery():
    return render_template("gallery.html")

@app.route("/map.html")
def map():
    return render_template("map.html")

@app.route("/upload.html")
def upload():
    return render_template("upload.html")

@app.route("/ethics_paper.html")
def ethics_paper():
    return render_template("ethics_paper.html")

if __name__ == "__main__":
    app.run(debug=True)