from .models import HomePage
from projects.models import ProjectsPage, IndividualProjectsPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'intro_left',
    )

@register(ProjectsPage)
class ProjectsPageTR(TranslationOptions):
    fields = (
        'description',
    )

@register(IndividualProjectsPage)
class IndividualProjectsPageTR(TranslationOptions):
    pass
