from django.shortcuts import render
from . import models


def about_view(request):
    banner = models.BannerImageAbout.objects.last()
    missions = models.Mission.objects.all()
    about = models.AboutUs.objects.last()
    team = models.Team.objects.all()
    return render(request, "about/about-us.html", {"banner" : banner,
                                                   "missions" : missions,
                                                   "about" : about,
                                                   "team": team})