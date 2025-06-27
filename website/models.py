from django.db import models

class SURVEY_LINKS(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    category= models.CharField(max_length=255)
    

    def __str__(self):
        return self.name
    

from django.contrib import admin
@admin.register(SURVEY_LINKS)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'link','category')
    # add search_fields, list_filter, inlines, etc. as needed
