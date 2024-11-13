from home.models import AricleList
from itertools import zip_longest

def combined_data_context(request):
    articlelist = AricleList.objects.all()

    return {
        'articlelist': articlelist

    }
