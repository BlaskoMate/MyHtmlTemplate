from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
    return render_template("main.html")

@app.route("/news", methods=['GET'])
def news():
    return render_template("news.html")

@app.route("/gallery", methods=['GET'])
def gallery():
    return render_template("gallery.html")

@app.route("/location", methods=['GET'])
def location():
    return render_template("location.html")

@app.route("/video", methods=['GET'])
def video():
    return render_template("video.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1',
            port=5000,
            debug=True)


