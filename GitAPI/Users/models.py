from django.db import models

# Create your models here.
class users(models.Model):
    user = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=100,blank=True, null= True)
    public_repo = models.IntegerField()
    created = models.DateTimeField(default=None, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    followers = models.IntegerField(default=None, null=False)
    following = models.IntegerField(default=None, null=False)

    class Meta:
        verbose_name_plural = "users"

    def __str__(self):
        return self.name
