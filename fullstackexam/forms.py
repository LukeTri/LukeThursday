from django import forms

from .models import Rating

class CreateRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('room', 'score', 'ratingCategory')

    def __init__(self, *args, **kwargs):
        super(CreateRatingForm, self).__init__(*args, **kwargs)