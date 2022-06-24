from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import ToDos

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY="testsecretkey",
            WTF_CSRF_ENABLED=False
            )
        return app
    
    def setUp(self):
        db.create_all()
        test = ToDos(task='Test',completed=True)
        db.session.add(test)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)