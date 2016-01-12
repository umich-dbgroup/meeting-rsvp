from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return "{} ({})".format(self.name, self.date)

class Rsvp(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=255, verbose_name='Your name')
    vegetarian = models.BooleanField(default=False, verbose_name='Want vegetarian food')

    def __str__(self):
        return "{} -- {} (vegetarian={})".format(self.event, self.name, 'yes' if self.vegetarian else 'no')
