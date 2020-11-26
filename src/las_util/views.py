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
from django.http import Http404
from django.utils.html import format_html
from django.urls import reverse

# imports for rest api
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# las-util-django imports
from .models import UploadForm, Upload, SectionInfo
from .cntrl import parse

# las-util-django imports for rest api
from .serializers import DocSerializer, ListSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content info JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# Create your views here.
def home(request):
    """Home page"""
    context = {}

    return render(request, 'las_util/home.html', context)

def upload(request):
    message = 'Choose file to upload'

    """Main page for uploading las files"""
    if request.method == 'POST':
        inform = UploadForm(request.POST, request.FILES)
        if inform.is_valid():
            stored_filename = parse(request.FILES['filename'])
            # Example uploaded file path
            # http://127.0.0.1:8000/detail/las_file-2020-10-15-13-52-56.las
            msg_template = 'Upload file as: <a href="/detail/{}">{}</a>'
            message = format_html(msg_template.format(
                stored_filename,
                stored_filename
            ))
        else:
            message = 'Failed to upload file. Retry.'
            inform = UploadForm()
    else:
        inform = UploadForm()

    infileslist = Upload.objects.all().order_by('-upload_date')
    version_section = SectionInfo.objects.all()

    context = {
        'form': inform,
        'infiles': infileslist,
        'version_section': version_section,
        'message' : message 
    }

    return render(request, 'las_util/upload.html', context)

def list(request):
    """
    Display list of las documents

    Get one instance of each filename from database.
    There will be one 'VERS' row for each filename, so we use that as the filter.
    """
    docs = SectionInfo.objects.filter(name='VERS')
    # queryset = SectionInfo.objects.values('filename').distinct()

    if docs:
        return render(request, 'las_util/list.html', {'docs': docs})
    else:
        # If there isn't any files then go back to home page
        return HttpResponseRedirect(reverse('home'))

def detail(request, docName):
    doc = SectionInfo.objects.filter(filename=docName)

    if doc and docName:
        return render(request, 'las_util/detail_display.html',
                      {'doc': doc, 'docName': docName})
    else:
        # If there isn't any files then go back to home page
        return HttpResponseRedirect(reverse('home'))


def api_upload(request):
    """Api view for uploading las files"""
    """
        This is an example for using the Serializer class
        TODO: Find an example that uploads a file
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(snippet, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResonse(serializer.errors, status=400)
    """
    if request.method == 'POST':
        inform = UploadForm(request.POST, request.FILES)
        if inform.is_valid():
            filename = request.FILES['filename']
            newname = parse(filename)
            # Redirect to the data display
            message = "Saved LAS data from {} as {}".format(
                filename,
                newname
            )
            # TODO: add new url location to Response headers
            # TODO: add new url to json response data
            return JSONResponse({'result': message},
                                status=status.HTTP_201_CREATED)
        else:
            return JSONResponse(form.errors,
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        message = "Retry api/upload as a POST request"
        return JSONResponse({'result': message},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)



class DumpApi(generics.ListCreateAPIView):
    """Create class for handling GET and POST api requests"""
    queryset = SectionInfo.objects.all()
    serializer_class = DocSerializer


class ListApi(generics.ListCreateAPIView):
    """Retrieve json with unique filename list"""
    queryset = SectionInfo.objects.values('filename').distinct()
    serializer_class = ListSerializer


class DetailApi(APIView):

    def get_objects(self, filename):
        try:
            return SectionInfo.objects.filter(filename=filename)
        except SectionInfo.DoesNotExist:
            return Http404

    def get(self, request, filename, format=None):
        queryset = self.get_objects(filename)
        serializer = DocSerializer(queryset, many=True)
        return Response(serializer.data)
