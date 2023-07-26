from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Index accessed')
    return HttpResponse("Hello, world")
