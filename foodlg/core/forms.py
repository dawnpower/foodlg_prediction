from django import forms 

class AddPhotoForm(forms.Form):
    file = forms.FileField(label="")
