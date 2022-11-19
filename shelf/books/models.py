from email.policy import default
from random import choices
from secrets import choice
from unicodedata import category
from xml.parsers.expat import model
from django.db import models
from django.urls import reverse
import gettext as _
# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class Publisher(models.Model):

    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Publisher_detail", kwargs={"pk": self.pk})

    
class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Book(models.Model):

    NEWCONDITION = "NC"
    USEDCONDITION = "UC"
    REFURBISHEDCONDITION= "RC"
    DAMAGEDCONDITION = "DC"
    CONDITION_CHOICES = (
        (NEWCONDITION, "New Condition"),
        (USEDCONDITION,"Used Condition"),
        (REFURBISHEDCONDITION, "Refurbished Condition"),
        (DAMAGEDCONDITION, "Damaged Condition"),
    )
    name = models.CharField(max_length=250, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
#    condition = models.CharField(max_length=2, choices=CONDITION_CHOICES, default=USEDCONDITION)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication = models.DateField()
    abstract = models.TextField(blank=True)
#    isbn = models.IntegerField(blank=True, null=True)
    image = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})

