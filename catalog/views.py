from django.shortcuts import render

def hello(request):
    if request.method == 'POST':
        # print(request.method)
        print(request.POST.get('name'))
        print(request.POST.get('e-mail'))
        print(request.POST.get('message'))
    # return render(request, 'catalog/index.html')
    return render(request, 'catalog/index.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')
