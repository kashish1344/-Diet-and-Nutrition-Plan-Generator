from flask import Flask, request, jsonify, render_template
from models.diet_matching import generate_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    user_profile = request.json
    if user_profile:
        recommendations = generate_recommendations(user_profile)
        return jsonify(recommendations)
    return jsonify({'error': 'Invalid profile data'}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
