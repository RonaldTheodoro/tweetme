from django.contrib import admin

from . import models, forms

class TweetAdmin(admin.ModelAdmin):
    form = forms.TweetForm


admin.site.register(models.Tweet)
