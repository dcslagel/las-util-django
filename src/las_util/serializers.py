"""
File-Name: [app]/serializers.py
File-Desc: Rest API serializers for las_util
App-Name: las_util
Project-Name: Las-Util-Django
Copyright: Copyright (c) 2019, DC Slagel
License-Identifier: BSD-3-Clause
"""
from rest_framework import serializers
from las_util.models import VersionInfo

class DocSerializer(serializers.ModelSerializer):
    """Link ModelSerializer to the VersionInfo model"""
    class Meta:
        model = VersionInfo
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    """Link ModelSerializer to the VersionInfo model"""
    class Meta:
        model = VersionInfo
        fields = ['filename']

# TODO: replace view.api_upload with to use this
# class UploadSerializer(serializer.ModelSerializer):
#     """Link ModelSerializer to the Upload model"""
#     class Meta:
#         model = Upload
#         fields = ['filename',]
