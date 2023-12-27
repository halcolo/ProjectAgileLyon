import unittest
from api_routes import app
from unittest.mock import patch
from package.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.squad = "xzC8ollQoBJRv9l7ZhUG"
        self.name =  "John Doe"
        self.email = "johndoe@example.com"
        self.player = Player(self.name, self.email)

    def test_get_player_existing(self):
        # Mocking the get_player_by_email method to return a player
        with patch.object(Player, "get_player_by_email", return_value={"id": "123", "name": self.name, "email": self.email, "squad_id": "xyz"}):
            self.player.get_player()
            self.assertEqual(self.player.get_id(), "123")
            self.assertEqual(self.player.name, self.name)
            self.assertEqual(self.player.email, self.email)
            self.assertEqual(self.player.squad_id, "xyz")

    def test_get_player_non_existing(self):
        # Mocking the get_player_by_email method to return None
        with patch.object(Player, "get_player_by_email", return_value=None):
            self.player.get_player()
            # self.assertIsNone(self.player.get_id())
            self.assertEqual(self.player.name, self.name)
            self.assertEqual(self.player.email, self.email)
            self.assertEqual(self.player.squad_id, self.squad)

    def test_get_squad(self):
        
        self.player.squad_id = self.squad
        self.assertEqual(self.player.get_squad(), self.squad)
        
    def test_delete_player(self):
        with app.app_context():
            self.player.delete_player()

