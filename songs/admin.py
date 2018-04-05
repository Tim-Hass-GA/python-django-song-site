from django.contrib import admin
from .models import Artist, Album, Song

## two ways to do this
## stacked inline way
## modular view on top of one another
class SongInLine(admin.StackedInline):
## tabular inline
## compact view condensed on the same line
# class SongInLine(admin.TabularInline):
    model = Song
    ## how to display blank fields at the bottom of the stack
    ## to add new things......
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInLine]

## defind the way the view looks
class AlbumInLine(admin.StackedInline):
    model = Album
    extra = 3

# import the model for the view 
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInLine]


# Register Artist and Album with their custom Admin interfaces
# add all admin views
admin.site.register(Artist, ArtistAdmin)
# update to include the view.....
admin.site.register(Album, AlbumAdmin)

# We haven't customized Song. Register it as itself and take
# Django default admin interface.
admin.site.register(Song)
