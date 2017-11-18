from django.shortcuts import render,redirect
from .models import User
import requests, json

from rest_framework import generics
from .serializers import UserSerializer

from rest_framework_mongoengine import viewsets
# Create your views here.

def index(request):

    check = False
    user = User.objects()
    logged_out = False
    if request.method == "POST":

        try:
            if request.POST['act'] == "logout":
                logged_out = True
                print("loggedzz")
        except KeyError:
            logged_out = False
            print("tangina")

        if logged_out:
            request.session['user_id'] = None
            print("logged out")
        else:
            usernm = request.POST['user']
            passwd = request.POST['pass']
            a = User.objects.filter(usrnm=usernm, pss=passwd)

            print(usernm, passwd)
            if a:
                print("PAZZUCC")
                id = str(a[0].id)
                request.session['user_id'] = id
                return render(request, 'homes/home.html', {'check': check, 'users': user,'userz': a[0]})
            else:
                print("Niggato")
                check = True
    return render(request, 'homes/index.html',{'check':check,'users':user})
def home(request):
    return render(request, 'homes/home.html',)

def signup(request):
    if request.method == "POST":
        print(request.POST['usrnm'])
        user = User.objects.create(usrnm=request.POST['usrnm'],
                                   pss=request.POST['pss'],
                                   name=request.POST['name'],
                                   email=request.POST['email'],
                                   githuburl=request.POST['githuburl'],
                                   bio=request.POST['bio'])
        user.save()
        return render(request, 'homes/index.html',{'check':False})
    return render(request, 'homes/signup.html', {'check': False})
def users(request, usrnm):
    user = User.objects.get(usrnm=usrnm)

    response = requests.get('https://api.github.com/users/'+user.githuburl)
    resp2 = requests.get('http://127.0.0.1:8000/homes/usrs/'+usrnm)
    json_data = json.loads(response.text)
    json2 = json.loads(resp2.text)


    print(json2)
    return render(request, 'homes/user.html', {'git_info':json_data})

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = self.queryset.all()
        parent_id = self.request.query_params.get('parent_id', None)

        if parent_id is not None:
            queryset = queryset.filter(parent_id=parent_id)

        return queryset

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "usrnm"

    def get_queryset(self):
        return self.queryset.all()

