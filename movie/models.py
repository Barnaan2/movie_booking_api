from django.db import models



class Cast(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True,null=True)
    about = models.CharField(max_length=200,null =True)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.name)

 

 
class Crew(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True,null=True,upload_to='movie/crew/')
    about = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.name)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=80)
    relase_date = models.DateField()
    poster = models.ImageField(blank=True,null=True,upload_to='movie/poster/')
    cover = models.ImageField(blank=True,null=True,upload_to='movie/cover/')
    cast = models.ManyToManyField(Cast, blank=True)
    crew = models.ManyToManyField(Crew, blank =True)
    trailer_link = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.title)