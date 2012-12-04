# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import get_model

def aloha_init(request):
    """
    Build the javascript file which is initializing the aloha-editor
    Run the javascript code for the AlohaInput widget
    """
    
    links = []
    link_models = getattr(settings, 'DJALOHA_LINK_MODELS', ())
    sidebar_disabled = getattr(settings, 'DJALOHA_SIDEBAR_DISABLED', True)
    for full_model_name in link_models:
        app_name, model_name = full_model_name.split('.')
        model = get_model(app_name, model_name)
        if model:
            links.extend(model.objects.all())
    
    return render_to_response(
        'djaloha/aloha_init.js',
        {
            'links': links,
            'sidebar_disabled': 'true' if sidebar_disabled else 'false',
        },
        context_instance=RequestContext(request)
    )
