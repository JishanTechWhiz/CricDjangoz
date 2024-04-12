
from . import views
from django.urls import path,include
from rest_framework import routers
from . views import *
from django.conf.urls.static import static
from django.conf import settings

# Register viewsets with router

routers=routers.DefaultRouter()
routers.register(r'users',UserViewSet)
routers.register(r'team',TeamViewSet)
routers.register(r'cities', CityViewSet)
routers.register(r'grounds', GroundViewSet)
routers.register(r'boxgrounds', boxGroundViewSet)
routers.register(r'matches', MatchViewSet)
routers.register(r'scorerdetails', ScorerDetailViewSet)
routers.register(r'tournaments', TournamentViewSet)
routers.register(r'pointtables', PointTableViewSet)
routers.register(r'tournamentTeams', TourTeamViewSet)
routers.register(r'Scorecards', ScorecardViewSet)
routers.register(r'booking', BookingListView)

urlpatterns = [
    path('',include(routers.urls)),
    path('register/', UserViewSet.as_view({'post': 'register'}), name='register'),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    #path('api/user/update_profile//', UserViewSet.as_view({'post': 'update_profile'}), name='update_profile'),
    path('login_check/', login_check, name='login'),
    path('update_profile/<int:user_id>/', update_profile, name='update_profile'),
    #
    path('check-time-slot-availability/', views.check_time_slot_availability),
    path('book-ground/', views.book_ground),
    path('booking-details/<int:booking_id>/', views.get_booking_details),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)