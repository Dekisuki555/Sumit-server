from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load database
with open('database.json') as db:
    data = json.load(db)

# Load questions
with open('questions.json') as qf:
    questions = json.load(qf)

@app.route('/')
def home():
    return render_template('index.html', data=data)

@app.route('/api/player/<player_id>', methods=['GET'])
def get_player(player_id):
    player = data['players'].get(player_id, {})
    return jsonify(player)

@app.route('/api/player/<player_id>/add_ticket', methods=['POST'])
def add_ticket(player_id):
    data['players'].setdefault(player_id, {'tickets': 0})
    data['players'][player_id]['tickets'] += 10
    save_db()
    return jsonify({'status': 'success'})

@app.route('/api/question', methods=['GET'])
def get_question():
    return jsonify(questions)

def save_db():
    with open('database.json', 'w') as db:
        json.dump(data, db, indent=4)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)