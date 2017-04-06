from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


def user_directory(instance, filename):
    return 'user_{0}/{1}/{2}'.format(instance.user_id, instance.storage_name, filename)


class Storage(models.Model):
    STORAGE_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )

    storage_id = models.AutoField(primary_key=True)
    storage_name = models.CharField(max_length=40, default='Storage')
    size = models.CharField(max_length=1, choices=STORAGE_SIZES)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    area_code = models.IntegerField()
    photos = ImageField(upload_to=user_directory, null=True, blank=True)
    date_from = models.DateField()
    date_to = models.DateField()
    user_id = models.ForeignKey(User)

    def __str__(self):
        return self.storage_name
