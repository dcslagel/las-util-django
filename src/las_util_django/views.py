"""
File-Name: [app]/views.py
File-Desc: App views for las-util-django
App-Name: las-util-django
Project-Name: Las-Util-Django
Copyright: Copyright (c) 2019, DC Slagel
License-Identifier: BSD-3-Clause
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import Http404

# imports for rest api
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# las-util-django imports
from .models import UploadForm, Upload, VersionInfo
from .cntrl import parse

# las-util-django imports for rest api
from .serializers import DocSerializer, ListSerializer


# Create your views here.
def home(request):
    """Home page"""
    context = {}

    return render(request, 'las_util_django/home.html', context)

def upload(request):
    """Main page for uploading las files"""
    if request.method == 'POST':
        inform = UploadForm(request.POST, request.FILES)
        if inform.is_valid():
            parse(request.FILES['filename'])
            # Redirect to the data display
            return HttpResponseRedirect(reverse('home'))
    else:
        inform = UploadForm()

    infileslist = Upload.objects.all().order_by('-upload_date')
    version_section = VersionInfo.objects.all()

    context = {
        'form': inform,
        'infiles': infileslist,
        'version_section': version_section
    }

    return render(request, 'las_util_django/upload.html', context)

def list(request):
    """
    Display list of las documents

    Get one instance of each filename from database.
    There will be one 'VERS' row for each filename, so we use that as the filter.
    """
    docs = VersionInfo.objects.filter(name='VERS')
    # queryset = VersionInfo.objects.values('filename').distinct()

    '''
    res = HttpResponse()
    res.write('<!doctype html><html><head></head><body>')

    if docs:
        res.write('<table><tbody>')
        for doc in docs:
            item = '<tr><td><a href=/detail/' + doc.filename + '>' + doc.filename + '</a></td></tr>'
            res.write(item)
        res.write('</tbody></table>')
    else:
        # If there isn't any files then go back to home page
        return HttpResponseRedirect(reverse('home'))

    res.write("</body></html>")
    return res
    '''

    if docs:
        return render(request, 'las_util_django/list.html', {'docs': docs})
    else:
        # If there isn't any files then go back to home page
        return HttpResponseRedirect(reverse('home'))

def detail(request, docName):
    doc = VersionInfo.objects.filter(filename=docName)
    '''
    res = HttpResponse()
    res.write("<!doctype html><html><head></head><body>")

    if docs:
        res.write('<table><tbody>')
        for row in docs:
            filename = '<tr><td>' + row.filename + '</td>'
            section = '<td>' + row.section + '</td>'
            name = '<td>' + row.name + '</td>'
            unit = '<td>' + row.unit + '</td>'
            value = '<td>' + row.value + '</td>'
            note = '<td>' + row.note + '</td>'
            item = filename + section + name + unit + value + note + '</tr>'
            res.write(item)
        res.write("</body></html>")
    else:
        # If there isn't any files then go back to home page
        return HttpResponseRedirect(reverse('home'))

    return res
    '''

    if doc:
        return render(request, 'las_util_django/detail_display.html', {'doc': doc})
    else:
        # If there isn't any files then go back to home page
        return HttpResponseRedirect(reverse('home'))


    
class DumpApi(generics.ListCreateAPIView):
    """Create class for handling GET and POST api requests"""
    queryset = VersionInfo.objects.all()
    serializer_class = DocSerializer


class ListApi(generics.ListCreateAPIView):
    """Retrieve json with unique filename list"""
    queryset = VersionInfo.objects.values('filename').distinct()
    serializer_class = ListSerializer


class DetailApi(APIView):

    def get_objects(self, filename):
        try:
            return VersionInfo.objects.filter(filename=filename)
        except VersionInfo.DoesNotExist:
            return Http404

    def get(self, request, filename, format=None):
        queryset = self.get_objects(filename)
        serializer = DocSerializer(queryset, many=True)
        return Response(serializer.data)
