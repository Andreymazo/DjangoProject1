from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.forms import inlineformset_factory
from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse

from catalog.forms import SubjectForm, ProductForm, RecordForm
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


class CategoryListView(ListView):
    model = Category
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/Product_list.html'


Record.views_controller = 0


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
    form_class = SubjectForm
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/Product_list.html'


class ProductCreateView(CreateView):
    model = Product
    # form_class = ProductForm
    # form_class = SubjectForm
    fields = ('product_name', 'product_description', 'preview', 'price_per_unit', 'category')
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/product_form.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/product_form.html'

    # def clean(self):
    #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #     if request.method == 'POST':
    #         form = ProductForm(request.POST, request.FILES)
    #         for i in t:
    #             if Product.product_name == i:
    #                 raise ValueError('Nedopustimie slova')
    #         if not form.is_valid():
    #
    #         else:
    #             return Product.product_name


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/Product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/product_confirm_delete.html'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def change_status(request, pk):
    # product_item = Product.objects.filter(pk=pk).first()
    # if product_item:
    #     if ... is None:
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.status == Product.STATUS_ACTIV:
        product_item.status = Product.STATUS_INACTIV
    else:
        product_item.status = Product.STATUS_ACTIV
    product_item.save()
    return redirect(reverse('catalog:Product_list'))


# class ProductCreateFormMore():
#     def context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         FormSet = inlineformset_factory(self.model, Product, form=ProductForm, extra=1)
#         if self.request.method == 'POST':
#             formset = FormSet(self.request.POST, instance=self.object)
#         else:
#             formset = FormSet(instance=self.object)
#         context_data['formset']=formset
#         return context_data


class RecordListView(ListView):
    model = Record


class RecordCreateView(CreateView):
    # Sozdaem zapis "Record form"
    model = Record
    form_class = RecordForm
    # fields = '__all__'
    # fields = ('title', 'content', 'id_public')
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
