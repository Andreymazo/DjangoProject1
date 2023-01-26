from django.urls import path
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from config import settings
from catalog.views import products, contact_us, crab1

#, contacts, hello,
app_name = CatalogConfig.name

urlpatterns = [
    # path('', hello, name='home'),#WRONG
    path('contact_us/crab1/', crab1, name='crab1'),
    path('contact_us', contact_us, name='contacts'),
    path('', products, name='home'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# in template <img ... src="{{key.image.url}}" ... >