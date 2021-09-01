from flask import Flask, render_template, request
from flask.json import jsonify
from functions import *
import json


with open('./json/races.json') as rc_file:
    race_data = json.load(rc_file)

with open('./json/classes.json') as class_file:
    class_data = json.load(class_file)

with open('./json/backgrounds.json') as bg_file:
    background_data = json.load(bg_file)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/random-character", methods=["GET"])
def get_random_character():
    race = pick_race(race_data)
    cclass = pick_class(class_data)
    subclass = pick_subclass(cclass)
    background = pick_background(background_data)
    equipment = add_equipment_from_class(
        cclass) + add_equipment_from_background(background)
    stats_array = roll_for_stats()

    response = {
        "race": race["name"],
        "class": cclass["name"],
        "subclass": subclass,
        "background": background["name"],
        "background feature": background["feature"],
        "stats": stats_array,
        "equipment": equipment
    }

    return jsonify(response)


@app.route("/get-background")
def search_background():
    searched = request.args.get("bg").lower().strip('"')
    for bg in background_data:
        name = bg["name"].lower()
        if name == searched:
            return jsonify(bg)
    return jsonify(error={"Not found": "that does not match any existing entries"})


@app.route("/get-class")
def search_class():
    searched = request.args.get("class").lower().strip('"')
    print(searched)
    for cclass in class_data:
        name = cclass["name"].lower()
        if name == searched:
            return jsonify(cclass)
    return jsonify(error={"Not found": "that does not match any existing entries"})


if __name__ == '__main__':
    app.run(debug=True)
