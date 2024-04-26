import os
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import render
from .models import Application, Environment

# Define your views here.

def index(request):
    if request.method == 'GET' and 'a_code' in request.GET:
        a_code = request.GET.get('a_code')
        try:
            application = Application.objects.get(aCode=a_code)
            # application = Application.objects.get(aCode=a_code)
            context = {'application': application}
        except Application.DoesNotExist:
            context = {'error_message': 'Application not found.'}
    else:
        context = {}
    return render(request, 'app/index.html', context)

def select_environment(request):
    if request.method == 'GET' and 'a_code' in request.GET:
        a_code = request.GET.get('a_code')
        try:
            application = Application.objects.get(aCode=a_code)
            # application = Application.objects.get(aCode=a_code)
            environments = application.environment_set.all()
            context = {'environments': environments, 'application': application}
        except Application.DoesNotExist:
            context = {'error_message': 'Application not found.'}
    else:
        context = {'error_message': 'No A-Code provided.'}
    return render(request, 'app/select_environment.html', context)

def open_svg(request):
    if request.method == 'GET' and 'a_code' in request.GET and 'environment' in request.GET:
        a_code = request.GET.get('a_code')
        environment_id = request.GET.get('environment')
        environment = Environment.objects.get(env_id = environment_id)
        environment_name = environment.name
        
        # Assuming your SVG files are stored in the specified directory
        svg_file_path = f"c:/Users/EXU552/exported_diagrams/{a_code}/{environment_name}.svg"

        # Check if the SVG file exists
        if os.path.exists(svg_file_path):
            # Read the contents of the SVG file
            with open(svg_file_path, 'r') as svg_file:
                svg_content = svg_file.read()

                # Return the SVG file content as the response
            return HttpResponse(svg_content, content_type='image/svg+xml')
            # return HttpResponse("svg_file_path : " + svg_file_path)
        else:
            # Return 404 Not Found if the SVG file doesn't exist
            return HttpResponseNotFound("SVG file not found. The svg file path is : " + svg_file_path)
    else:
        # Return 400 Bad Request if A-Code or environment not provided
        return HttpResponseBadRequest("A-Code or environment not provided.")
