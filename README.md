# django-cms-menu-icons
Simple app that allows user to add menu icons in the django-cms

#Dependencies

App requires django-cms to run, check their docs at:
https://django-cms.readthedocs.org/

App is compatbile with both django-cms <3 and newest versions.

#Features

App allows you to add a icon class or image or both.
Full integration with django cms - to add/change icon - go to edit mode, and on the page dropdown menu you will find "page icon" option.

#Usage

You can access menu icons in the template by using {{child.menu_icon_font_awesome}} or {{child.menu_icon_image}}

Example:

    {% for child in children %}
    		<li class="{% if child.selected %}active {% endif %}" title="{{child.get_menu_title}}">
    			<a href="{{ child.attr.redirect_url|default:child.get_absolute_url }}"> <i class="fa color--50 {{child.menu_icon_font_awesome}} "></i>{{child.get_menu_title}}</a>
    		</li>
    {% endfor %}
