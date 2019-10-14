import sys
from django.test import TestCase


from .models import VersionInfo


# Create your tests here.
class RouteTests(TestCase):
    mimetype = 'text/html'

    def setup(self):
        VersionInfo.objects.create(name="myverisionline")

    def test_home_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mimetype, response.__getitem__('content-type'))
        self.assertIn(b'<h2>Welcome to LAS-Util</h2>', response.content)
        self.assertIn(b'Copyright &copy; 2019 - Present, DC Slagel', response.content)

    def test_upload_no_slash_returns_301(self):
        response = self.client.get('/upload')
        self.assertEqual(response.status_code, 301)
        self.assertIn(self.mimetype, response.__getitem__('content-type'))
        self.assertEqual('/upload/', response['location'])
        self.assertIn(b'', response.content)

    def test_upload_with_slash_returns_200(self):
        response = self.client.get('/upload/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mimetype, response.__getitem__('content-type'))
        self.assertIn(b'<h2>Upload LAS File</h2>', response.content)
        self.assertIn(b'Copyright &copy; 2019 - Present, DC Slagel', response.content)

    def test_list_no_slash_returns_301(self):
        response = self.client.get('/list')
        self.assertEqual(response.status_code, 301)
        self.assertIn(self.mimetype, response.__getitem__('content-type'))
        self.assertEqual('/list/', response['location'])
        self.assertIn(b'', response.content)

    def test_list_with_slash_returns_302(self):
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.mimetype, response.__getitem__('content-type'))
        # Till test data is added
        self.assertEqual('/', response['location'])
        self.assertIn(b'', response.content)


class ApiRouteTests(TestCase):
    mimetype = 'text/html'

    def setup(self):
        VersionInfo.objects.create(name="myverisionline")

    def test_api_upload_get_no_slash_returns_405(self):
        response = self.client.get('/api/upload')
        test_str = b'{"result":"Retry api/upload as a POST request"}'

        self.assertEqual(response.status_code, 405)
        self.assertEqual(test_str, response.content)

    def test_api_upload_get_with_slash_returns_405(self):
        response = self.client.get('/api/upload/')
        self.assertEqual(response.status_code, 405)

    """
    def test_upload_post_no_slash_returns_200(self):
        response = self.client.post('/api/upload')
        self.assertEqual(response.status_code, 200)
    """

    def test_upload_post_with_slash_returns_201(self):
        with open('las_util/example_data/version.las') as fp:
            response = self.client.post(
                '/api/upload/',
                { 'filename' : fp })
            self.assertEqual(response.status_code, 201)


    def test_dump_no_slash_returns_200(self):
        response = self.client.get('/api/dump')
        test_str = b'[]'

        self.assertEqual(response.status_code, 200)
        self.assertEqual(test_str, response.content)

    def test_dump_with_slash_returns_200(self):
        response = self.client.get('/api/dump/')
        test_str = b'[]'

        self.assertEqual(response.status_code, 200)
        self.assertEqual(test_str, response.content)

    def test_list_no_slash_returns_200(self):
        response = self.client.get('/api/list')
        test_str = b'[]'

        self.assertEqual(response.status_code, 200)
        self.assertEqual(test_str, response.content)

    def test_list_with_slash_returns_200(self):
        response = self.client.get('/api/list/')
        test_str = b'[]'

        self.assertEqual(response.status_code, 200)
        self.assertEqual(test_str, response.content)

    """
    def test_versioninfo_object(self):
        vi = VersionInfo.objects.get(name="myversionline")
        self.assertEqual(vi['name'] == 'myversionline', True)
    """

class VersionInfoTests(TestCase):

    def test_is_section_the_version_section(self):
        VersionInfo.objects.create(name="myverisionline")

        vi = VersionInfo.objects.all()
        self.assertIs(len(vi) == 1, True)
