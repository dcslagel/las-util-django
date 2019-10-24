import sys
from django.test import TestCase


from las_util.models import VersionInfo


# Create your tests here.
class VersionInfoModelTests(TestCase):
    mimetype = 'text/html'
    fixtures = ['version_info_data.json']

    @classmethod
    def setUpTestData(self):
        '''print("setUpTestData: Run once to set up data for all ModelTests")'''
        pass

    def setUp(self):
        '''print("setUp: Run once for every test method")'''
        pass

    def test_fixture_loading(self):
        self.assertEqual(18, VersionInfo.objects.count())
        pList = VersionInfo.objects.all()
        self.assertEqual(18, len(pList))

    def test_label_filename(self):
        item = VersionInfo.objects.get(pk=1)
        field_label = item._meta.get_field('filename').verbose_name
        self.assertEqual(field_label, 'filename')

    def test_label_name(self):
        item = VersionInfo.objects.get(pk=1)
        field_label = item._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_label_section(self):
        item = VersionInfo.objects.get(pk=1)
        field_label = item._meta.get_field('section').verbose_name
        self.assertEqual(field_label, 'section')

    def test_label_unit(self):
        item = VersionInfo.objects.get(pk=1)
        field_label = item._meta.get_field('unit').verbose_name
        self.assertEqual(field_label, 'unit')

    def test_label_value(self):
        item = VersionInfo.objects.get(pk=1)
        field_label = item._meta.get_field('value').verbose_name
        self.assertEqual(field_label, 'value')

    def test_label_note(self):
        item = VersionInfo.objects.get(pk=1)
        field_label = item._meta.get_field('note').verbose_name
        self.assertEqual(field_label, 'note')

    def test_label_filename_max_length(self):
        item = VersionInfo.objects.get(pk=1)
        max_length = item._meta.get_field('filename').max_length
        self.assertEqual(max_length, 100)

    def test_label_name_max_length(self):
        item = VersionInfo.objects.get(pk=1)
        max_length = item._meta.get_field('name').max_length
        self.assertEqual(max_length, 10)

    def test_label_section_max_length(self):
        item = VersionInfo.objects.get(pk=1)
        max_length = item._meta.get_field('section').max_length
        self.assertEqual(max_length, 30)

    def test_label_unit_max_length(self):
        item = VersionInfo.objects.get(pk=1)
        max_length = item._meta.get_field('unit').max_length
        self.assertEqual(max_length, 10)

    def test_label_value_max_length(self):
        item = VersionInfo.objects.get(pk=1)
        max_length = item._meta.get_field('value').max_length
        self.assertEqual(max_length, 100)

    def test_label_note_max_length(self):
        item = VersionInfo.objects.get(pk=1)
        max_length = item._meta.get_field('note').max_length
        self.assertEqual(max_length, 100)

    def test_object_str(self):
        item = VersionInfo.objects.get(pk=1)
        tmpl = "filename: {}, section: {}, name: {}, unit: {}, value: {}, note: {}\n"
        expected_str = tmpl.format(item.filename, item.section, item.name, item.unit, item.value, item.note)
        self.assertEqual(expected_str, str(item))

