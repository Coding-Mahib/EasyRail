from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Station(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return self.name

class Train(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    train_code = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate a slug when saving the Train object
        self.slug = slugify(f"{self.name}-{self.train_code}")
        super().save(*args, **kwargs)

class TrainStation(TimestampMixin):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

    class Meta:
        ordering = ['arrival_time']

    def __str__(self):
        return f"{self.train} - {self.station}"

# class Ticket(TimestampMixin):
#     train_station = models.ForeignKey(TrainStation, on_delete=models.CASCADE)
#     passenger_name = models.CharField(max_length=100)
#     passenger_age = models.PositiveIntegerField()
#     date_of_travel = models.DateField()

#     def __str__(self):
#         return f"{self.passenger_name} - {self.train_station}"

#     def is_travel_date_expired(self):
#         # Check if the ticket's travel date is expired
#         return self.date_of_travel < timezone.now().date()

#     def get_train(self):
#         # Get the associated train for this ticket
#         return self.train_station.train

#     def get_departure_time(self):
#         # Get the departure time for this ticket's train station
#         return self.train_station.departure_time