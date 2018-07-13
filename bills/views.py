from django.template import loader
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils import translation


def bill_page(request):
    curr_site_info = "Bills"
    pages = [
        ("Home", _("Home")),
        ("Bills", _("Bills")),
    ]

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    template = loader.get_template('pages/bills.html')
    context = {
        "TAB_TITLE": _("Bills"),
        "PAGES": pages,
        "CURR_SITE": curr_site_info,
    }
    return HttpResponse(template.render(context, request))