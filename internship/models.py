from django.db import models
from core.models import CustomUser

User = CustomUser()
# Create your models here
 
#creating a table for Categories
class Category (models.Model):
    name=models.CharField(max_length=250)


    #to change the name of the plural tabl
    class Meta :
        verbose_name_plural='Categories'
        ordering=('name',) # to reorder the items 

    #to show the name of every category
    def __str__(self):
        return self.name
    
TYPE_CHOICES = (
    ('practical','practical'),
    ('theoretical', 'theoretical'),
)    
class Item (models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField(blank=True,null=True)
    interns=models.FloatField()
    duration=models.FloatField()
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    #to add the creator and delete te model once the creator deleted
    created_by=models.ForeignKey(User, related_name='internships',on_delete=models.CASCADE)    
    #same thing for the category
    category=models.ForeignKey(Category, related_name='internships', on_delete=models.CASCADE)

    class Meta :
        ordering=('category','name',) 
    def __str__(self):
        return self.name