from django.contrib.auth.models import User
from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.core.files.images import get_image_dimensions
from models import Profile


class RegistrationExtendedForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'website', 'bio', 'phone', 'city', 'country', 'organization')


class UserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)

        def clean(self):
            avatar = self.cleaned_data['photo']

            try:
                w, h = get_image_dimensions(avatar)

                #validate dimensions
                max_width = max_height = 400
                if w > max_width or h > max_height:
                    raise forms.ValidationError(
                        u'Please use an image that is %s x %s pixels or smaller.' % (max_width, max_height))

                #validate content type
                main, sub = avatar.content_type.split('/')
                if not (main == 'image' and sub in ['jpeg', 'jpeg', 'gif', 'png']):
                    raise forms.ValidationError(u'Please use a JPEG, GIF or PNG image.')

                #validate file size
                if len(avatar) > (20 * 1024):
                    raise forms.ValidationError(u'Avatar file size may not exceed 20k.')

            except AttributeError:
                """
                Handles case when we are updating the user profile
                and do not supply a new avatar
                """
                pass

            return avatar


class UseEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

