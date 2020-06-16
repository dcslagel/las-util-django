import sys
import os 

from django.test import TestCase
# from unittest import TestCase


import las_util.cntrl as cntrl


# Create your tests here.
class ParseRecordTests(TestCase):

    """
    @classmethod
    def setUpTestData(self):
        '''print("setUpTestData: Run once to set up data for all ModelTests")'''
        pass

    def setUp(self):
        '''print("setUp: Run once for every test method")'''
        pass
    """

    def test_parse_record(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        las_path = dir_path + "/../example_data/sample_2.0.las"
        las_file = open(las_path, "+rb")
        entry_filename = cntrl.parse(las_file)
        self.assertEqual(entry_filename[0:8], "las_file")
        self.assertTrue(entry_filename.endswith('.las'))
        self.assertEqual(cntrl.SectionInfo.objects.count(), 32)

        pList = cntrl.SectionInfo.objects.all()

        # Check expected number of records
        self.assertEqual(pList.distinct().count(), 32)
        self.assertEqual(pList.filter(section = "~VERSION INFORMATION").count(), 2)
        self.assertEqual(pList.filter(section = "~WELL INFORMATION").count(), 12)
        self.assertEqual(pList.filter(section = "~CURVE INFORMATION").count(), 8)
        self.assertEqual(pList.filter(section = "~PARAM INFORMATION").count(), 0)
        self.assertEqual(pList.filter(section = "~OTHER").count(), 2)
        self.assertEqual(pList.filter(section = "").count(), 0)

        # Check specific data
        self.assertEqual(pList.get(section = "~VERSION INFORMATION", name = "VERS").value, '2.0')
