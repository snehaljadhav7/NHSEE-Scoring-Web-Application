from django.shortcuts import render
from scoring.views import import_data
from django.contrib import messages

def import_file(request):
    if request.method=='POST':
        try:
            file = request.FILES['document']
            import_data(file)
            messages.success(request, "Data imported successfully")
        except Exception:
            messages.success(request, "Please choose file first")
    return render(request, 'import.html')
