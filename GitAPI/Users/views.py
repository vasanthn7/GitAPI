from django.shortcuts import render
from rest_framework import viewsets
from .models import users
from .serializers import user_serializers
import requests

from .models import users
# Create your views here.

class user_view(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = user_serializers


def home(request):
    user = {}
    args = {}
    if 'username' in request.GET:
        username = request.GET['username']
        # print("-------------request-------------")
        # print(request)
        #
        # print("-----------request.GET-----------")
        # print(request.GET)
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        # print("-------response.status_code------")
        # print (response.status_code)
        if (response.status_code == 200):                                           #Check if valid Username
            user = response.json()
            # print("-------------user-------------")
            # print(user, type(user))
            # print(user['login'])

            args = {'status':200, 'user': user}
            # print("-------------response-------------")
            # print(response)
            # print("-------------response.json-------------")
            # print(response.json())
            if(users.objects.filter(user=request.GET['username']).exists()):        #Check if entry exists
                print("user exist")
                user_update = users.objects.get(user=request.GET['username'])
                user_update.user = user['login']
                user_update.name = user['name']
                user_update.email = user['email']
                user_update.public_repo = user['public_repos']
                user_update.created = user['created_at']
                user_update.followers = user['followers']
                user_update.following = user['following']
                user_update.save()

            else:
                print("user doesn't exist")
                new_user = users()
                new_user.user = user['login']
                new_user.name = user['name']
                new_user.email = user['email']
                new_user.public_repo = user['public_repos']
                new_user.created = user['created_at']
                new_user.followers = user['followers']
                new_user.following = user['following']
                new_user.save()

        elif response.status_code == 404:
            args = {'status':404,}
    return render(request, 'Users/home.html', args)


# user = models.CharField(max_length=128, primary_key=True)
# name = models.CharField(max_length=200, null=True, blank=True)
# email = models.EmailField(max_length=100,blank=True, null= True)
# public_repo = models.IntegerField()
# created = models.DateTimeField(default=None, null=False)
# followers = models.IntegerField(default=None, null=False)
# following = models.IntegerField(default=None, null=False)
