import json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import YTDownloaderForm


def ytDownloader_view(request):
    if request.method == 'POST':
        form = YTDownloaderForm(request.POST)
        if form.is_valid():
            # Convert form data to dictionary
            form_data = {key: value for key, value in form.cleaned_data.items()}

            # Convert dictionary to JSON string
            json_data = json.dumps(form_data)

            # Make a POST request to the Flask endpoint
            url = 'http://127.0.0.1:8080/ytDownloader'
            headers = {'Content-Type': 'application/json'}  # Specify JSON content type
            response = requests.post(url, data=json_data, headers=headers)

            # Handle the response as needed
            return HttpResponse(response.text)
    else:
        form = YTDownloaderForm()

    return render(request, 'ytDownloader.html', {'form': form})
