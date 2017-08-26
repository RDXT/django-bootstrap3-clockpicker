# -*- coding: utf-8 -*-
import re

from django import forms


class ClockpickerMixin(object):
    def __init__(self, attrs=None, clockpicker_attrs=None):
        # Immediate finalization, return the structure
        if clockpicker_attrs is None:
            clockpicker_attrs = {}
        if attrs is None:
            attrs = {}
        for k, v in clockpicker_attrs.items():
            # We set properties as underscore string
            underscore = re.sub('([A-Z]+)', r'-\1', k).lower()
            # we convert value to string (mainly for boolean values)
            attrs["clockpicker-%s" % underscore] = str(v)

        attrs['data-clockpicker'] = "clockpicker"
        super(ClockpickerMixin, self).__init__(attrs)

    def _get_media(self):
        """
        Construct Media as a dynamic property.
        .. Note:: For more information visit
            https://docs.djangoproject.com/en/1.8/topics/forms/media/#media-as-a-dynamic-property
        """
        return forms.Media(
            js=('clockpicker/js/clockpicker_init.js',),
        )

    media = property(_get_media)


class ClockpickerWidget(ClockpickerMixin, forms.TimeInput):
    pass
