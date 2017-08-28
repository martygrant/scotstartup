from django import template
from scotstartup.models import Company

register = template.Library()

@register.inclusion_tag('scotstartup/companies.html')
def get_company_list(company=None):
    return {'companies': Company.objects.all(), 'act_company': company}