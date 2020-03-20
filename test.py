from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):

    def test_board_display(self):
        " test display of game board on HTML"

        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
