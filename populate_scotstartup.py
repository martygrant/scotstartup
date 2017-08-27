import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scotstartup_project.settings')

import django
django.setup()

from scotstartup.models import Company

def populate():
    addCompany("Tesla", "Electrical consumer vehicles.");

    addCompany("Blizzard", "Computer games developer.");

    for company in Company.objects.all():
        print "- {0} -".format(str(company))



def addCompany(name, description):
    company = Company.objects.get_or_create(name=name, description=description)[0]
    company.save()

    return company

if __name__ == '__main__':
    print "Starting ScotStartup population script..."
    populate()
