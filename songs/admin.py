from django.contrib import admin
from .models import Artist, Album, Song

# Register your models here.

# Stacked Inline shows model fields all stacked up on top of
# each other, row by row. Inheriting from the TabularInline
# class shows model fields all in one row across columns.
# The TabularInline class is a great choice when you want to
# show condensed information, like songs on an album.
#
#class SongInline(admin.StackedInline):
class SongInline(admin.TabularInline):
  model = Song
  # "extra" defines how many blank fields appear at the bottom
  # of the list. If you look at an album admin page you'd see
  # all of the songs on the album plus "an extra" two blank
  # spots conveniently there for you to add any more songs.
  extra = 2

class AlbumInline(admin.TabularInline):
  model = Album
  extra = 0

class AlbumAdmin(admin.ModelAdmin):
  inlines = [SongInline]

class ArtistAdmin(admin.ModelAdmin):
  inlines = [AlbumInline]


# Register Artist and Album with their custom Admin interfaces
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)

# We haven't customized Song. Register it as itself and take
# Django default admin interface.
admin.site.register(Song)
