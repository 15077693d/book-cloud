from django.contrib import admin

from catalog.models import *


# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'date_of_death')
    fields = ['name', ('date_of_birth', 'date_of_death')]


# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('display_book', 'status', 'due_back',)
    fieldsets = (
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
         ('Role', {
            'fields': ('borrower', 'holder', 'bookers')
        }),
        (
            'Record',{
                'fields': ('book', 'history')
            }
        )
    )

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('status', 'receiver', 'requester')


admin.site.register(Language)
admin.site.register(Genre)
