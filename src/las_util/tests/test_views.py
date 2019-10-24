import sys
from django.test import TestCase
from django.urls import reverse

from las_util.models import VersionInfo


# Create your tests here.
class ViewTests(TestCase):
    mimetype = 'text/html'
    fixtures = ['version_info_data.json']

    @classmethod
    def setUpTestData(self):
        '''print("setUpTestData: Run once to set up data for all ModelTests")'''
        VersionInfo.objects.create(name="myversionline")
        pass

    def setUp(self):
        '''print("setUp: Run once for every test method")'''
        pass

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
        self.assertEqual(response.content, b'')
        # self.assertRedirects(response, '/upload/') # this currently fails with expected 302, got 301

    def test_upload_with_slash_returns_200(self):
        response = self.client.get('/upload/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mimetype, response.__getitem__('content-type'))
        self.assertTemplateUsed(response, 'las_util/upload.html')
        self.assertIn(b'<h2>Upload LAS File</h2>', response.content)
        self.assertIn(b'Copyright &copy; 2019 - Present, DC Slagel', response.content)

    def test_upload_view_accessible_by_name(self):
        response = self.client.get(reverse('upload'))
        self.assertEqual(response.status_code, 200)

    def test_list_no_slash_returns_301(self):
        response = self.client.get('/list')
        self.assertEqual(response.status_code, 301)
        self.assertIn(self.mimetype, response.__getitem__('content-type'))
        self.assertEqual(response['location'], '/list/')
        self.assertEqual(response.content, b'')

    def test_list_with_slash_returns_200(self):
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mimetype, response.__getitem__('content-type'))
        self.assertTemplateUsed(response, 'las_util/list.html')
        self.assertIn(b'<h2>LAS-Util File List</h2>', response.content)
        test_str = b'href=/detail/las_file-2019-10-01-11-11-50.las'
        self.assertIn(test_str, response.content)

    def test_list_view_accessible_by_name(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_with_slash_returns_200(self):
        response = self.client.get('/detail/las_file-2019-10-01-11-11-50.las')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'las_util/detail_display.html')
        


class ApiViewTests(TestCase):
    mimetype = 'text/html'

    def setUp(self):
        pass

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

    def setUp(self):
        VersionInfo.objects.create(name="myversionline")

    def test_is_section_the_version_section(self):
        vi = VersionInfo.objects.all()
        self.assertEqual(len(vi), 1)
