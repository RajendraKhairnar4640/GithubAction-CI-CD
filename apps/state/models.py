from django.db import models
from django.utils import timezone



# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.IntegerField(default=1,blank=True,null=True,help_text='1->Active,0->Inactive',choices=((1,'Active'),(0,'Inactive')))
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'state'
        verbose_name_plural = 'StateList'