# from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils import translation


def index(request):
    #if request.LANGUAGE_CODE == 'vi'
    #user_language = "vi"
    #translation.activate(user_language)
    #request.session[translation.LANGUAGE_SESSION_KEY] = request.LANGUAGE_CODE

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    template = loader.get_template('pages/home.html')
    context = {
        # Translators: Testing welcome message
        'temp_content': _("welcome"),
    }
    return HttpResponse(template.render(context, request))