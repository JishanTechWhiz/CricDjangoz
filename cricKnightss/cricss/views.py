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


@csrf_exempt
@action(detail=False, methods=['post'])
def update_profile(request, user_id):
    try:
        user_instance = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    if request.method == 'POST':
        # Get the data from the request
        data = request.POST  # Assuming form data is sent in a POST request
        # Update the user instance with the received data
        user_instance.FirstName = data.get('FirstName', user_instance.FirstName)
        user_instance.LastName = data.get('LastName', user_instance.LastName)
        user_instance.Email = data.get('Email', user_instance.Email)
        user_instance.Contact_no = data.get('Contact_no', user_instance.Contact_no)
        user_instance.Dob = data.get('Dob', user_instance.Dob)
        user_instance.Batting_style = data.get('Batting_style', user_instance.Batting_style)
        user_instance.Bowling_style = data.get('Bowling_style', user_instance.Bowling_style)
        user_instance.Role = data.get('Role', user_instance.Role)
        # Save the updated user instance
        user_instance.save()
        return JsonResponse({'message': 'Profile updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)       
        
@csrf_exempt
@action(detail=False, methods=['post'])
def login_check(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        f_uname = data.get('username', None)
        f_pwd = data.get('password', None)
        print(f_pwd)
        try:
            student = User.objects.get(Username=f_uname)
            print("Comes")
            flag = check_password(f_pwd, student.Password)
            if flag: 
                details = {
                        'id':student.id,
                        'firstname':student.FirstName,
                        'lastname':student.LastName,
                        'username': student.Username,
                        'password': student.Password,
                        'email':student.Email,
                        'phone':student.Contact_no,
                        'dob':student.Dob,
                        'battingstyle':student.Batting_style,
                        'bowlingstyle':student.Bowling_style,
                        
                    }
                return JsonResponse({'data': details}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


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
    def update_profile(self, request):
        # Get the user object
        user = request.user
        # Check if the user is authenticated
        if user.is_authenticated:
            # Get the data from the request
            data = request.data
            # Get the user instance
            user_instance = User.objects.get(id=user.id)
            # Update the user instance with the received data
            user_instance.FirstName = data.get('first_name', user_instance.FirstName)
            user_instance.LastName = data.get('last_name', user_instance.LastName)
            user_instance.Email = data.get('email', user_instance.Email)
            user_instance.Contact_no = data.get('contact_no', user_instance.Contact_no)
            user_instance.Dob = data.get('dob', user_instance.Dob)
            user_instance.Batting_style = data.get('batting_style', user_instance.Batting_style)
            user_instance.Bowling_style = data.get('bowling_style', user_instance.Bowling_style)
            user_instance.Role = data.get('role', user_instance.Role)
            # Save the updated user instance
            user_instance.save()
            return JsonResponse({'message': 'Profile updated successfully'}, status=200)
        else:
            return JsonResponse({'error': 'User not authenticated'}, status=401)    

    
    @csrf_exempt
    @action(detail=False, methods=['post'])
    def login_check(request):
        if request.method == 'POST':
           data = json.loads(request.body)
           print(data)   
           f_uname = data.get('username', None)
           f_pwd = data.get('password', None)
           print(f_pwd)
           try:
               student = User.objects.get(Username=f_uname)
               print("Comes")
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
    
class BookingListView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@csrf_exempt
def check_time_slot_availability(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = data.get('date')
        time_slot = data.get('time_slot')
        ground_id = data.get('ground_id')  # Identifier for the specific cricket ground
        # Check if there's any booking with the same date, time slot, and ground identifier
        existing_bookings = Booking.objects.filter(date=date, time_slot=time_slot, ground_id=ground_id)
        if existing_bookings.exists():
            return JsonResponse({"available": False, "message": "Time slot not available"})
        else:
            return JsonResponse({"available": True, "message": "Time slot available"})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def book_ground(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        date = data.get('date')
        time_slot = data.get('time_slot')
        price = data.get('price')
        ground_id = data.get('ground_id')
        # Check if the time slot is available
        existing_bookings = Booking.objects.filter(date=date, time_slot=time_slot, ground_id=ground_id)
        if existing_bookings.exists():
            return JsonResponse({"error": "Time slot not available"}, status=400)
        else:
            # Create a new booking
            booking = Booking.objects.create(user_id=user_id, date=date, time_slot=time_slot, price=price, ground_id=ground_id)
            return JsonResponse({"message": "Booking successful", "booking_id": booking.id})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def get_booking_details(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        booking_details = {
            "user_id": booking.user_id,
            "date": booking.date,
            "time_slot": booking.time_slot,
            "status": booking.status,
            "price": booking.price,
            "ground_id": booking.ground_id
        }
        return JsonResponse(booking_details)
    except Booking.DoesNotExist:
        return JsonResponse({"error": "Booking not found"}, status=404)



