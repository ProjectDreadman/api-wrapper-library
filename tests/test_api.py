import unittest
from api_wrapper import APIWrapper, APIWrapperError

class TestAPIWrapper(unittest.TestCase):
    def setUp(self):
        self.api = APIWrapper(api_key="test_api_key")

    def test_get_success(self):
        response = self.api.get("test_endpoint")
        self.assertIsInstance(response, dict)

    def test_get_failure(self):
        with self.assertRaises(APIWrapperError):
            self.api.get("invalid_endpoint")

if __name__ == "__main__":
    unittest.main()
