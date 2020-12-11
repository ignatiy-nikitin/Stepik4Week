from django.contrib import admin
from junior.models import Vacancy, Specialty, Company, Application


class VacancyAdmin(admin.ModelAdmin):
    fields = ('title', 'specialty', 'company', 'skills', 'description', 'salary_min', 'salary_max', 'published_at')


class SpecialityAdmin(admin.ModelAdmin):
    fields = ('code', 'title', 'picture')


class CompanyAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'logo', 'description', 'employee_count', 'owner')


class ApplicationAdmin(admin.ModelAdmin):
    fields = ('written_username', 'written_phone', 'written_cover_letter', 'vacancy', 'user')


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Specialty, SpecialityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Application, ApplicationAdmin)
