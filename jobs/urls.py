"""jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from jobs import settings
from junior.views.authorization.authorization import LogInView, RegisterView, LogOutView
from junior.views.account import MyCompanyView, MyCompanyCreateView, MyCompanyVacanciesView, MyCompanyVacancyView, \
    MyCompanyVacancyCreate, ResumeView, ResumeCreateView
from junior.views.public import MainView, VacanciesListView, SpecializationView, CompanyCardView, VacancyView, \
    SearchView, custom_handler_404, custom_handler_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesListView.as_view()),
    path('vacancies/cat/<str:category>/', SpecializationView.as_view()),
    path('companies/<int:id>/', CompanyCardView.as_view()),
    path('vacancies/<int:id>/', VacancyView.as_view()),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/create/', MyCompanyCreateView.as_view(), name='create_company'),
    path('mycompany/vacancies/', MyCompanyVacanciesView.as_view()),
    path('mycompany/vacancies/<int:vacancy_id>/', MyCompanyVacancyView.as_view(), name='vacancy_edit'),
    path('mycompany/vacancy/create/', MyCompanyVacancyCreate.as_view(), name='vacancy_create'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('resume/create/', ResumeCreateView.as_view()),
    path('search/', SearchView.as_view()),
    path('login/', LogInView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogOutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = custom_handler_404
handler500 = custom_handler_500
