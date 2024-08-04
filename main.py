from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis', model="dharalam/mtg_card_classifier")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        card_name = request.form.get("card_name", "")
        set_name = request.form.get("set", "")
        rarity = request.form.get("rarity", "")
        card_type = request.form.get("type", "")
        mana_cost = request.form.get("mana_cost", "")
        power = request.form.get("power", "")
        toughness = request.form.get("toughness", "")
        loyalty = request.form.get("loyalty", "")
        defense_counters = request.form.get("defense_counters", "")
        ability = request.form.get("ability", "")

        card_description = "\n".join(filter(None, [
            card_name,
            set_name,
            rarity,
            card_type,
            mana_cost,
            power,
            toughness,
            loyalty,
            defense_counters,
            ability
        ]))

        result = sentiment_pipeline(card_description)[0]
        return render_template("full.html", result=result)

    return render_template("full.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
