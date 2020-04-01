from django.db import models
from django.urls import reverse
from django.db.models import (
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    EmailField,
    URLField,
    ManyToManyField,
    ForeignKey,
    CASCADE
)
from django_extensions.db.fields import AutoSlugField

# Create your models here.up()
class Tag(Model):
    name = CharField(max_length = 31, unique=True)
    #slug = SlugField(max_length = 31, unique=True, help_text="A Label for URL Config.")
    slug = AutoSlugField(
        help_text="A label for URL config.",
        max_length=31,
        populate_from=["name"],
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        print("in get_absolute_url: self.slug: ", self.slug)
        return reverse(
            "tag_detail", kwargs={"slug":self.slug},
        )

    def get_update_url(self):
        """Return URL to update page of Tag"""
        return reverse(
            "tag_update", kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        """Return URL to delete page of Tag"""
        return reverse(
            "tag_delete", kwargs={"slug": self.slug}
        )

class Startup(Model):
    name = CharField(max_length = 31, db_index=True,)
    slug = SlugField(max_length = 31, unique=True, help_text="A Label for URL Config.")
    description = TextField()
    founded_date = DateField("date founded")
    contact = EmailField()
    website = URLField(max_length=255)
    tags = ManyToManyField(Tag)

    class Meta:
        get_latest_by = "founded_date"
        ordering = ["name"]


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("startup_detail", kwargs={"slug":self.slug})

    def get_update_url(self):
        """Return URL to update page of Startup"""
        return reverse(
            "startup_update", kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        """Return URL to delete page of Startup"""
        return reverse(
            "startup_delete", kwargs={"slug": self.slug}
        )
'''
    def get_newslink_create_url(self):
        """Return URL to detail page of Startup"""
        return reverse(
            "newslink_create",
            kwargs={"startup_slug": self.slug},
        )
'''

class NewsLink(Model):
    title = CharField(max_length = 31)
    slug = SlugField(max_length = 31)
    pub_date = DateField("date published")
    link = URLField(max_length=255)
    startup = ForeignKey(Startup, on_delete=CASCADE)

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date"]
        unique_together = ("slug", "startup")
        verbose_name = "news article"


    def __str__(self):
        return f"{self.startup}: {self.title}"
