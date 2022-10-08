from django.db import models

# Create your models here.


class news(models.Model):
    source=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    title=models.IntegerField()
    #description=models.ForeignKey(Department, on_delete=models.CASCADE)

    def str(self) -> str:
        return self.source
