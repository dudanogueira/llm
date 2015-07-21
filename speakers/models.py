from django.db import models
import uuid
from django.core.urlresolvers import reverse

DOCUMENT_TYPE_CHOICES = (
    ('cpf', 'Brazilian CPF'),
    ('passport', 'Passport'),
)

class Speaker(models.Model):

    def __unicode__(self):

        return "%s (%s)" % (self.complete_name, self.email)

    def get_absolute_url(self):
        return reverse("speaker", args=[self.uuid])

    def open_flight_options(self):
        return self.flightoption_set.filter(rejected=False)

    email = models.EmailField()
    complete_name = models.CharField(blank=True, max_length=100)
    nickname = models.CharField(blank=True, max_length=100)
    document = models.CharField(blank=True, max_length=100)
    document_type = models.CharField(blank=True, max_length=100, choices=DOCUMENT_TYPE_CHOICES)
    contact_phones = models.TextField(blank=True)
    origin_city_state = models.CharField(blank=True, max_length=100)
    require_flight = models.BooleanField(default=False)
    flight_arranged = models.BooleanField(default=False)
    waiting_flight = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)