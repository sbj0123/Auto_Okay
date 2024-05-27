from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.forms import MyModelForm

# # Create your views here.
# def index(request):
#     if request.method == 'POST':
#         my_file = request.FILES['file']
#         MyFile.objects.create(my_file=my_file)
#     return render(request, 'main/main.html')

def upload_file(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('karaoke')  # 파일 업로드 성공 시 이동할 URL
    else:
        form = MyModelForm()
    return render(request, 'main/main.html', {'form': form})
