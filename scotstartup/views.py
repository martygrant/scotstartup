from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from scotstartup.models import Company, Event
from scotstartup.forms import CompanyForm, UserForm, UserProfileForm, EventForm

def index(request):
    company_list = Company.objects.all()
    
    context_dict = {}

    context_dict['companies'] = company_list

    recentCompanies = Company.objects.order_by("-created")[:5]
    context_dict['recentCompanies'] = recentCompanies

    featuredCompanies = Company.objects.order_by("-created")[:5]
    context_dict['featuredCompanies'] = recentCompanies

    events = Event.objects.order_by("-created")[:5]
    context_dict['events'] = events

    return render(request, 'scotstartup/index.html', context_dict)

def companies(request):
    company_list = Company.objects.all()
    
    context_dict = {}

    context_dict['companies'] = company_list

    return render(request, 'scotstartup/companies.html', context_dict)

def company(request, company_name_slug):
    context_dict = {}

    try:
        company = Company.objects.get(slug=company_name_slug)
        context_dict['company_name'] = company.name
        context_dict['company_description'] = company.description
        context_dict['company'] = company
    except Company.DoesNotExist:
        pass

    return render(request, 'scotstartup/company.html', context_dict)
            
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            
            return index(request)
        else:
            print form.errors
    else:
        form = CompanyForm()
        
    return render(request, 'scotstartup/add_company.html', {'form': form})


def event(request, event_name_slug):
    context_dict = {}

    try:
        event = Event.objects.get(slug=event_name_slug)
        context_dict['event_name'] = event.name
        context_dict['event_description'] = event.description
        context_dict['event'] = event
    except event.DoesNotExist:
        pass

    return render(request, 'scotstartup/event.html', context_dict)


def events(request):
    event_list = Event.objects.all()
    
    context_dict = {}

    context_dict['events'] = event_list

    return render(request, 'scotstartup/events.html', context_dict)


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            
            return index(request)
        else:
            print form.errors
    else:
        form = EventForm()
        
    return render(request, 'scotstartup/add_event.html', {'form': form})


def about(request):
    return render(request, 'scotstartup/about.html')


def news(request):
    return render(request, 'scotstartup/news.html')