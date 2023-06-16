from django import forms

from .models import InquiryMessage

class InquiryMessageForm(forms.ModelForm):
    class Meta:
        model = InquiryMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder' : 'Write here!'
            })
        }