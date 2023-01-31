from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from catalog.forms import ProductForm
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

Record.views_controller=0
def products(request):

    g = Record.views_controller
    g += 1
    context = {
     'object_list': Product.objects.all(),
        'g': g

    }
    return render(request, 'catalog/products.html', context)
# def vivod_postatusu(request):
#     context = {'object_list': Record.objects.all()}
#     return render(request, 'catalog/record_detail.html', context)

def contact_us(request):
    if request.method == 'POST':
        # print(request.method)
        # print(request.POST.get('name'))
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
# def vivod_postatusu(request):
#     if Record.id_public != True:
#         context = {'object_list': Record.objects.all()}
#         return render(request, 'catalog/record_detail.html', context)
######################################
def get_counter(requests):
    if requests.method == "GET":
        g = Record.views_controller
        g += 1
        print(f'CounteEEEEr  {g}')
        context = {"g": g}
        return render(requests, context)
class ProductListView(ListView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/Product_list.html'
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    fields = ('product_name', 'product_description', 'preview', 'price_per_unit', 'category')
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/Product_list.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/product_form.html'

class RecordListView(ListView):
    model = Record

class RecordCreateView(CreateView):
    # Sozdaem zapis
    model = Record
    # fields = '__all__'
    fields = ('title', 'content', 'id_public')
    success_url = reverse_lazy('catalog:Rec_list')
# def rec_lst_img(request):
#     if request.method=='POST' and request.FILES:
#         file=request.FILES['myfile1']
#         fs=FileSystemStorage()
#         filename=fs.save(file.name, file)
#         file_url = fs.url(filename)
#         return render(request, 'Rec_list.html', {
#             'file_url':file_url
#         })
class RecordUpdateView(UpdateView):
        # Sozdaem zapis
    model = Record
        # fields = '__all__'
    fields = ('title', 'content', 'image', 'id_public')
    success_url = reverse_lazy('catalog:Rec_list')
class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('catalog:Rec_list')
class RecordDetailView(DetailView):
    model = Record
    template_name = 'catalog/record_detail.html'

# def vivod_postatusu(request):
#     context = {'object_list': Record.objects.all()}
#     return render(request, 'catalog/record_detail.html', context)

    # def show_record(request, post_id):
    #     post = get_object_or_404(Record, pk=id)
    #
    #     context = {
    #         'title': post.title
    #     }
    #
    #     return render(request, 'catalog/record_detail.html', context=context)