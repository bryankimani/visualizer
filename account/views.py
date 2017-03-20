from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.forms import UserProfileForm
from models import Profile
# Create your views here.


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')

    editprofile = Profile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'website': editprofile.website, 'photo': editprofile.photo})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=editprofile)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('editprofile', args=[user.username]))
        else:
            print(form.errors)
    else:
        form = UserProfileForm()
    return render(request, 'account/editprofile.html',
                  {'editprofile': editprofile,
                   'selecteduser': user, 'form': form})
