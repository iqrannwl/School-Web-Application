from django.db import models

# class testimonialManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status='isPublic')



from django.db import models

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='isPublic')        