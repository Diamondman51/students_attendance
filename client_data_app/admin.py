from datetime import timedelta
import datetime
from django import forms
from django.contrib import admin
from django.http import HttpRequest

from client_data_app.models import *

# Register your models here.
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

        widgets = {
            'teacher': forms.CheckboxSelectMultiple()
        }


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectForm


class HomeworkAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request: HttpRequest) -> dict[str, str]:
        data = super().get_changeform_initial_data(request)
        d = data.get('till')
        d = datetime.date.today() + timedelta(days=5)
        data['till'] = d
        return data
    
    list_display = ['exercise', 'created_at', 'till']


admin.site.register(Parents)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Curator)
admin.site.register(StudentGroup)
admin.site.register(Student)
admin.site.register(Exercise)
admin.site.register(Homework, HomeworkAdmin)