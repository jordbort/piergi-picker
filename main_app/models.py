from django.db import models

# Create your models here.


class Pierogi(models.Model):

    method = models.CharField(max_length=20)
    filling = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filling

    class Meta:
        ordering = ['filling']


# class Pierogi:
#     def __init__(self, method, filling, image):
#         self.method = method
#         self.filling = filling
#         self.image = image
