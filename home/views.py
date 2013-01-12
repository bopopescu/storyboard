#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Darcy Liu on 2012-03-03.
Copyright (c) 2012 Close To U. All rights reserved.
"""

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.contrib import auth

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.utils.html import urlize,linebreaks
from templatetags.filter import imgize
from models import *
from forms import *
from common.filter import *
import logging
import markdown
from gfm import gfm

from storage.models import *

def index(request):
    query = Storage.objects.all().order_by('-updated')
    #return HttpResponseRedirect('/r')
    return render_to_response('index.html',{'photos':query},context_instance=RequestContext(request))
        
def about(request):
    return render_to_response('home/about.html',{},context_instance=RequestContext(request))

def minisite(request):
    if request.user.is_superuser:
        minisites = Minisite.objects.all().order_by('-updated')
        return render_to_response('home/site_list.html',{'minisites':minisites},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def page(request,minisite=None):
    if request.user.is_superuser:
        minisite = get_object_or_404(Minisite,slug=minisite)
        pages = Page.objects.all().order_by('-updated').filter(minisite=minisite)
        return render_to_response('home/page_list.html',{'pages':pages,'minisite':minisite},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def edit_page(request,minisitepath=None,pagepath=None):
    if request.user.is_superuser:
        minisite = get_object_or_404(Minisite,slug=minisitepath)
        page = get_object_or_404(Page,slug=pagepath,minisite=minisite)
    
        if page.author!=request.user:
            return HttpResponseRedirect('/minisite')
    
        if request.method == 'POST' and page:
            form = PageForm(data=request.POST or None, instance = page)
            if form.is_valid():
                obj = form.save(commit=False)
                # obj.author = request.user
                # obj.minisite = minisite
                obj.save()
                return HttpResponseRedirect('/minisite/'+minisite.slug)
        else:
            form = PageForm(instance = page, initial = {'minisite': minisite })
        return render_to_response('home/add_page.html',{'form': form},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')
    
def add_page(request,minisite=None):
    if request.user.is_superuser:
        minisite = get_object_or_404(Minisite,slug=minisite)
    
        if minisite.author!=request.user:
            return HttpResponseRedirect('/minisite')
        
        if request.method == 'POST':
            form = PageForm(data=request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = request.user
                obj.minisite = minisite
                obj.save()
                return HttpResponseRedirect('/minisite/'+minisite.slug)
        else:
            form = PageForm()
        return render_to_response('home/add_page.html',{'form':form},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')
      
def add_minisite(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = MinisiteForm(data=request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = request.user
                obj.save()
                return HttpResponseRedirect('/minisite')
        else:
            form = MinisiteForm()
        return render_to_response('home/add_site.html',{'form':form},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')
       
def router(request,path=None):
    if path:
        paths = path.split('/')
        values = None
        if len(paths) == 2:
            # if paths[1] == 'index.html':
            #     return HttpResponseRedirect('/%s/'%paths[0])
            # if paths[1] == '':
            #     paths[1] = 'index.html'
            
            minisite = get_object_or_404(Minisite,slug=paths[0])
            page = get_object_or_404(Page,slug=paths[1],minisite=minisite)
            if page.format == '0':
                page.text_html = linebreaks(urlize(imgize(page.text)))
            if page.format == '2':
                html = gfm(page.text)
                html = page.text
                page.text_html = markdown.markdown(html, ['extra','codehilite','toc','nl2br'],safe_mode=False, 
                                   html_replacement_text='--RAW HTML NOT ALLOWED--',output_format='html5')
            values = {'minisite':minisite,'page':page}
        else:
            return HttpResponseRedirect('/%s/'%path)
        return render_to_response('home/minisite.html',values,context_instance=RequestContext(request))
    return HttpResponseNotFound()