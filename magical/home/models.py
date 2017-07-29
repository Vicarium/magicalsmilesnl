from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey

from common.models import RelatedLink, StandardIndexPage, CarouselItem

class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.HomePage', related_name='carousel_items')


class HomePage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


HomePage.content_panels = [
    FieldPanel('intro', classname="full"),
    FieldPanel('body', classname="full"),
    ImageChooserPanel('image'),
    InlinePanel('carousel_items', label="Carousel items"),
]
