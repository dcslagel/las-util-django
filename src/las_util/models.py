"""
File-Name: [app]/models.py
File-Desc: App models and functions for las-util
App-Name: las-util-django
Project-Name: Las-Util-Django
Copyright: Copyright (c) 2019, DC Slagel
License-Identifier: BSD-3-Clause
"""

from django.db import models
from django.forms import ModelForm

# Create your models here.
class Upload(models.Model):
    """Model to register the location of an uploaded file"""
    filename = models.FileField()
    upload_date = models.DateTimeField(auto_now_add=True)

class UploadForm(ModelForm):
    """FileUpload form class"""
    class Meta:
        model = Upload
        fields = ('filename',)

class SectionInfo(models.Model):
    """Section fields for LAS metadata sections"""
    filename = models.CharField(max_length=100)
    section = models.CharField(max_length=30)
    name = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    value = models.CharField(max_length=100)
    note = models.CharField(max_length=100)

    def __str__(self):
        tmpl = "filename: {}, section: {}, name: {}, unit: {}, value: {}, note: {}\n"
        return (tmpl.format(
            self.filename, self.section, self.name, self.unit, self.value, self.note))
