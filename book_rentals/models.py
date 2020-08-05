from django.db import models
from users.models import CustomUser
from books.models import Book

class Book_Rental(models.Model):
    
    RETURNED = 1
    NOT_RETURNED = 2
    STATUS_CHOICES = (
        (RETURNED, 'Returned'),
        (NOT_RETURNED, 'Not Returned'),
    )
    
    ref = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    status =  models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=False, blank=True, default=2)

    def __str__ (self):
        return str(self.ref)

