from django.db import models
from django.forms import ValidationError
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password

from django.contrib.auth.hashers import make_password, check_password as check_password_hashed


groundType = (
    ('0','Select Ground Type'),
    ('1', 'Box Cricket'),
    ('2', 'Open Ground')
)

groundType = (
    ('0','Select Ground Type'),
    ('1', 'Box Cricket'),
    ('2', 'Open Ground')
)
ballType=(
    ('0','Select Ball Type'),
    ('1','Tennis'),
    ('2','Leather'),
    ('3','Others')
)
pitchType=(
    ('0','Select Pitch Type'),
    ('1','Rough'),
    ('2','Cement'),
    ('3','Turf'),
    ('4','AstroTurf'),
    ('5','Matting')
)

groundTiming = (
    ('0','Select Time'),
    ('1', '8AM - 9AM'),
    ('2', '9AM - 10AM'),
    ('3', '10AM - 11AM'),
    ('4', '11AM - 12PM'),
    ('5', '3PM - 4PM'),
    ('6', '4PM - 5PM'),
    ('7', '6PM - 7PM'),
    ('8', '7PM - 8PM'),
    ('9', '9PM - 10PM'),
    ('10', '10PM - 11PM'),
    ('11', '11PM - 12AM'),
    ('12', '12AM - 1AM'),
    ('13', '1AM - 2AM')
)


#models.py

class User(models.Model):
    FirstName = models.CharField(max_length=25, null=False)
    LastName = models.CharField(max_length=25, null=False)
    Username = models.CharField(max_length=25, null=False,unique=True)
    Password = models.CharField(max_length=254, null=False)
    Email = models.EmailField(null=False,unique=True)
    Contact_no = models.IntegerField(null=False)
    Dob = models.DateField(null=True,blank=True)
    Batting_style = models.CharField(max_length=20, null=True,blank=True)
    Bowling_style = models.CharField(max_length=20, null=True,blank=True)
    Role = models.CharField(max_length=20, null=True,blank=True)
    def __str__(self):
        # return f"{self.id} - {self.Username}"
        return str(self.id)
    
#any validation change is create and update in def save function
    def save(self, *args, **kwargs):
        # Use make_password to hash the password before saving
        self.Password = make_password(self.Password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Check if the raw password matches the hashed password stored in the database
        return check_password_hashed(raw_password, self.Password)

    


# class User(models.Model):
#     FirstName = models.CharField(max_length=25, null=False)
#     LastName = models.CharField(max_length=25, null=False)
#     Username = models.CharField(max_length=25, null=False,unique=True)
#     Password = models.CharField(max_length=254, null=False)
#     Email = models.EmailField(null=False,unique=True)
#     Contact_no = models.IntegerField(null=False)
#     Dob = models.DateField(null=True,blank=True)
#     Batting_style = models.CharField(max_length=20, null=True,blank=True)
#     Bowling_style = models.CharField(max_length=20, null=True,blank=True)
#     Role = models.CharField(max_length=20, null=True,blank=True)
#
#     def __str__(self):
#         return self.Username

class City(models.Model):
    cityName=models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.cityName


class Team(models.Model):
    Team_name = models.CharField(max_length=50, null=False,default="")
    Captain_name = models.CharField(max_length=25, null=False)
    Players = models.ManyToManyField(User)

    def __str__(self):
        return self.Team_name


# class groundInfo(models.Model):
#     startTime=models.TimeField(null=False)
#     endTime=models.TimeField(null=False)
#     groundType = models.CharField(choices=groundType, max_length=12, null=False)

#     price=models.IntegerField(null=False)

class Ground(models.Model):
    groundName = models.CharField(max_length=100, null=False)
    Location = models.CharField(max_length=255, null=False)
    Price = models.IntegerField(default=1500, null=False)
    isAvailable = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.groundName

class boxGround(models.Model):
    groundName = models.CharField(max_length=100, null=False)
    Location = models.CharField(max_length=255, null=False)
    groundTime = models.CharField(choices=groundTiming, max_length=20, null=False)
    Price = models.IntegerField(default=600, null=False)
    isAvailable = models.BooleanField(default=True, null=False)
    organizername = models.CharField(max_length=25, null=False,default='')
    rating = models.CharField(max_length=4, null=True, blank=True) 
    phone = models.CharField(max_length=12, null=True, blank=True)
    boxImg=models.ImageField(upload_to='photos',null=True)

    def __str__(self):
        return self.groundName

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ground = models.ForeignKey(boxGround, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='pending')  # Status: pending, confirmed, cancelled
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.time_slot}"


class Match(models.Model):
    userId = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True,related_name='home_matches')
    team_id2 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True,related_name='away_matches')
    ground_id = models.ForeignKey(Ground, on_delete=models.SET_NULL, null=True)
    match_type = models.CharField(max_length=50, null=False)
    noOfOvers = models.IntegerField(null=False)
    overPerBowler = models.IntegerField(null=False)
    city = models.ForeignKey(City,null=True,on_delete=models.SET_NULL)
    dateTime = models.DateTimeField(null=False)
    ballType = models.CharField(choices=ballType,max_length=30, null=False)
    pitchType = models.CharField(choices=pitchType,max_length=30, null=False)
    def __str__(self):
        return str(self.id)
    
class Scorecard(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE, related_name='scorecard')
    tossWin = models.CharField(max_length=50)
    battingTeam = models.CharField(max_length=50)
    bowlingTeam = models.CharField(max_length=50)
    firstInnings_totalRuns = models.IntegerField()
    firstInnings_totalFours = models.IntegerField()
    firstInnings_totalSixs = models.IntegerField()
    firstInnings_totalWicket = models.IntegerField()
    secondInnings_totalRuns = models.IntegerField()
    secondInnings_totalFours = models.IntegerField()
    secondInnings_totalSixs = models.IntegerField()
    secondInnings_totalWicket = models.IntegerField()
    winnerTeam = models.CharField(max_length=50)



