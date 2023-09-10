from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Aulia Rizqi Hidayatunnisa',
        'class': 'PBP B',
        'app_name': 'shopping_product',
    }

    return render(request, "main.html", context)
