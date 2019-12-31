from django.db import models


# Create your models here.
class RoomType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.DecimalField(decimal_places=0, max_digits=4)
    roomType = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="roomType", blank=True, null=True)

    def __str__(self):
        return str(self.number)


class RatingCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Rating(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room", blank=True, null=True)
    score = models.DecimalField(decimal_places=0, max_digits=1)
    ratingCategory = models.ForeignKey(RatingCategory, on_delete=models.CASCADE, related_name="ratingCategory", blank=True, null=True)
