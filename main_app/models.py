from django.db import models

class Artist(models.Model):
    monikr = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    artist_statement = models.CharField(max_length=250)

    def __str__(self):
        return self.monikr
    


# a = Artist(monikr='sleepy icarus', artist_statement='comfort in loneliness', genre='vaporwave', pronouns='she/her', medium='digital photography')
# a.save()