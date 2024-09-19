from flask import jsonify, request
from app import app, db
from app.models import User

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              username:
                type: string
              email:
                type: string
    """
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])
