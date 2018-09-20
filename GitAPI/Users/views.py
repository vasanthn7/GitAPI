from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import users
from .serializers import user_serializers
import requests
import django_filters
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from decouple import config

class user_all(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = user_serializers
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('user', 'created', 'email')
    search_fields = ('user', 'created', 'email')

    def get_queryset(self):
        return users.objects.all()

def home(request):
    user = {}
    args = {}
    if 'username' in request.GET:
        username = request.GET['username']

        # Git OAuth token
        # Generate Personal access tokens on github and replace values
        username_auth = config('username_auth')
        token_auth = config('token_auth')

        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url, auth=(username_auth, token_auth))
        print (response.json())
        if (response.status_code == 200):                                           #Check if valid Username
            user = response.json()
            args = {'status':200, 'user': user}

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
