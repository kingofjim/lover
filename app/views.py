from django.core.exceptions import ObjectDoesNotExist
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from app.func import save_player_image, get_file_type
from .models import Players, Voter
from datetime import datetime

# Create your views here.

@require_http_methods('GET')
def index(request):
    return render(request, 'index.html', {})

@csrf_exempt
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

@require_http_methods(['GET', 'POST'])
def vote(request):
    if (request.method == 'GET'):

        players_data = Players.objects.filter(active=True).values('id', 'nickname', 'votes', 'fb', 'ig', 'intro',  'youtube', 'video', 'photo_half', 'photo_whole').order_by('-votes')
        return render(request, 'vote.html', {'players': players_data})

    elif (request.method == 'POST'):
        user_id = request.POST['user_id']
        vote = request.POST['vote']
        access_toke = request.POST['access_token']
        now = datetime.now()
        # print(now.strftime('%Y-%m-%d %H:%M:%S'))
        today = now.strftime('%Y-%m-%d')
        end_time = datetime.strptime('2020-08-06 00:00:00', '%Y-%m-%d %H:%M:%S')
        # print(today)
        if now > end_time:
            return HttpResponse("The event is end.")
        try:
            voter = Voter.objects.filter(date=today, user_id=user_id).get()
        except ObjectDoesNotExist:
            voter = Voter(date=today, user_id=user_id)
        # print(_isUnique(voter, vote))
        if voter.vote_5:
           return HttpResponse(json.dumps({"voted": 5}), content_type="application/json")
        elif(_isUnique(voter, vote)):
            if not voter.vote_1:
                voter.vote_1 = vote
                voted = 1
            elif not voter.vote_2:
                voter.vote_2 = vote
                voted = 2
            elif not voter.vote_3:
                voter.vote_3 = vote
                voted = 3
            elif not voter.vote_4:
                voter.vote_4 = vote
                voted = 4
            else:
                voter.vote_5 = vote
                voted = 5
            voter.access_toke = access_toke
            player = Players.objects.get(pk=vote)
            player.votes += 1
            voter.save()
            player.save()
            return HttpResponse(json.dumps({"voted": voted}), content_type="application/json")
        else:
            return HttpResponse("duplicated")

    return HttpResponse()

def _isUnique(voter, vote):
    theList = []
    for i in range(1, 6):
        val = getattr(voter, "vote_"+str(i))
        if val:
            theList.append(val)
    return False if int(vote) in theList else True

def profile(request, id):
    return HttpResponse()