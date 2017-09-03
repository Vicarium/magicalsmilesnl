from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel




class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    # # Overight mail function to send email in a format friendly to google calendar
    # def send_mail(self, form):
    #     addresses = [x.strip() for x in self.to_address.split(',')]
    #
    #     # Add submission date to subject string
    #     submitted_date_str = date.today().strftime('%x')
    #     subject = self.subject + " - " + submitted_date_str
    #
    #     # Create email content from template using form values as context
    #     template = '/form/email_template.html'
    #     context = {}
    #     for field in form:
    #         context[field.label] = field.value()
    #     email_content = render_to_string(template, context)
    #
    #     send_mail(subject, email_content, addresses, self.from_address)


    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )



FormPage.promote_panels = AbstractEmailForm.promote_panels + [
    ImageChooserPanel('feed_image'),
]
