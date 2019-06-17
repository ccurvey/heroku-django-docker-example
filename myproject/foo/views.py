# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

import requests

from django.shortcuts import render
from django.http import HttpResponse

LOGGER = logging.getLogger(__name__)

# Create your views here.
def testme(request):
    try:
        import wingdbstub
    except ImportError:
        pass

    transparint_response = requests.get("https://search.transparint.com")
    LOGGER.error("tr = " , transparint_response)
    print("tr = " , transparint_response)

    return HttpResponse("OK")