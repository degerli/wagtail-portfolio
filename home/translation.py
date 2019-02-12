from .models import HomePage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(HomePage)
class FooTR(TranslationOptions):
    fields = (
        'intro_left',
    )
