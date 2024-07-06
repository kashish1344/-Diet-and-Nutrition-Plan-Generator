from flask import Blueprint, request, jsonify
from models.diet_matching import generate_recommendations

recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/generate', methods=['POST'])
def get_recommendation():
    user_profile = request.json.get('profile')
    if user_profile:
        recommendations = generate_recommendations(user_profile)
        return jsonify(recommendations)
    return jsonify({'error': 'Invalid profile data'}), 400
