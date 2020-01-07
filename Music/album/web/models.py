from django.db import models

# Create your models here.
class Album(models.Model):
	albums_id = models.AutoField(primary_key=True)
	albums_name = models.CharField(max_length=200)
	albums_image = models.ImageField(upload_to="image/", default="")
	albums_year = models.DateField()

	def __str__(self):
		return self.albums_name


class Song(models.Model):
	
	
	songs_title_name = models.CharField( max_length=200)
	songs_image = models.ImageField(upload_to="image/", default="")
	songs_release_date_year = models.DateTimeField()
	songs_singer_name = models.CharField(max_length=200)

	def __str__(self):
		return self.songs_title_name
		return self.songs_singer_name


class Login(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=10)

	def __str__(self):
		return self.username
		return self.password
	


class Register(models.Model):
	username = models.CharField(max_length=50)
	last_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=254)
	password = models.ForeignKey(Login, on_delete=models.CASCADE)


	def __str__(self):
		return self.username
		return self.password
	

