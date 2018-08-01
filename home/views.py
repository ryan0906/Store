from django.template import loader
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.core.cache import cache


def home(request):
    #if request.LANGUAGE_CODE == 'vi'
    #user_language = "vi"
    #translation.activate(user_language)
    #request.session[translation.LANGUAGE_SESSION_KEY] = request.LANGUAGE_CODE

<<<<<<< HEAD
    tables = cache.keys("con*")
    if len(tables) < 1:
        cache_data = ""
    else:
        for i in tables:
            cache_data = cache.get(i)
=======
    test = cache.scan("conv*")
    if len(test) < 1:
        cache_data = ""
    else:
        for i in test:
            cache_data = test.get(i)
>>>>>>> f2886f1dd39bd905a364c4917e3dba06a03e2602

    # if 'conv' in cache:
    #     cache_data = cache.get('conv')
    #else:
    #    cache_data = ""
    curr_site_info = "Home"
    pages = [
        ("Home", _("Home")),
        ("Bills", _("Bills")),
    ]
    curr_orders = []

    curr_orders += [{
        "table": 1,
        "dishes": [{"BCCC": 1, "BCG": 2}],
    }]

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    template = loader.get_template('pages/home.html')
    context = {
        "TAB_TITLE": _("Home"),
        "PAGES": pages,
        "CURR_SITE": curr_site_info,
        "CURR_ORDERS": curr_orders,
        "cacheData": cache_data,
    }
    return HttpResponse(template.render(context, request))