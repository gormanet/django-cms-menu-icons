# -*- coding: utf-8 -*-
from menus.base import Modifier
from menus.menu_pool import menu_pool
from cms.models.pagemodel import Page


class MenuIconsMod(Modifier):
    """
    Extends django-cms menu context
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        for node in nodes:
            try:
                #Load icons
                page = Page.objects.get(pk=node.id)
                menu_icons = page.iconextension
                node.menu_icon_image = menu_icons.menu_icon_image
                node.menu_icon_url = menu_icons.menu_icon_url
                node.menu_icon_font_awesome = menu_icons.menu_icon_font_awesome
            except:
                pass

        return nodes

menu_pool.register_modifier(MenuIconsMod)
