import unittest
from app import app, db
from app.models import User

class RoutesTestCase(unittest.TestCase):
    
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

    def test_get_users(self):
        response = self.client.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'testuser', response.data)
