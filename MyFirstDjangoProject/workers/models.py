from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    salary = models.IntegerField(default=0)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Worker({self.id}) {self.name}: {self.salary} $'


class Resume(models.Model):
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)  # при видаленні Worker, зникне його Resume
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f'Резюме {self.worker.name}'


class Contact(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='contacts')


