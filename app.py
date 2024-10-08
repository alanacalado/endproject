from flask import Flask, render_template, request

app = Flask(__name__)

# Definição das perguntas
questions = [
    {
        "question": "Como você descreveria sua pele ao acordar?",
        "options": ["Oleosa", "Normal", "Seca", "Mista"]
    },
    {
        "question": "Sua pele tende a ficar brilhante ao longo do dia?",
        "options": ["Sim", "Não"]
    },
    {
        "question": "Você tem tendência a acne?",
        "options": ["Sim", "Não"]
    },
    {
        "question": "Sua pele fica vermelha ou irritada facilmente?",
        "options": ["Sim", "Não"]
    },
    {
        "question": "Você sente sua pele seca ou áspera?",
        "options": ["Sim", "Não"]
    },
    {
        "question": "Você já notou áreas secas e descamativas na sua pele?",
        "options": ["Sim", "Não"]
    },
    {
        "question": "Sua pele se irrita com produtos cosméticos?",
        "options": ["Sim", "Não"]
    },
    {
        "question": "Você tem alguma condição como rosácea ou eczema?",
        "options": ["Sim", "Não"]
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    score = {
        'normal': 0,
        'oleosa': 0,
        'seca': 0,
        'mista': 0,
        'acneica': 0,
        'rosacea': 0,
        'sensível': 0
    }

    answers = request.form

    # Incrementa os scores com base nas respostas
    if answers.get('question-0') == "Oleosa":
        score['oleosa'] += 1
    elif answers.get('question-0') == "Normal":
        score['normal'] += 1
    elif answers.get('question-0') == "Seca":
        score['seca'] += 1
    elif answers.get('question-0') == "Mista":
        score['mista'] += 1

    if answers.get('question-1') == "Sim":
        score['oleosa'] += 1
    if answers.get('question-2') == "Sim":
        score['acneica'] += 1
    if answers.get('question-3') == "Sim":
        score['sensível'] += 1
    if answers.get('question-4') == "Sim":
        score['seca'] += 1
    if answers.get('question-5') == "Sim":
        score['seca'] += 1
    if answers.get('question-6') == "Sim":
        score['sensível'] += 1
    if answers.get('question-7') == "Sim":
        score['rosacea'] += 1

    # Determinando o tipo de pele
    result = ""
    if score['oleosa'] > 0:
        result += "Sua pele é oleosa."
    if score['seca'] > 0:
        result += " Sua pele é seca."
    if score['mista'] > 0:
        result += " Sua pele é mista."
    if score['acneica'] > 0:
        result += " Sua pele é acneica."
    if score['rosacea'] > 0:
        result += " Você pode ter rosácea."
    if score['sensível'] > 0:
        result += " Sua pele é sensível."

    if result == "":
        result = "Sua pele é normal."

    return render_template('result.html', result=result.strip())

if __name__ == '__main__':
    app.run(debug=True)