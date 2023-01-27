from django.urls import path
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from config import settings
from catalog.views import products, contact_us, RecordListView, RecordCreateView, \
    RecordUpdateView, RecordDeleteView, RecordDetailView  # , RecordCreateView, crab1,

#, contacts, hello,
app_name = CatalogConfig.name

urlpatterns = [
    # path('', hello, name='home'),#WRONG
    path('', products, name='home'),
    path('contact_us/', contact_us, name='contacts'),

    # path('contact_us/crab1/', crab1, name='crab1'),#Созданы 2 одинаковые ветки
    # для тренировки, через класс RecordListView и черерз функцию render in file view
    path('Rec_list/', RecordListView.as_view(), name='Rec_list'),
    path('create/', RecordCreateView.as_view(), name='create'),
    path('update/<int:pk>/', RecordUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', RecordDetailView.as_view(), name='detail')
              ] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# in template <img ... src="{{key.image.url}}" ... >