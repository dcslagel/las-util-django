import sys

# django's database is not needed so we use unittest.TestCase
# from django.test import TestCase
from unittest import TestCase


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

    def test_parse_version_record(self):
        entry = cntrl.SectionInfo()
        line = "VERS.               2.0 :   CWLS LOG ASCII STANDARD -VERSION 2.0"
        entry = cntrl.parse_formatted_section_line("V", line, entry)
        self.assertEqual(entry.name, "VERS")
        self.assertEqual(entry.unit, "")
        self.assertEqual(entry.value, "2.0")
        self.assertEqual(entry.note, "CWLS LOG ASCII STANDARD -VERSION 2.0")


    def test_parse_well_record(self):
        entry = cntrl.SectionInfo()
        line = "STRT    .M              1670.0000                :START DEPTH"
        entry = cntrl.parse_formatted_section_line("W", line, entry)
        self.assertEqual(entry.name, "STRT")
        self.assertEqual(entry.unit, "M")
        self.assertEqual(entry.value, "1670.0000")
        self.assertEqual(entry.note, "START DEPTH")

    def test_parse_curve_record(self):
        entry = cntrl.SectionInfo()
        line = "DEPT   .M                                       :  1  DEPTH"
        entry = cntrl.parse_formatted_section_line("C", line, entry)
        self.assertEqual(entry.name, "DEPT")
        self.assertEqual(entry.unit, "M")
        self.assertEqual(entry.value, "")
        self.assertEqual(entry.note, "1  DEPTH")

    def test_parse_param_record(self):
        entry = cntrl.SectionInfo()
        line = "MUD    .               GEL CHEM        :   MUD TYPE"
        entry = cntrl.parse_formatted_section_line("", line, entry)
        self.assertEqual(entry.name, "MUD")
        self.assertEqual(entry.unit, "")
        self.assertEqual(entry.value, "GEL CHEM")
        self.assertEqual(entry.note, "MUD TYPE")

