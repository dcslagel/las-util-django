import sys
from django.test import TestCase


from .models import VersionInfo

# Create your tests here.
class RouteTests(TestCase):

    def setup(self):
        VersionInfo.objects.create(name="myverisionline")

    def test_home_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_no_slash_returns_301(self):
        response = self.client.get('/upload')
        self.assertEqual(response.status_code, 301)

    def test_upload_with_slash_returns_200(self):
        response = self.client.get('/upload/')
        self.assertEqual(response.status_code, 200)

    def test_list_no_slash_returns_301(self):
        response = self.client.get('/list')
        self.assertEqual(response.status_code, 301)

    def test_list_with_slash_returns_302(self):
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 302)

    def test_upload_get_no_slash_returns_405(self):
        response = self.client.get('/api/upload')
        self.assertEqual(response.status_code, 405)

    def test_upload_get_with_slash_returns_405(self):
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
        self.assertEqual(response.status_code, 200)

    def test_dump_with_slash_returns_200(self):
        response = self.client.get('/api/dump/')
        self.assertEqual(response.status_code, 200)

    def test_list_no_slash_returns_200(self):
        response = self.client.get('/api/list')
        self.assertEqual(response.status_code, 200)

    def test_list_with_slash_returns_200(self):
        response = self.client.get('/api/list/')
        self.assertEqual(response.status_code, 200)


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
