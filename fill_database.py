import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'jobs.settings'
django.setup()

from data import specialties, jobs, companies
from junior.models import Specialty, Vacancy, Company


def fil_specialties():
    for specialty in specialties:
        Specialty.objects.create(
            code=specialty.get('code'),
            title=specialty.get('title'),
        )


def fill_jobs():
    for job in jobs:
        Vacancy.objects.create(
            id=job.get('id'),
            title=job.get('title'),
            specialty=Specialty.objects.get(code=job.get('specialty')),
            company=Company.objects.get(id=job.get('company')),
            skills=job.get('skills'),
            description=job.get('description'),
            salary_min=float(job.get('salary_from')),
            salary_max=float(job.get('salary_to')),
            published_at=job.get('posted'),
        )


def fill_companies():
    for company in companies:
        Company.objects.create(
            id=company.get('id'),
            name=company.get('title'),
            location=company.get('location'),
            description=company.get('description'),
            employee_count=company.get('employee_count'),
        )


if __name__ == '__main__':
    fil_specialties()
    fill_companies()
    fill_jobs()
