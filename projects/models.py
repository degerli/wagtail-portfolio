from django.db import models
from django import forms

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.snippets.models import register_snippet


class ProjectsPage(Page):
    description = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
    ]



class IndividualProjectsPage(Page):
    technologies    = ParentalManyToManyField('projects.TechnologyUsed', blank=True)
    client          = models.CharField(max_length=255, blank=True)
    link            = models.URLField(max_length=255, blank=True)
    completed       = models.DateField(max_length=255, blank=True, null=True)

    project_image   = models.ForeignKey(
                                    'wagtailimages.Image',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    related_name='+'
                                    )


    content_panels = Page.content_panels + [
        FieldPanel('client'),
        FieldPanel('link'),
        FieldPanel('completed'),
        FieldPanel('technologies', widget=forms.CheckboxSelectMultiple),
        ImageChooserPanel('project_image'),
    ]


@register_snippet
class TechnologyUsed(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Technologies'
