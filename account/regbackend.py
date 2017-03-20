from account.forms import RegistrationExtendedForm


def user_created(sender, user, request, **kwargs):
    """
    Called via signals when user registers. Creates different profiles and
    associations
    """
    form = RegistrationExtendedForm(request.POST)
    # Update first and last name for user
    user.first_name=form.data['first_name']
    user.last_name=form.data['last_name']
    user.save()

from registration.signals import user_registered
user_registered.connect(user_created)