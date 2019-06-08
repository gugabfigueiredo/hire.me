from django.contrib import admin

# Register your models here.
from url_app.models import Urls
# Register your models here.


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('alias', 'httpurl', 'pub_date', 'count')
    ordering = ('-pub_date',)


admin.site.register(Urls, UrlsAdmin)  # Register the Urls model with UrlsAdmin options
