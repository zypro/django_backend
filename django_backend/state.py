# -*- coding: utf-8 -*-
from django.conf import settings

from .localstate import LocalState


def _get_languages():
    languages = tuple(settings.LANGUAGES)
    contains_default_language = any(
        (code, name)
        for code, name in settings.LANGUAGES
        if code == settings.LANGUAGE_CODE)
    if not contains_default_language:
        languages = languages + (
            (settings.LANGUAGE_CODE, settings.LANGUAGE_CODE),
        )
    return languages


# the language state is separate to the global translation, as we want the
# backend to be translated separately
LANGUAGES = _get_languages()
LANGUAGE_IDS = [code for code, name in LANGUAGES]


language = LocalState(default=settings.LANGUAGE_CODE)


site = LocalState(default=settings.SITE_ID)


class override(object):
    def __init__(self, state_obj, value):
        self.state_obj = state_obj
        self.value = value
        self.old_value = state_obj.active

    def __enter__(self):
        self.state_obj.active = self.value

    def __exit__(self, exc_type, exc_value, traceback):
        self.state_obj.active = self.old_value
