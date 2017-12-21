from django.db import models

# Create your models here.
TYPE_CHOICES = (
    ('Duplex', 'Duplex'),
    ('Apartment', 'Apartment'),
    ('Bungalow', 'Bungalow'),
    ('BQ', 'BQ')
)


class Properties(models.Model):
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    price = models.PositiveIntegerField()
    bed_no = models.IntegerField(verbose_name= 'bedroom')
    sitting_no = models.IntegerField(verbose_name='sitting_room')
    toilet_no = models.IntegerField(verbose_name='toilet')
    house_img = models.ImageField(upload_to='static')
    sitting_room_img = models.ImageField(upload_to='static')
    bedroom_img = models.ImageField(upload_to='static')
    bathroom_img = models.ImageField(upload_to='static')

    def __str__(self):
        return str(self.bed_no) + ' Bedroom ' + self.type + ' at ' + self.address + ', ' + self.city + ', ' + self.state