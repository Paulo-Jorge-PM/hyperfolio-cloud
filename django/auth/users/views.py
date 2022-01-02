from django.http import HttpResponse, HttpRequest

from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Profile

class IndexView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'latest_profiles'

    def get_queryset(self):
        """Return the last five published questions."""
        return Profile.objects.order_by('-dateBirth')[:5]

#def index(request):
#    latest_profiles_list = Profile.objects.order_by('-dateBirth')[:5]
#    output = ', '.join([q.fullName for q in latest_profiles_list])
#    return HttpResponse(output)

class DetailView(generic.DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'

def profile(request, user_id):
    if request.method == 'GET':
        #HttpRequest.META
        return HttpResponse(user_id)
    elif request.method == 'POST':
        return HttpResponse("post")
