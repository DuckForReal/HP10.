from django.db import models
# from django.utils.text import slugify

# Create your models here.

# class Destination(models.Model):
    # name = models.CharField(max_length=200)
    # slug = models.SlugField(unique=True, blank=True)
    # description = models.TextField()
    # location = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='destinations/')
    # featured_activities = models.TextField(help_text='List the featured activities, one per line')
    # best_time_to_visit = models.CharField(max_length=200, help_text="Ex: Spring (February-April)")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # 
    # class Meta:
        # ordering = ['name']
        # 
    # def __str__(self):
        # return self.name
    # 
    # def save(self, *args, **kwargs):
        # if not self.slug:
            # self.slug = slugify(self.name)
        # super().save(*args, **kwargs)
    # 
    # def get_activities_list(self):
        # return [activity.strip() for activity in self.featured_activities.split('\n') if activity.strip()]