# -*- coding: utf-8 -*-
import re

from django import forms
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.translation import ugettext

COMPONENT_TEMPLATE = u"""
        <div class="input-group clockpicker" {}>
            {}
            <span class="input-group-addon">
            <span class="glyphicon glyphicon-time"></span></span>
        </div>"""


class ClockpickerWidget(forms.TimeInput):
    glyphicon = 'glyphicon-time'

    def __init__(self, attrs=None, options=None, format=None):
        self.options = options
        if self.options is None:
            self.options = {}
        self.options.setdefault('autoclose', True)
        self.options.setdefault('donetext', ugettext('Done'))

        if attrs is None:
            attrs = {}

        self.cpw_attrs = {}

        for k, v in self.options.items():
            if isinstance(v, bool):
                v = {True: 'true', False: 'false'}[v]
            # set properties
            pattern = re.sub('([A-Z]+)', r'-\1', k).lower()
            # we convert value to string (mainly for boolean values)
            self.cpw_attrs["data-%s" % pattern] = str(v)

        super(ClockpickerWidget, self).__init__(attrs, format)

    def render(self, name, value, attrs=None, renderer=None):
        attrs["type"] = self.input_type
        attrs["name"] = name
        input_attrs = self.build_attrs(attrs)
        rendered = super(ClockpickerWidget, self).render(name, value, input_attrs, renderer)
        cpw_attrs = self.build_attrs(self.cpw_attrs)
        return format_html(COMPONENT_TEMPLATE, flatatt(cpw_attrs), rendered, self.glyphicon)

    def _get_media(self):
        return forms.Media(
            js=('clockpicker/js/clockpicker_init.js',),
        )

    media = property(_get_media)
