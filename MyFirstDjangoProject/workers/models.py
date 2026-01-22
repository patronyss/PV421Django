from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f'Worker({self.id}) {self.name}: {self.salary} $'
