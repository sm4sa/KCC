from django.shortcuts import render

from KCCIC.authentication_decorators import admin_required


@admin_required()
def testing_page(request):
    return render(request, 'KCCIC/testing_page.html')