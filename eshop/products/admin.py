from django.contrib import admin
from .models import Product

# Register your models here.


admin.site.register(Product)


from django.contrib import admin
from .models import Director, Movie, Review

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'duration')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'text')
