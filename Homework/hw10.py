from flask import Flask
import json

with open("candidates.json") as file:
    candidates = json.load(file)

app = Flask(__name__)

"""
Главная страница
"""
@app.route("/")
def main_page():
    main_page_candidates = ""
    for candidate in candidates:
        main_page_candidates += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n"
    return f"<pre>{main_page_candidates}</pre>"


"""
Страница для поиска кандидатов по id
"""
@app.route("/candidate/<int:id>")
def candidate_page(id):
    candidate_photo = ""
    candidate_data = ""
    for candidate in candidates:
        if id == candidate['id']:
            candidate_photo += f"<img src={candidate['picture']}>\n\n\n"
            candidate_data += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n"
    return f"<pre>{candidate_photo}{candidate_data}</pre>"

"""
Страница для поиска кандидатов по скиллам
"""
@app.route("/candidate/<skill>")
def candidates_skill(skill):
    candidate_skills = ""
    for candidate in candidates:
        if skill in candidate['skills']:
            candidate_skills += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n"
    return f"<pre>{candidate_skills}</pre>"


app.run()
