from django.shortcuts import render

import faker
import calendar
from datetime import date
from django.views import View

from django.template.response import TemplateResponse




class Journal(View):
    def get(self, request):
        fake = faker.Faker()
        cal = calendar.Calendar()
        day = date.today()
        month_days = [day for day, week in cal.itermonthdays2(day.year, day.month) if day != 0 and week != 6]
        names = [fake.name for _ in range(len(month_days))]
        context = {
            "month": month_days,
            "names": names,
        }
        return TemplateResponse(request, "templ.html", context)
