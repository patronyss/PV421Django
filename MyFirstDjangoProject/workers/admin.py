from django.contrib import admin
from workers.models import Worker, Resume

# Register your models here.
admin.site.register(Worker)
admin.site.register(Resume)
