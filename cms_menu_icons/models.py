# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.extensions.models import PageExtension
from cms.extensions.extension_pool import extension_pool


class IconExtension(PageExtension):
    """
    This model extent django-cms page and add icon related fields
    """
    menu_icon_font_awesome = models.CharField(
        max_length=48,
        verbose_name="Icon",
        default="icon-",
        blank=True,
        null=True,
        help_text="use font awesome codes - http://fortawesome.github.io/Font-Awesome/icons/"
    )
    menu_icon_image = models.ImageField(
        'Menu Icon Image',
        upload_to='menu_icons/',
        blank=True,
        null=True
    )
    menu_icon_url = models.URLField(
        'Menu Icon URL',
        blank=True,
        null=True)


extension_pool.register(IconExtension)
