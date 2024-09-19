import unittest
from app import app, db
from app.models import User

class ModelsTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()
        with app.app_context():
            db.create_all()
            user = User(username='testuser', email='testuser@example.com')
            db.session.add(user)
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.drop_all()

    def test_user_creation(self):
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'testuser@example.com')
