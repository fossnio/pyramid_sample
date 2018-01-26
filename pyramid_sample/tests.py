import os
import unittest
import plaster
from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home_view(self):
        from .views import home_view
        request = testing.DummyRequest()
        info = home_view(request)
        self.assertEqual(info['project'], 'pyramid-sample')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyramid_sample import main
        config_loader = plaster.get_loader(os.environ.get('ini_file', 'development.ini'), protocols=['wsgi'])
        app = main({}, **config_loader.get_settings('app:main'))
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'pyramid-sample' in res.body)
