from django import template

from ..models.pages import NewHomePage

register = template.Library()


@register.simple_tag
def home_page_nav_link(page, hash):
    if isinstance(page, NewHomePage):
        return f"{hash}"

    while page and not isinstance(page, NewHomePage):
        page = page.get_parent().specific

    if page:
        return f"{page.url}{hash}"

    return f"/{hash}"
