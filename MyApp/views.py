from django.shortcuts import render
from .forms import Imageform
from .models import ImageModel


# Create your views here.
def home(request):
    if request.method == "POST":
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = Imageform()
    img = ImageModel.objects.all()

    return render(request, 'MyApp/home.html', {'img': img, 'form': form})
