from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Index accessed')
    context = {
        "title": "Index page of Homework 06",
        "body": "At this stage just a stub page to demonstrate "
                "the site is able to function."
    }
    return render(request, "front/index.html", context=context)


def about(request):
    logger.info(f'About accessed')
    context = {"title": "About page of Homework 06"}
    return render(request, "front/about.html", context=context)
