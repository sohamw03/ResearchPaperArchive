from django.db import models
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.


class Paper(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    slug = models.SlugField(null=True, max_length=255)
    researchPaper = models.FileField(
        upload_to="static/pdf/", max_length=250, null=True, default="")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("paper_detail", kwargs={"slug": self.slug})
