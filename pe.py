from flask import Flask, request, jsonify
import random

app = Flask(_name_)

name_ideas = {
    "tech": ["CodeNova", "TechTide", "ByteBloom", "NeuroStack", "InnovForge"],
    "health": ["FitPulse", "MindMend", "WellnessWave", "CoreVital", "Healthly"],
    "travel": ["Wanderly", "Roamly", "TripNest", "NomadSky", "GlobeGo"],
    "finance": ["FinWise", "WealthGrid", "Budgetly", "CoinNest", "MoneyMate"],
    "creative": ["SparkNest", "MuseForge", "DreamWeave", "CreateFlow", "IdeaFlick"]
}

def get_category(text):
    text = text.lower()
    if "tech" in text:
        return "tech"
    if "health" in text or "fitness" in text:
        return "health"
    if "travel" in text or "trip" in text:
        return "travel"
    if "finance" in text or "money" in text:
        return "finance"
    if "creative" in text or "design" in text:
        return "creative"
    return None

@app.route('/generate', methods=['POST'])
def generate_name():
    data = request.json
    message = data.get("message", "")
    category = get_category(message)

    if category and category in name_ideas:
        suggestion = random.choice(name_ideas[category])
        return jsonify({"response": f"How about: {suggestion}"})
    else:
        return jsonify({"response": "Hmm, I didn’t get the category. Try mentioning tech, travel, health, etc."})

if _name_ == '_main_':
    app.run(debug=True)

