# -*- coding: utf-8 -*-
import requests, json
import logging
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from zipcode.models import ZipCode
from zipcode.serializers import ZipCodeSerializer

logger = logging.getLogger(__name__)
 
def logerror(msg):
    logger.debug(msg)

def logdebug(msg):
    logger.error(msg)

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def zipcode_list(request):
    if request.method == 'GET':
        if request.GET.get('limit', None):
            limit = int(request.GET.get('limit'))
            p = Paginator(ZipCode.objects.all(), 10)
            num_pages = p.num_pages
            if limit <= num_pages:
                page = p.page(limit)
                zipcodes = page.object_list
            else:
                logdebug('no more records')
                return JSONResponse({'erro': 'no more records'})
        else:
            zipcodes = ZipCode.objects.all()

        logdebug('zipcode records')
        serializer = ZipCodeSerializer(zipcodes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        zip_code = request.POST.get('zip_code')
        if not zip_code:
            logerror('zip_code is empty')
            return HttpResponse('zip_code is empty', status=500)
        r = requests.get('http://api.postmon.com.br/v1/cep/{0}'.format(zip_code))
        if r.status_code == 200:
            data = json.loads(r.content)
            zipcode, created = ZipCode.objects.get_or_create(
                zip_code=data['cep'],
                address=data['logradouro'] if data.get('logradouro') else '',
                neighborhood=data['bairro'] if data.get('bairro') else '',
                city=data['cidade'],
                state=data['estado']
            )
            serializer = ZipCodeSerializer(zipcode)
            logdebug('zip_code created')
            return HttpResponse(JSONResponse(serializer.data), status=201)

        logerror('zip_code not found')
        return JSONResponse('zipcode not found', status=200)

@csrf_exempt
def zipcode_detail(request, zip_code):
    try:
        zipcode = ZipCode.objects.get(zip_code=zip_code)
    except ZipCode.DoesNotExist:
        logerror('zipcode not found')
        return HttpResponse('zipcode not found', status=200)

    if request.method == 'GET':
        serializer = ZipCodeSerializer(zipcode)
        logdebug('zipcode show')
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ZipCodeSerializer(zipcode, data=data)
        if serializer.is_valid():
            serializer.save()
            logdebug('zipcode put')
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        logdebug('zipcode delete')
        zipcode.delete()
        return JSONResponse('', status=204)