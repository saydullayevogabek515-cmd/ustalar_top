from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name and self.description