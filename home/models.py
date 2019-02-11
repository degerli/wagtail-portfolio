from django.db import models
from django import forms
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, TabbedInterface, ObjectList
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    # Add the intro fields to homepage model
    intro_heading       = models.CharField(max_length=255, null=True)
    intro_sub_heading   = models.CharField(max_length=255, null=True)
    intro_left          = RichTextField(blank=True)
    intro_right         = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro_heading'),
        FieldPanel('intro_sub_heading'),
        FieldPanel('intro_left', classname="full"),
        FieldPanel('intro_right', classname="full"),
    ]

    # Display the portfolio items !IMPORTANT! take a good look at the slug, otherwise the page wont render.
    # Generate a projects page and insert that slug down here at Page.objects.get(slug='my-slug')
    def get_context(self, request):
        context                     = super(HomePage, self).get_context(request)
        context['portfolio_page']   = Page.objects.get(slug='afgeronde-projecten')
        return context

    # The portfolio info is registered as a wagtail setting. Can be viewed at settings --> portfolio settings
@register_setting
class PortfolioSettings(BaseSetting):
    # Personal information
    name                = models.CharField(max_length=255, help_text='Your name')
    heading             = models.CharField(max_length=255, help_text='Your title')
    email               = models.CharField(max_length=255, help_text='Your email')
    telephone           = models.CharField(max_length=255, help_text='Your telephone')
    profile_pic         = models.ForeignKey(
                                    'wagtailimages.Image',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    related_name='+'
                                    )

    # Social links
    social_linkedin     = models.URLField(max_length=255, null=True)
    social_twitter      = models.URLField(max_length=255, null=True)
    social_github       = models.URLField(max_length=255, null=True)

    # Business stats
    stat_description_1  = models.CharField(max_length=255, null=True)
    stat_number_1       = models.IntegerField(null=True)
    stat_description_2  = models.CharField(max_length=255, null=True)
    stat_number_2       = models.IntegerField(null=True)
    stat_description_3  = models.CharField(max_length=255, null=True)
    stat_number_3       = models.IntegerField(null=True)
    stat_description_4  = models.CharField(max_length=255, null=True)
    stat_number_4       = models.IntegerField(null=True)


    # Tab panel 1
    first_tab_panels = [
        FieldPanel('name'),
        FieldPanel('heading'),
        FieldPanel('email'),
        FieldPanel('telephone'),
        ImageChooserPanel('profile_pic'),
    ]
    # Tab panel 2
    second_tab_panels = [
        FieldPanel('social_linkedin'),
        FieldPanel('social_twitter'),
        FieldPanel('social_github'),
    ]
    # Tab panel 3
    third_tab_panels = [
         MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('stat_description_1'),
                        FieldPanel('stat_number_1'),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel('stat_description_2'),
                        FieldPanel('stat_number_2'),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel('stat_description_3'),
                        FieldPanel('stat_number_3'),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel('stat_description_4'),
                        FieldPanel('stat_number_4'),
                    ]
                ),
            ],
            heading="Business stats",
            classname="collapsible",
        ),
    ]

    # Tab handler
    edit_handler = TabbedInterface([
        ObjectList(first_tab_panels, heading='Personal information'),
        ObjectList(second_tab_panels, heading='Social media'),
        ObjectList(third_tab_panels, heading='Business stats'),
    ])
