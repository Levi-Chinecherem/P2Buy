from django import forms
from .models import Feedback
from django.contrib.auth.models import User  # Import the built-in User model

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FeedbackForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.filter(pk=user.pk), initial=user.pk)

         # Add Bootstrap classes to form fields
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        