# -*- coding: utf-8 -*-

from django.http import HttpResponse
import time
from moviefun.models import *
def select(request):
        t0=time.clock()
        s=Movie.objects.filter(year='2007',type='episode')
        response=''
        n=0
        for var in s:
                r=TVPlay.objects.get(imdbid=var.imdbid)
                if r.season=='3':
                        n=n+1
                        response += str(n) + '.' + var.title + ' '
        t0=time.clock()-t0
        response='runningtime: ' + str(t0) + ' ' + response
        return HttpResponse("<p>" + response + "</p>")
