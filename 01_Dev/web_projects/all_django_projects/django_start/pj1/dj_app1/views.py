from django.shortcuts import render
from .models import Series, Session

# Create your views here.
def home(request):
    all_series = Series.objects.all()
    all_sessions = Session.objects.all()
    return render(request, './dj_app1/home.html',{'all_series': all_series, 'all_sessions': all_sessions})

def sessions_list(request):
    all_sessions = Session.objects.all()
    return render(request, './dj_app1/series_list.html',{'all_sessions': all_sessions})

def series_detail(request, series_id):
    series = Series.objects.get(id=series_id)
    sessions = Session.objects.filter(series=series)
    return render(request, './dj_app1/series_detail.html', {'series': series, 'sessions': sessions})
