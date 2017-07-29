from django import template

from artist.models import ArtistPage, Page

register = template.Library()


# Artist feed
@register.inclusion_tag(
    'artist/tags/artist_listing.html',
    takes_context=True
)
def artist_listing(context, count=2):
    artists = ArtistPage.objects.live().order_by('?')
    return {
        'artists': artists[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
