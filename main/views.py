from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406422922',
        'name': 'Rifqy Pradipta Kurniawan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)