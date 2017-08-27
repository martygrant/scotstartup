from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from scotstartup.models import Company
from scotstartup.forms import CompanyForm, UserForm, UserProfileForm

def index(request):
    company_list = Company.objects.all()
    
    context_dict = {'companies': company_list}

    return render(request, 'scotstartup/index.html', context_dict)

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
            
