from django import template

import mistune

register = template.Library()


@register.simple_tag
def render_home_page():
    with open('HOME.md', 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    rendered_text = mistune.html(text)

    return rendered_text
