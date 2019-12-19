from django.db import models


# Create your models here.
class RoomType(models.Model):
    name = models.CharField(max_length=250)


class Room(models.Model):
    number = models.DecimalField(max_digits=4)
    roomType = models.ForeignKey(RoomType)


class RatingCategory(models.Model):
    name = models.CharField(max_length=250)


class Player(models.Model):
    account = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="account", unique=True)
    displayName = models.CharField(max_length=250)
    credibility = models.DecimalField(max_digits=1)


class Rating(models.Model):
    player = models.ForeignKey(Player)
    room = models.ForeignKey(Room)
    score = models.DecimalField(max_digits=1)


ratingCategory = models.ForeignKey(RatingCategory)
