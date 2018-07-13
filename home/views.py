from django.template import loader
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils import translation


def home(request):
    #if request.LANGUAGE_CODE == 'vi'
    #user_language = "vi"
    #translation.activate(user_language)
    #request.session[translation.LANGUAGE_SESSION_KEY] = request.LANGUAGE_CODE

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
    }
    return HttpResponse(template.render(context, request))