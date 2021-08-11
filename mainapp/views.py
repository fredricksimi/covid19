from django.shortcuts import render, redirect, get_object_or_404
from commentsapp.forms import CommentForm, DoctorEmailForm
from django.http import JsonResponse
from django.contrib import messages
from commentsapp.models import Comment, DoctorEmails
from datetime import date, datetime
import requests
import json
from datetime import date

def home_view(request):
    user_comments = Comment.objects.all().order_by('-timestamp')
    url = "https://covid-193.p.rapidapi.com/statistics?country=kenya"
    headers = {
    'x-rapidapi-key': "6672acff71msha2668ee10af537bp1245a2jsn31635e6b6758",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    mylist = []
    querystring = {"country": "kenya"}
    response = requests.request("GET", url, headers=headers, params=querystring).text
    our_json_data = json.loads(response)
    
    country = our_json_data['response'][0]['country']
    population = our_json_data['response'][0]['population']
    new_cases = our_json_data['response'][0]['cases']['new']
    active_cases = our_json_data['response'][0]['cases']['active']
    critical = our_json_data['response'][0]['cases']['critical']
    recovered = our_json_data['response'][0]['cases']['recovered']
    new_deaths = our_json_data['response'][0]['deaths']['new']
    total_deaths = our_json_data['response'][0]['deaths']['total']
    tests = our_json_data['response'][0]['tests']['total']
    day = our_json_data['response'][0]['day']
    day_object = datetime.fromisoformat(day)
    new_day_object = day_object.strftime("%d %b %Y")
    time = our_json_data['response'][0]['time']
    datetime_object = datetime.fromisoformat(time)
    new_datetime_object = datetime_object.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            data = form.cleaned_data
            comment_created = Comment.objects.create(**data, user=request.user)
            messages.success(request, 'Your Comment was added successfully!')
            return redirect('mainapp:homepage')
    else:
        form = CommentForm()
    
    doctorform = DoctorEmailForm(request.POST or None)
    if request.method == 'POST':
        if doctorform.is_valid():
            data = doctorform.cleaned_data
            comment_created = DoctorEmails.objects.create(**data, sender=request.user)
            messages.success(request, 'Your Note was sent Successfully!')
            return redirect('mainapp:homepage')
    else:
        doctorform = DoctorEmailForm()
    
    context = {
        "country":country,
        "population":population,
        "new_cases":new_cases,
        "active_cases":active_cases,
        "critical":critical,
        "recovered":recovered,
        "new_deaths":new_deaths,
        "total_deaths":total_deaths,
        "tests":tests,
        "day":new_day_object,
        "time":new_datetime_object,
        "form":form,
        "doctorform":doctorform,
        "usercomments":user_comments,
    }
    return render(request, 'mainapp/index.html', context)

def view_emails(request):
    emails = DoctorEmails.objects.all().order_by('-timestamp')
    context = {'emails':emails}
    return render(request, 'mainapp/emails.html', context)

def delete_email(request, id):
    the_email = get_object_or_404(DoctorEmails, id=id)
    if request.method == 'POST':
        the_email.delete()
        return redirect('mainapp:emails')
    context = {
        'the_email':the_email
    }
    return render(request, 'mainapp/delete-email.html', context)

def seven_days(request):
    return render(request, 'mainapp/seven.html')

def history_view(request):
    our_list = []
    converted_list = []
    our_file = '/home/freddy/covid19/final.json'
    with open(our_file) as obj:
        data = json.load(obj)
        for entry in data:
            new_dict = {
                "total_cases":entry['total_cases'],
                "total_deaths": entry['total_deaths'],
                "recovered": entry['recovered'],
                "day":entry['day'],
            }
            converted_list.append(new_dict)
    return JsonResponse(converted_list, safe=False)
