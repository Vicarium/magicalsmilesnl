from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


# Page for an embedded google document with optional thumbnail
class GcalendarPage(Page):
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)
    link = models.CharField(max_length=255, blank=False)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

GcalendarPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    FieldPanel('body', classname="full"),
    FieldPanel('link', classname="full")
]

GcalendarPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]
