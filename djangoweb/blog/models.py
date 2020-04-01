from django.db import models
from django.db.models import (
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    ManyToManyField
)
from django.urls import reverse

from datetime import date

from organizer.models import Startup, Tag

# Create your models here.
class Post(Model):
    title = CharField(max_length=63)
    slug = SlugField(max_length = 63, help_text="A Label for URL config.", unique_for_month="pub_date")
    text = TextField()
    pub_date = DateField("date published", default=date.today)
    #tags = ManyToManyField(Tag)
    #startups = ManyToManyField(Startup)
    tags = ManyToManyField(Tag, related_name="blog_posts")
    startups = ManyToManyField(Startup, related_name="blog_posts")

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date","title"]
        verbose_name = "blog_post"

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"

    def get_absolute_url(self):
        return reverse(
            "post_detail",
            kwargs={
                "year": self.pub_date.year,
                "month": self.pub_date.month,
                "slug": self.slug,
            },
        )

    def get_update_url(self):
        """Return URL to update page of Post"""
        return reverse(
            "post_update",
            kwargs={
                "year": self.pub_date.year,
                "month": self.pub_date.month,
                "slug": self.slug,
            },
        )

    def get_delete_url(self):
        """Return URL to delete page of Post"""
        return reverse(
            "post_delete",
            kwargs={
                "year": self.pub_date.year,
                "month": self.pub_date.month,
                "slug": self.slug,
            },
        )
