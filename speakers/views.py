from django.shortcuts import render

from speakers.models import Speaker

from django.forms import ModelForm

from django.core.exceptions import ValidationError

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
            updated_speaker = speaker_form.save()
        else:
            speaker = Speaker.objects.get(uuid=uuid)
    else:
        speaker_form = SpeakerForm(instance=speaker)

    context = {
        'speaker': speaker,
        'speaker_form': speaker_form,
        'show_first_time_modal': show_first_time_modal
        
    }
    return render(request, 'speaker.html', context,)
    