from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

# Define the custom 404 view correctly
def custom_404_view(request, exception):
    return render(request, "404.html", status=404)

# Set handler404 at the module level, NOT inside urlpatterns
handler404 = custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('profile/', include('profiles.urls')),
]

# Serve media files in development (only when DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

