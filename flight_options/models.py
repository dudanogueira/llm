from django.db import models

class FlightOption(models.Model):

    def __unicode__(self):
        return "Flight Option #%s for %s" % (self.id, self.speaker)

    speaker = models.ForeignKey('speakers.Speaker')
    route_description = models.TextField(blank=True)
    # arrival
    arrival_date = models.DateTimeField(blank=True, null=True)
    arrival_observations = models.TextField(blank=True)
    # departure
    departure_date = models.DateTimeField(blank=True, null=True)
    departure_observations = models.TextField(blank=True)
    # sent
    sent = models.BooleanField(default=False)
    sent_timestamp = models.DateTimeField(blank=True, null=True)
    # seen
    seen = models.BooleanField(default=False)
    seen_timestamp = models.DateTimeField(blank=True, null=True)
    # approved
    approved = models.BooleanField(default=False)
    approved_timestamp = models.DateTimeField(blank=True, null=True)
    # approved
    rejected = models.BooleanField(default=False)
    rejected_timestamp = models.DateTimeField(blank=True, null=True)
    rejected_reason = models.TextField(blank=True)
    # meta
    criado = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Criado")
    atualizado = models.DateTimeField(blank=True, auto_now=True, verbose_name="Atualizado")
    