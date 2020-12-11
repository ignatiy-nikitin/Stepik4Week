import random

from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views import View

from junior.forms import ApplicationForm, SearchVacanciesForm
from junior.models import Vacancy, Company, Specialty


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.all().annotate(vacancy_count=Count('vacancies'))
        companies = Company.objects.all().annotate(vacancies_count=Count('vacancies'))
        context = {
            'form': SearchVacanciesForm,
            'skills': get_random_skills(),
            'specialties': specialties,
            'companies': companies,
        }
        return render(request, 'junior/index.html', context)


class VacanciesListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'form': SearchVacanciesForm,
            'vacancies': vacancies,
            'count': vacancies.count(),
        }
        return render(request, 'junior/vacancies.html', context)


class SpecializationView(View):
    def get(self, request, category):
        vacancies = Vacancy.objects.filter(specialty__code=category)
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'category_name': Specialty.objects.get(code=category),
            'vacancies': vacancies,
            'count': vacancies.count(),
        }
        return render(request, 'junior/vacancies.html', context)


class CompanyCardView(View):
    def get(self, request, id):
        company = Company.objects.get(pk=id)
        vacancies = Vacancy.objects.filter(company__name=company.name)
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'company': company,
            'vacancies': vacancies,
            'count': vacancies.count(),
        }
        return render(request, 'junior/company.html', context)


class VacancyView(View):
    def get(self, request, id):
        vacancy = get_object_or_404(Vacancy, id=id)
        vacancy.skills = vacancy.skills.split(', ')
        context = {
            'vacancy': vacancy,
        }
        if request.user.is_authenticated:
            context['form'] = ApplicationForm
        return render(request, 'junior/vacancy.html', context)

    def post(self, request, id):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = Vacancy.objects.get(id=id)
            application.user = User.objects.get(id=request.user.id)
            application.save()
            return render(request, 'junior/sent.html', {'vacancy_id': id})


class SearchView(View):
    def get(self, request):
        query = request.GET.get('query')
        vacancies = get_vacancies_by_search_query(query)
        divide_skills(vacancies)
        context = {
            'form': SearchVacanciesForm,
            'vacancies': vacancies,
            'count': len(vacancies),
        }
        return render(request, 'junior/vacancies.html', context)

    def post(self, request, query):
        vacancies = Vacancy.objects.filter(
            title__icontains=query
        )
        context = {
            'form': SearchVacanciesForm(request.POST),
            'vacancies': vacancies,
        }
        return render(request, 'junior/vacancies.html', context)


def custom_handler_404(request, exception):
    return render(request, 'junior/error_404.html')


def custom_handler_500(request):
    return render(request, 'junior/error_500.html')


def get_random_skills(count=5):
    skills_ = Vacancy.objects.values('skills')
    skills = set()
    for item in skills_:
        for s in item['skills'].split(', '):
            skills.add(s)
    return random.sample(skills, count)


def divide_skills(vacancies):
    for vacancy in vacancies:
        vacancy.skills = vacancy.skills.split(', ')


def get_vacancies_by_search_query(query):
    # фрагмент кода, который должен был быть использован:
    # Vacancy.objects.filter(Q(title__icontains=query) | Q(skills__icontains=query) | Q(description__icontains=query))
    # из-за специфики sqllite данный код не работает, подробней здесь: https://www.sqlite.org/faq.html#q18
    vacancies = []
    for vacancy in Vacancy.objects.all():
        for item in [vacancy.title, vacancy.skills, vacancy.description]:
            if query.upper() in item.upper():
                vacancies.append(vacancy)
                break
    return vacancies
