from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


from url_app.models import Urls
from url_app import randomstrings

import time
import json
import favicon


# Create your views here.


def index(request):
    c = {}
    most_popular = Urls.objects.order_by('-count')[:10]
    c['urls'] = most_popular
    return render(request, 'url_app/index.html', context=c)


def redirect_original(request, alias):
    url = get_object_or_404(Urls, pk=alias)
    # get object, if not found return 404 error
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)


def shorten_url(request):
    url = request.POST.get('url', '')
    custom_alias = request.POST.get('custom_alias', '')
    max_length = request.POST.get('max_length', 6)
    response_data = {}

    if not (url == ''):

        start = time.time()

        while True:

            alias = custom_alias or randomstrings.alpha(max_length)

            try:
                temp = Urls.objects.get(pk=alias)
                if not (custom_alias == ''):
                    response_data['alias'] = alias
                    response_data['ERR_CODE'] = '001'
                    response_data['description'] = 'CUSTOM ALIAS ALREADY EXISTS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")

            except ObjectDoesNotExist:

                icon = favicon.get(url)[0]

                b = Urls(httpurl=url, alias=alias, favicon=icon.url)
                b.save()

                response_data['alias'] = alias
                response_data['url'] = settings.SITE_URL + "/" + alias
                response_data['statistics'] = {'time_taken': int((time.time() - start) * 1000)}
                return HttpResponse(json.dumps(response_data), content_type="application/json")