# class ScorerDetail(models.Model):
#     matchId = models.ForeignKey(Match, null=True,on_delete=models.SET_NULL)
#     teamId = models.ForeignKey(Team, null=True,on_delete=models.SET_NULL)
#     tossWin = models.CharField(max_length=30, null=False)
#     battingTeam = models.CharField(max_length=30, null=False)
#     bowlingTeam = models.CharField(max_length=30, null=False)
#     firstInnings_totalRuns= models.IntegerField(null=False)
#     firstInnings_totalFours = models.IntegerField(null=False)
#     firstInnings_totalSixs = models.IntegerField(null=False)
#     firstInnings_totalWicket = models.IntegerField(null=False)
#     secondInnings_totalRuns= models.IntegerField(null=False)
#     secondInnings_totalFours = models.IntegerField(null=False)
#     secondInnings_totalSixs = models.IntegerField(null=False)
#     secondInnings_totalWicket = models.IntegerField(null=False)
#     winnerTeam = models.CharField(max_length=30, null=False)
    
class MatchScorerDetail(models.Model):
    matchId = models.ForeignKey(Match, null=True,on_delete=models.SET_NULL)
    tossWin = models.CharField(max_length=30, null=False)
    battingTeam = models.CharField(max_length=30, null=False)
    bowlingTeam = models.CharField(max_length=30, null=False)
    firstInnings_totalRuns= models.IntegerField(null=False)
    firstInnings_totalFours = models.IntegerField(null=False)
    firstInnings_totalSixs = models.IntegerField(null=False)
    firstInnings_totalWicket = models.IntegerField(null=False)
    secondInnings_totalRuns= models.IntegerField(null=False)
    secondInnings_totalFours = models.IntegerField(null=False)
    secondInnings_totalSixs = models.IntegerField(null=False)
    secondInnings_totalWicket = models.IntegerField(null=False)
    winnerTeam = models.CharField(max_length=30, null=False)


# class ScoreCard(models.Model):
#     scoreId = models.ForeignKey(ScorerDetail, null=True)


class Tournament(models.Model):
    #bannerImg=models.ImageField(upload_to='photos',null=True)
    userId = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    tournamentName = models.CharField(max_length=50, null=False)
    city = models.ForeignKey(City,null=True,on_delete=models.SET_NULL)
    groundId = models.ForeignKey(Ground, null=True,on_delete=models.SET_NULL)
    organizerName = models.CharField(max_length=30, null=False)
    organizerNum = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    organizerEmail = models.EmailField(null=False)
    startDate = models.DateField(null=False)
    endDate = models.DateField(null=False)
    tournamentCat = models.CharField(max_length=40, null=False)
    ballType = models.CharField(choices=ballType,max_length=30, null=False)
    pitchType = models.CharField(choices=pitchType,max_length=30, null=False)
    description = models.CharField(max_length=255, null=False)
    def __str__(self):
        return str(self.id)

    # def __str__(self):
    #     return self.tournamentName

    def f1(self):
        return mark_safe('<img src="{}" width="100%">'.format(self.bannerImg.url))
    
class TourTeam(models.Model):
    tournamentId = models.ForeignKey(Tournament, null=True,on_delete=models.SET_NULL)
    Team_name = models.CharField(max_length=50, null=False,default="")
    Captain_name = models.CharField(max_length=25, null=False,default='')
    Players = models.ManyToManyField(User)

    def __str__(self):
        return self.Team_name

    
class TournamentPointTable(models.Model):
    tournamentId = models.ForeignKey(Tournament, null=True,on_delete=models.SET_NULL)
    teamName1 = models.CharField(max_length=30, null=False)
    matches1= models.IntegerField(null=False)
    win1 = models.IntegerField(null=False)
    loss1 = models.IntegerField(null=False)
    tie1 = models.IntegerField(null=False)
    point1 = models.IntegerField(null=False)
    teamName2 = models.CharField(max_length=30, null=False)
    matches2= models.IntegerField(null=False)
    win2 = models.IntegerField(null=False)
    loss2 = models.IntegerField(null=False)
    tie2 = models.IntegerField(null=False)
    point2 = models.IntegerField(null=False)
    teamName3 = models.CharField(max_length=30, null=False)
    matches3= models.IntegerField(null=False)
    win3 = models.IntegerField(null=False)
    loss3 = models.IntegerField(null=False)
    tie3 = models.IntegerField(null=False)
    point3 = models.IntegerField(null=False)
    teamName4 = models.CharField(max_length=30, null=False)
    matches4= models.IntegerField(null=False)
    win4 = models.IntegerField(null=False)
    loss4 = models.IntegerField(null=False)
    tie4 = models.IntegerField(null=False)
    point4 = models.IntegerField(null=False)
    teamName5 = models.CharField(max_length=30, null=False)
    matches5= models.IntegerField(null=False)
    win5 = models.IntegerField(null=False)
    loss5 = models.IntegerField(null=False)
    tie5 = models.IntegerField(null=False)
    point5 = models.IntegerField(null=False)
    teamName6 = models.CharField(max_length=30, null=False)
    matches6= models.IntegerField(null=False)
    win6 = models.IntegerField(null=False)
    loss6 = models.IntegerField(null=False)
    tie6 = models.IntegerField(null=False)
    point6 = models.IntegerField(null=False)