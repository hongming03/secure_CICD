import unittest
import json
import sys
import os

# Add src folder to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from app import app


class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        """Set up test client before each test"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_hello_world(self):
        """Test the root endpoint"""
        response = self.app.get('/')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, World!')
        self.assertEqual(data['status'], 'success')
    
    def test_health_check(self):
        """Test the health check endpoint"""
        response = self.app.get('/health')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'healthy')
    
    def test_hello_world_returns_json(self):
        """Test that response is JSON"""
        response = self.app.get('/')
        self.assertEqual(response.content_type, 'application/json')
    
    def test_health_check_returns_json(self):
        """Test that health check returns JSON"""
        response = self.app.get('/health')
        self.assertEqual(response.content_type, 'application/json')
    
    def test_invalid_route(self):
        """Test that invalid routes return 404"""
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()