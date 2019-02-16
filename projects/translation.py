from .models import ProjectsPage, IndividualProjectsPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(ProjectsPage)
class ProjectsPageTR(TranslationOptions):
    fields = (
        'description',
    )

@register(IndividualProjectsPage)
class IndividualProjectsPageTR(TranslationOptions):
    fields = (
        'technologies',
    )
