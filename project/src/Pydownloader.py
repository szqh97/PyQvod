#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import Queue
import downloader
import downloadviewer
import listenURL
import threading 
import pprint


#class qvodDownload(threading.Thread):
#    def __init__(self, urlfiles):
#        threading.Thread.__init__(self)
#
#

def downloadProc(url, filename):

    #url = u'qvod://297167808|0225CE017F36A404BF7347ED306311E8BC96C9C8|小爸爸_HDTV_01.rmvb|'
    #fname = url.split('|')[-2]

    downloader.download(url, None, fname)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '''usage: Pydownloader.py "qvod://297167808|0225CE017F36A404BF7347ED306311E8BC96C9C8|小爸爸_HDTV_01.rmvb|" "filename"'''
        os._exit(1)
    url = unicode(sys.argv[1])
    fname = unicode(sys.argv[2])
    ret = downloader.valid_url(url)
    if ret == False:
        print ''' the url is not a valid url '''
        os._exit(2)
    downloadProc(url, fname)
    os._exit(0)


