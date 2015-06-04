from django.contrib import admin
from cms.extensions.admin import PageExtensionAdmin
from cms_menu_icons.models import IconExtension


class PageIconAdmin(PageExtensionAdmin):
    pass

admin.site.register(IconExtension, PageIconAdmin)
