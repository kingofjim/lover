from django.shortcuts import render
from django.http import HttpResponse
from app.func import save_player_image, get_file_type
from .models import Players

# Create your views here.

def index(request):
    print('haha')
    return render(request, 'index.html', {})

def apply(request):
    if(request.method == 'GET'):
        return render(request, 'apply.html', {})

    elif(request.method == 'POST'):
        # print(request.POST)

        player = Players()
        player.name = request.POST['name']
        player.birthday = request.POST['birthday']
        player.nickname = request.POST['nickname']
        player.email = request.POST['email']
        player.phone = request.POST['phone']
        player.line = request.POST['line']
        player.ig = request.POST['ig']
        player.fb = request.POST['fb']
        player.save()

        files = request.FILES
        player.photo_whole = save_player_image(files['photo-whole'], player.id, 'photo-whole' + get_file_type(files['photo-whole'].content_type))
        player.photo_half = save_player_image(files['photo-half'], player.id, 'photo-half' + get_file_type(files['photo-half'].content_type))
        player.save()

        return HttpResponse('Ok')