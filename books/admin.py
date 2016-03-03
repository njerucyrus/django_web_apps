from django.contrib import admin
from .models import *

# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = [ 'book_category', 'book_title', 'book_author', 'publisher','copies', 'date_added']
    prepopulated_fields = {'slug': ('book_title',)}
    list_editable = ['copies']
    class Meta:
        model = Book
admin.site.register(Book, BooksAdmin)

class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name', )}
    class Meta:
        model = BookCategory

admin.site.register(BookCategory, BookCategoryAdmin)

class BooksIssuedAdmin(admin.ModelAdmin):
    list_display = ['student_reg_no',
                    'student_phone',
                    'book_title',
                    'date_issued',
                    'exp_return_date'
                    ]
    class Meta:
        model = BooksIssued
admin.site.register(BooksIssued, BooksIssuedAdmin)

class BookReturnHistoryAdmin(admin.ModelAdmin):
    list_display = ['student_reg_no', 'student_phone', 'book_title','date_returned']
    prepopulated_fields = {'slug': ('book_title',)}
    class Meta:
        model = BookReturnHistory
admin.site.register(BookReturnHistory, BookReturnHistoryAdmin)


