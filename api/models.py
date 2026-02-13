from django.db import models
from django.contrib.auth.models import User
class Report(models.Model):

    TYPE_CHOICES = [
        ('yardim', '🚑 ACİL YARDIM'),
        ('kayip', '🔎 KAYIP / BULUNDU'),
    ]
    STATUS_CHOICES = [
        ('acil', '🔴 ACİL DURUM'),
        ('bekliyor', '🟡 Bekliyor'),
        ('cozuldu', '🟢 Çözüldü'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    report_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='yardim')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='acil')
    image = models.ImageField(upload_to='reports/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


