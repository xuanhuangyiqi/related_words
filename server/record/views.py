#coding: utf-8
import simplejson as json
from models import *
from functions import *

from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def search_word(request):
    center = request.GET['word']

    # for xiaomao
    # add your commands here
    # to call your scrapy

    all_words = []
    f = open('output.txt').readlines()
    for x in range(len(f)/3):
        title = f[x*3]
        url = f[x*3+1]
        word = f[x*3+2]
        record = Record.objects.create(
                url = url,
                word = word,
                center = center,
                title = title
                )
        all_words.extend(word.split(' '))
    set_words = list(set(all_words))
    res = jsonResponse()
    res.write(set_words)
    res['Cache-Control'] = 'no-cache'
    print json.dumps(set_words)
    return res


def get_full_list(request):
    word1 = request.GET['word1']
    word2 = request.GET['word2']

    print Record.objects.all()[0].center
    record_list = Record.objects.filter( center = word1 )
    res_list = []
    for x in record_list:
        print x.word.split(' ')[2]
        if word2 in x.word.split(' '):
            print x.word
            res_list.append([x.title, x.url, x.word])

    res = jsonResponse()
    res.write(res_list)
    res['Cache-Control'] = 'no-cache'
    print json.dumps(res_list)
    return res

    

