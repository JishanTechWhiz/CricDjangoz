from rest_framework import serializers
from .models import *

# Serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=User
        fields=['id', 'FirstName', 'LastName','Password','Username', 'Email', 'Contact_no', 'Dob', 'Batting_style', 'Bowling_style', 'Role']


    def validate(self, data):
        username = data.get('Username')
        email = data.get('Email')


        # Check if username is already in use
        if User.objects.filter(Username=username).exists():
            raise serializers.ValidationError("Username is already in use.")

        # Check if email is already in use
        if User.objects.filter(Email=email).exists():
            raise serializers.ValidationError("Email is already in use.")



        return data



        

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    Players = serializers.SlugRelatedField(many=True, slug_field='Username', queryset=User.objects.all())
    #Players = serializers.SerializerMethodField()
    class Meta:
        model=Team
        fields = ['id', 'Team_name', 'Captain_name', 'Players']
        #fields="__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        players_data = []
        for player in instance.Players.all():
            user_data = {'Username': player.Username, 'Role': player.Role}  # Assuming 'Username' and 'Role' are fields in the User model
            players_data.append(user_data)
        representation['Players'] = players_data
        return representation
        
   

   






class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'



class GroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ground
        fields = '__all__'



class boxGroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = boxGround
        fields = ['id','groundName','Location','groundTime','Price','isAvailable','rating','phone','boxImg']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'ground', 'date', 'time_slot', 'status', 'price']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class ScorecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scorecard
        fields = '__all__'


class ScorerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchScorerDetail
        fields = '__all__'

        

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'



class PointTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentPointTable
        fields = '__all__'

class TourTeamSerializer(serializers.ModelSerializer):
    Players = serializers.SlugRelatedField(many=True, slug_field='Username', queryset=User.objects.all())
    #Players = serializers.SerializerMethodField()
    class Meta:
        model = TourTeam
        fields = ['id','tournamentId' ,'Team_name','Captain_name', 'Players']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        players_data = []
        for player in instance.Players.all():
            user_data = {'Username': player.Username, 'Role': player.Role}  # Assuming 'Username' and 'Role' are fields in the User model
            players_data.append(user_data)
        representation['Players'] = players_data
        return representation
    # def get_Players(self, obj):
    #     # Retrieve players for the team
    #     players = obj.Players.all()
    #     return players


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    


   