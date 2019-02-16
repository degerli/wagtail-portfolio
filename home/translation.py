from .models import HomePage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'intro_heading',
        'intro_sub_heading',
        'intro_left',
        'intro_right',
    )
