from django import template
from app_menu.models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    """
    Функция, которая рисует меню на основе указанного имени меню.
    Декоратор @register.simple_tag используется в Django для создания пользовательских шаблонных тегов. Он регистрирует
    функцию как шаблонный тег, который может быть использован в шаблонах Django.
    Параметры:
        menu_name (str): Имя меню, которое нужно нарисовать.

    Возвращает:
        str: Выведенное меню в виде строки.
    """
    menu_items = MenuItem.objects.filter(name=menu_name).select_related('parent')
    return mark_safe(_render_menu(menu_items))


def _render_menu(menu_items):
    """
    Рендерит строку HTML-меню на основе предоставленных элементов меню.

    Аргументы:
        menu_items (list): Список объектов MenuItem, представляющих элементы меню.

    Возвращает:
        str: Сгенерированная строка HTML-меню.
    """
    menu_html = '<ul>'
    for item in menu_items:
        menu_html += '<li>'
        if item.url:
            menu_html += f'<a href="{item.url}">{item.name}</a>'
        elif item.named_url:
            menu_html += f'<a href="{item.named_url}">{item.name}</a>'
        else:
            menu_html += item.name
        if item.children.exists():
            menu_html += _render_menu(item.children.all())
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
