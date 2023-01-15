from django.db import models

class Joy(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    # __str__ mane holo ei Joy table ta theke by default je je value gula print korty casshi ( mane joy ke call korlei ei property gula show korbe ). django dashboard a 
    def __str__(self):
        return self.name+" "+self.description+" ";

