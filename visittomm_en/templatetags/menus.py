from django import template
# from ..models import Cities
# from django.views.generic.simple import direct_to_template
register = template.Library()


@register.inclusion_tag('en/menus.html')
def menus(results):
    return {
        # 'results': results,
        # 'count': len(results),
        'myvar': "myvar",
    }


# @register.inclusion_tag('en/menus.html')
# def entry_history():
#     entries = Cities.objects.all()[:5]
#     return {'entries': entries}

# def contact(request):
#     # snip ...
#     return direct_to_template(request, 'menus.html', { 'myvar' : "myvar" })