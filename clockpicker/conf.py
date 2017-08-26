# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.conf import settings as base_settings


class ClockpickerConfig(AppConfig):
    name = 'clockpicker'


class Settings(object):
    CLOCKPICKER_VERSION = '0.0.7'
    CLOCKPICKER_JS = '//cdnjs.cloudflare.com/ajax/libs/clockpicker/{}/bootstrap-clockpicker.min.js'.format(
        CLOCKPICKER_VERSION)
    CLOCKPICKER_CSS = '//cdnjs.cloudflare.com/ajax/libs/clockpicker/{}/bootstrap-clockpicker.min.css'.format(
        CLOCKPICKER_VERSION)

    def __getattribute__(self, name):
        if hasattr(base_settings, name):
            return getattr(base_settings, name)
        return object.__getattribute__(self, name)


settings = Settings()
