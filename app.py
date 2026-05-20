from flask import Flask, render_template, request
import fakenewss

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    prediction = None
    confidence = None
    news = ""

    if request.method == "POST":

        news = request.form["news"]

        prediction, confidence = fakenewss.web_predict(news)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        news=news
    )

if __name__ == "__main__":
    app.run(debug=True)