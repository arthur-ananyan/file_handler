from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import shortuuid
from .tasks import handle_file
from .models import File


def upload(request):
    if request.method == 'POST':
        file_extension = request.FILES['file'].name.rsplit('.', 1)[-1]
        request.FILES['file'].name = shortuuid.uuid() + "." + file_extension
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file_name = request.FILES['file'].name
            file = File.objects.get(file=file_name)
            file_url = file.file.url
            handle_file.delay(file_url)

            return HttpResponse('Your file has been successfully uploaded!')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
