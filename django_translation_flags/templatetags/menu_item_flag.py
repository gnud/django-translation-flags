from django import template

register = template.Library()


@register.inclusion_tag('language_item.html', takes_context=True)
def menu_item_flag(context, flag_type='', flag_iso='', flag_style='', flag_classes='', **kwargs):
    """
    Templatetag menu_item_flag

    :param context: Getting context
    :param flag_type: Default empty, It accepts the string 'square'
    :param flag_iso: Default empty, ISO language country code
    :param flag_style: Pass inline styles to the img tag
    :param flag_classes: Pass classes to use on the img tag
    :param kwargs: Classes to HTML tags
    :return: A dict with classes
    """

    icon_full_path = f'icons/{flag_type}/{flag_iso}.svg'

    default = dict(li_class='', a_class='')
    classes = dict(default, **kwargs)
    return {
        'icon_class': flag_type,
        'icon_path': icon_full_path,
        'icon_iso': flag_iso,
        'icon_style': flag_style,
        'icon_classes': flag_classes,
        'classes': classes,
        'redirect_to': context.request.get_full_path
    }
