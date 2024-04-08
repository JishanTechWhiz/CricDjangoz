from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework.response import Response

from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import *
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import ensure_csrf_cookie

from django.contrib.auth import authenticate, login
from rest_framework import status




from django.http import *
import json

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request,"index.html")

def homePage(request):
    return render(request,"home.html")

def register(request):
    return render(request,"register.html")

def loginView(request):
    return render(request,"login.html")



# Viewsets
#serializers for api
#Example :-
#Login url :- http://127.0.0.1:8000/users/login/
#Register url :- http://127.0.0.1:8000/users/register/

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     @action(detail=False, methods=['post'])
#     def register(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({'message': 'User created successfully'})
#
#
#
#         # try:
#         #     user = User.objects.get(Username=username,Password=password)
#
#         #     if user is not None:
#         #         return Response({'message': 'Login successful'})
#         #     else:
#         #         return Response({'message': 'Login Fails'})
#         # except User.DoesNotExist:
#         #     return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#
#
#         # if user and check_password(password, user.Password):
#         #     return Response({'message': 'Login successful'})
#         # else:
#         #     return Response({'message': 'Login Fail'})
#
#
#
#
#
#
#         # user = authenticate(request, username=username, password=password)
#
#         # if user is not None:
#         #     return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#         # else:
#         #     return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#
#
#
#     #users/1/team
#     # @action(detail=True, methods=['get'])
#     # def team(self, request, pk=None):
#     #     usrs = User.objects.get(id=pk)
#     #     plyrs=Team.obejcts.filter(players=usrs)
#     #     plyrsSerializer=TeamSerializer(plyrs,many=True,context={'request':request})
#     #     return Response(plyrsSerializer.data)3
        



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @csrf_exempt
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'message': 'User created successfully'})
    
    @csrf_exempt
    @action(detail=False, methods=['post'])
    def login_check(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            f_uname = data.get('username', None)
            f_pwd = data.get('password', None)

            try:
                student = User.objects.get(Username=f_uname)
                flag = check_password(f_pwd, student.Password)
                if flag:
                    details = {
                        'user': student.Username,
                        'pass': student.Password
                    }
                    return JsonResponse({'data': details}, status=200)
                else:
                    return JsonResponse({'error': 'Invalid credentials'}, status=400)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        else:
            return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

   
    

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    # function = register_data()




class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    # function = register_data()


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class GroundViewSet(viewsets.ModelViewSet):
    queryset = Ground.objects.all()
    serializer_class = GroundSerializer


class boxGroundViewSet(viewsets.ModelViewSet):
    queryset = boxGround.objects.all()
    serializer_class = boxGroundSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class ScorecardViewSet(viewsets.ModelViewSet):
    queryset = Scorecard.objects.all()
    serializer_class = ScorecardSerializer

class ScorerDetailViewSet(viewsets.ModelViewSet):
    queryset = MatchScorerDetail.objects.all()
    serializer_class = ScorerDetailSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class PointTableViewSet(viewsets.ModelViewSet):
    queryset = TournamentPointTable.objects.all()
    serializer_class = PointTableSerializer
    
class TourTeamViewSet(viewsets.ModelViewSet):
    queryset = TourTeam.objects.all()
    serializer_class = TourTeamSerializer





