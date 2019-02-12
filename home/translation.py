from .models import Foo
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(Foo)
class FooTR(TranslationOptions):
    fields = (
        'intro_left',
    )
