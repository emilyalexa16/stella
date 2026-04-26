import unittest
from src import create_app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app({
            "TESTING": True,
            "SECRET_KEY": "test"
        })
        self.client = self.app.test_client()

    # basic routes

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_route(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)

    def test_contact_route(self):
        response = self.client.get("/contact")
        self.assertEqual(response.status_code, 200)

    def test_instructions_route(self):
        response = self.client.get("/instructions")
        self.assertEqual(response.status_code, 200)

    # categories (session protected)

    def test_categories_with_no_session(self):
        response = self.client.get("/categories")
        self.assertEqual(response.status_code, 302)

    def test_categories_with_session(self):
        with self.client.session_transaction() as sess:
            sess["uploaded_file"] = "tests/fixtures/save/Ivans_401983009.xml"

        response = self.client.get("/categories")
        self.assertEqual(response.status_code, 200)

    # features (session dependent)

    def setUp_session(self):
        with self.client.session_transaction() as sess:
            sess["uploaded_file"] = "tests/fixtures/save/Ivans_401983009.xml"

    def test_friendships_route(self):
        self.setUp_session()
        response = self.client.get("/friendships")
        self.assertIn(response.status_code, [200, 302])

    def test_skills_route(self):
        self.setUp_session()
        response = self.client.get("/skills")
        self.assertIn(response.status_code, [200, 302])

    def test_progression_route(self):
        self.setUp_session()
        response = self.client.get("/progression")
        self.assertIn(response.status_code, [200, 302])

    def test_advanced_friendships_route(self):
        self.setUp_session()
        response = self.client.get("/advanced_friendships")
        self.assertIn(response.status_code, [200, 302])

    # error route

    def test_invalid_route(self):
        response = self.client.get("/invalid_route")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()