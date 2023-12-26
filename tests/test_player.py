import unittest
from unittest.mock import patch
from package.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("John Doe", "johndoe@example.com")

    def test_get_player_existing(self):
        # Mocking the get_player_by_email method to return a player
        with patch.object(Player, "get_player_by_email", return_value={"id": "123", "name": "John Doe", "email": "johndoe@example.com", "squad_id": "xyz"}):
            self.player.get_player()
            self.assertEqual(self.player.get_id(), "123")
            self.assertEqual(self.player.name, "John Doe")
            self.assertEqual(self.player.email, "johndoe@example.com")
            self.assertEqual(self.player.squad_id, "xyz")

    def test_get_player_non_existing(self):
        # Mocking the get_player_by_email method to return None
        with patch.object(Player, "get_player_by_email", return_value=None):
            self.player.get_player()
            self.assertIsNone(self.player.get_id())
            self.assertEqual(self.player.name, "John Doe")
            self.assertEqual(self.player.email, "johndoe@example.com")
            self.assertEqual(self.player.squad_id, None)

    def test_create_player(self):
        # Mocking the db.collection and db.document methods
        with patch("player.db.collection") as mock_collection, patch("player.db.collection.document") as mock_document:
            mock_document.id = "456"
            self.player.create_player()
            mock_collection.assert_called_with("player")
            mock_document.assert_called_once()
            mock_document().set.assert_called_with({"name": "John Doe", "email": "johndoe@example.com", "squad_id": "xzC8ollQoBJRv9l7ZhUG"})
            self.assertEqual(self.player.get_id(), "456")
            self.assertEqual(self.player.squad_id, "xzC8ollQoBJRv9l7ZhUG")

    def test_get_squad(self):
        self.player.squad_id = "xyz"
        self.assertEqual(self.player.get_squad(), "xyz")
