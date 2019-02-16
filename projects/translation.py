from .models import ProjectsPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(ProjectsPage)
class ProjectsPageTR(TranslationOptions):
    fields = (
        'description',
    )
