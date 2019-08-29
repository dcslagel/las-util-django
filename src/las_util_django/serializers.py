"""
File-Name: [app]/serializers.py
File-Desc: Rest API serializers for las_util_django
App-Name: las_util_django
Project-Name: Las-Util-Django
Copyright: Copyright (c) 2019, DC Slagel
License-Identifier: BSD-3-Clause
"""
from rest_framework import serializers
from las_util_django.models import VersionInfo

class VersionInfoSerializer(serializers.ModelSerializer):
    """Link ModelSerializer to the VersionInfo model"""
    class Meta:
        model = VersionInfo
        fields = '__all__'
