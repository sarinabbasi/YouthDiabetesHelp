from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SubscribeModel,  HomeBanner, OurMission, OurMissionImage, AricleList
from article.models import Article
from itertools import zip_longest
import ghasedakpack


def home(request):
    banner = HomeBanner.objects.last()
    missionimage = OurMissionImage.objects.last()
    ourmission = OurMission.objects.all()

    if request.method == 'POST':
        number = request.POST.get('phone')
        try:
            SubscribeModel.objects.get(number=number)
        except SubscribeModel.DoesNotExist:
            if len(number) == 11 and number.isdigit():
                SubscribeModel.objects.create(number=number)

    return render(request, 'home/home.html', {
        'banner': banner,
        'mission': missionimage,
        'missions': ourmission,
    })



def send_messages_to_subscribers(message_text):
    subscribers = SubscribeModel.objects.al
    sms = ghasedakpack.Ghasedak("815fd62100f7a0e93271a74e3d418ec6818758cc8a4dbee1edf38a2868da0334")

    for subscriber in subscribers:
        response = sms.send({'message': message_text, 'receptor': subscriber.number, 'linenumber': '10008566'})

        if response:
            print(f"Message successfully sent to {subscriber.number}")
        else:
            print(f"Failed to send the message to {subscriber.number}")
