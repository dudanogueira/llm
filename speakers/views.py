import datetime
from django.shortcuts import render

from speakers.models import Speaker
from flight_options.models import FlightOption

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from django.contrib import messages

class SpeakerForm(ModelForm):
    
    def clean(self):
        cleaned_data = super(SpeakerForm, self).clean()
        document = cleaned_data.get("document")
        document_type = cleaned_data.get("document_type")
        origin_city_state = cleaned_data.get("origin_city_state")
        if self.instance.require_flight:
            if not document or not document_type or not origin_city_state:
                raise ValidationError('Error! We need some additional information in order to buy you flight tickets. Please, fill bellow.')
                
    
    def __init__(self, *args, **kwargs):
        super(SpeakerForm, self).__init__(*args, **kwargs)
        self.fields['complete_name'].required = True
        if self.instance.require_flight:
            self.fields['document'].required = True
            self.fields['document_type'].required = True
            self.fields['origin_city_state'].required = True
            
    class Meta:
        model = Speaker
        fields = "complete_name", 'nickname', 'document', 'document_type', 'contact_phones', 'origin_city_state'

def home(request):
    context = {}
    return render(request, 'index.html', context,)

def speaker(request, uuid):
    speaker = Speaker.objects.get(uuid=uuid)
    if not speaker.complete_name:
        show_first_time_modal = True
    else:
        show_first_time_modal = False
    if request.POST:
        speaker_form = SpeakerForm(request.POST, instance=speaker)
        if speaker_form.is_valid():
            updated_speaker = speaker_form.save(commit=False)
            updated_speaker.waiting_flight = True
            updated_speaker.save()
            return redirect(reverse("speaker", args=[speaker.uuid]))
        else:
            speaker = Speaker.objects.get(uuid=uuid)
            show_first_time_modal = False
    else:
        speaker_form = SpeakerForm(instance=speaker)

    context = {
        'speaker': speaker,
        'speaker_form': speaker_form,
        'show_first_time_modal': show_first_time_modal
    }
    return render(request, 'speaker.html', context,)

def speaker_flight(request, uuid, flight_id):
    flight = FlightOption.objects.get(speaker__uuid=uuid, pk=flight_id)
    if not flight.seen:
        flight.seen_timestamp = datetime.datetime.now()
        flight.seen = True
        flight.save()
    context = {
        'speaker': flight.speaker,
        'flight': flight
    }
    return render(request, 'speaker_flight.html', context,)

def speaker_flight_decision(request, uuid, flight_id, decision):
    flight = FlightOption.objects.get(speaker__uuid=uuid, pk=flight_id)
    if decision == "accept":
        messages.success(request, "Success! Flight Option ID %s Accepted" % flight.pk)
        flight.approved=True
        flight.approved_timestamp = datetime.datetime.now()
        flight.save()
    else:
        messages.error(request, "Flight Option ID %s Rejected"  % flight.pk)
        flight.rejected=True
        flight.rejected_timestamp = datetime.datetime.now()
        flight.save()
    return redirect(reverse("speaker", args=[flight.speaker.uuid]))

def manager(request):
    speakers_no_name = Speaker.objects.filter(complete_name__in=(None, ''))
    flightoptions_not_rejected_not_seen = FlightOption.objects.filter(rejected=False, seen=False)
    context = {
        'speakers_no_name': speakers_no_name,
        'flightoptions_not_rejected_not_seen': flightoptions_not_rejected_not_seen
    }
    return render(request, 'manager.html', context,)

