from django.contrib import admin
from .models import *
# Register your models here.

class a1(admin.ModelAdmin):
    list_display = ['id','FirstName','LastName','Username','Password','Email','Contact_no','Dob','Batting_style','Bowling_style','Role']


class a2(admin.ModelAdmin):
    list_display = ['id','Team_name', 'custom_display_method']

    def custom_display_method(self, obj):
        # Access the many-to-many field 'Players'
        return ', '.join([player.Username for player in obj.Players.all()])
class a3(admin.ModelAdmin):
    list_display = ['id','groundName','Location','Price','isAvailable']

class a4(admin.ModelAdmin):
    list_display = ['id','groundName','Location','groundTime','Price','isAvailable','organizername','rating','phone','boxImg']

class a5(admin.ModelAdmin):
    list_display = ['id','team_id','team_id2','ground_id','match_type','noOfOvers','overPerBowler','city','dateTime','ballType','pitchType']

class a6(admin.ModelAdmin):
    list_display = ['id','cityName']

class a7(admin.ModelAdmin):
    list_display = ['id','matchId','tossWin','battingTeam','bowlingTeam','firstInnings_totalRuns','firstInnings_totalFours','firstInnings_totalSixs','firstInnings_totalWicket','secondInnings_totalRuns','secondInnings_totalFours','secondInnings_totalSixs','secondInnings_totalWicket','winnerTeam']

class a8(admin.ModelAdmin):
    list_display = ['id','tournamentName','city','groundId','organizerName','organizerNum','organizerEmail','startDate','endDate','tournamentCat','ballType','pitchType','description']

class a9(admin.ModelAdmin):
    list_display = ['id','tournamentId','teamName1','matches1','win1','loss1','tie1','point1','teamName2','matches2','win2','loss2','tie2','point2','teamName3','matches3','win3','loss3','tie3','point3','teamName4','matches4','win4','loss4','tie4','point4','teamName5','matches5','win5','loss5','tie5','point5','teamName6','matches6','win6','loss6','tie6','point6']

class a10(admin.ModelAdmin):
    list_display = ['id','tournamentId','Team_name', 'custom_display_method']
    
    def custom_display_method(self, obj):
        # Access the many-to-many field 'Players'
        return ', '.join([player.Username for player in obj.Players.all()])

    # def custom_display_method(self, obj):
    #     # Access the many-to-many field 'Players'
    #     return ', '.join([team.Team_name for team in obj.team.all()])
        
    
class a11(admin.ModelAdmin):
    list_display = ['id','match','tossWin','battingTeam','bowlingTeam','firstInnings_totalRuns','firstInnings_totalFours','firstInnings_totalSixs','firstInnings_totalWicket','secondInnings_totalRuns','secondInnings_totalFours','secondInnings_totalSixs','secondInnings_totalWicket','winnerTeam']



admin.site.register(User,a1)
admin.site.register(Team,a2)
admin.site.register(Ground,a3)
admin.site.register(boxGround,a4)
admin.site.register(Match,a5)
admin.site.register(City,a6)
admin.site.register(MatchScorerDetail,a7)
admin.site.register(Tournament,a8)
admin.site.register(TournamentPointTable,a9)
admin.site.register(TourTeam, a10)
admin.site.register(Scorecard, a11)

#list_display=['name of function'] for image


#Username : jishan7562
#Password : 123456