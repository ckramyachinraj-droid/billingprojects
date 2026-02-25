from django.shortcuts import render

def billing_page(request):
    return render(request, 'billing.html')
