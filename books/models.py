from __future__ import unicode_literals

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField




#book categories
class BookCategory(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    def __unicode__(self):
        return self.category_name

#books
class Book(models.Model):

    book_category = models.ForeignKey(BookCategory, related_name='books')
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    copies = models.IntegerField(default=1)
    image = models.ImageField(upload_to='bks_photos')
    publisher = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('book_title',)
        verbose_name_plural = "Books"
    def __unicode__(self):

        return self.book_title

#model for storing books issued out
class BooksIssued(models.Model):
    student_reg_no = models.CharField(max_length=100)
    student_phone = PhoneNumberField("Phone Number")
    book_title = models.CharField(max_length=100)
    date_issued = models.DateTimeField(auto_now_add=True)
    exp_return_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date_issued',)
        verbose_name_plural = "Books Issued"

    def __unicode__(self):
        return self.student_reg_no

class BookReturnHistory(models.Model):
    student_reg_no = models.CharField(max_length=100)
    student_phone = PhoneNumberField("Phone Number")
    book_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    date_returned = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_returned',)
        verbose_name_plural = "Books Returned Log"













