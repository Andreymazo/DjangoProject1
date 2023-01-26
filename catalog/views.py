from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from catalog.models import Category, Product, Record


# def hello(request):
#     if request.method == 'POST':
#         # print(request.method)
#         print(request.POST.get('name'))
#         print(request.POST.get('e-mail'))
#         print(request.POST.get('message'))
    # return render(request, 'catalog/index.html')
    # return render(request, 'catalog/index.html')
def category(request):
    context = {
     'object_list': Category.objects.all()

    }
    return render(request, 'catalog/products.html', context)
def products(request):
    context = {
     'object_list': Product.objects.all()

    }
    return render(request, 'catalog/products.html', context)
def contact_us(request):
    if request.method == 'POST':
        # print(request.method)
        print(request.POST.get('name'))
        print(request.POST.get('e-mail'))
        print(request.POST.get('message'))
    return render(request, 'catalog/contact_us.html')
# def crab1(request):
#     context = {
#         'object_list': Record.objects.all()
#
#     }
#     return render(request, 'catalog/crab1.html', context)
# def contacts(request):
#     return render(request, 'catalog/contact_us.html')

class RecordListView(ListView):
    model = Record
class RecordCreateView(CreateView):
    # Sozdaem zapis
    model = Record
    # fields = '__all__'
    fields = ('slug', 'content')
    success_url = reverse_lazy('catalog:Rec_list')

class RecordUpdateView(UpdateView):
        # Sozdaem zapis
    model = Record
        # fields = '__all__'
    fields = ('slug', 'content')
    success_url = reverse_lazy('catalog:Rec_list')
class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('catalog:Rec_list')
class RecordDetailView(DetailView):
    model = Record
    template_name = 'catalog/record_detail.html'