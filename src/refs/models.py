from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.name} #{self.pk}"
    
class PostOffice(models.Model):
    number = models.CharField(max_length=100)
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name="post_offices"
        )
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"Post office # {self.pk}"

