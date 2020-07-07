from django.contrib import admin
from django.urls import path
from app.controller import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-auth/', AuthToken.as_view(), name='token'),
    path('user/', FetchUserView.as_view()),
    path('register/', RegisterToken.as_view()),
    path('offers/', ListOffer.as_view()),
    path('create-offer/', CreateOffer.as_view()),
    path('offer/<pk>', UpdateOffer.as_view()),
    path('user-edit/<pk>', RetrieveUpdateDestroyAPIView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
