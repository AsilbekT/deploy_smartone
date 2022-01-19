from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contact.models import FeedBack

class FeedBackForm(forms.ModelForm):
    # name = forms.CharField(label='Your name', max_length=100)
    # surname = forms.CharField(label='Your surname', max_length=100)
    # comment = forms.CharField(widget=forms.Textarea)
    # text = forms.CharField(widget=forms.Textarea
    # (attrs={'class': 'text_area_form',
    #         'id': 'some_id'}))
    class Meta:
        model = FeedBack
        fields = "__all__"

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user