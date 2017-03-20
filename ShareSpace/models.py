from django.db import models


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
    user_id = models.ForeignKey('auth.User')

    def __str__(self):
        return self.storage_name
