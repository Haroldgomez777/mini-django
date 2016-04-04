# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.encoding import smart_text
from myapp.models import Document
from myapp.models import Msg
from myapp.forms import DocumentForm
from myapp.forms import MsgForm
from .ecc import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def msg(request):
    
    if request.method == "POST":
        form = MsgForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            testmsg1 = post.user
            testmsg1 = bytes(testmsg1,'utf-8')
            public = passphrase_to_pubkey(testmsg1)
            testmsg1 = public
            pkey = post.public
            msgenc = post.encmsg
            #testmsg = encrypt(b'This is a very secret message\n', b'8W;>i^H0qi|J&$coR5MFpR*Vn') 
            #testmsg = byte_string.decode(encoding)
            #unicode_text = byte_string.decode(encoding)
            #testmsg1 = smart_text(testmsg, encoding='utf-8', strings_only=True, errors='strict')
            #str2 = bytes("hello world", encoding="UTF-8")
            post.save()
		
            return render(request, 'myapp/msg.html', {'form': form ,'pkey':pkey ,'msgenc':msgenc ,'testmsg1':testmsg1})
    else:
	
        form = MsgForm()
        #message = Msg.objects.all()
        return render(request, 'myapp/msg.html', {'form': form })
    
def liss(request):
    # Handle file upload
	    
    MEDIA_FILE = os.path.join(BASE_DIR, 'media/%s.enc' % os.urandom(10).encode('hex'))
   
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            encrypt_file(request.FILES['docfile'], MEDIA_FILE, '8W;>i^H0qi|J&$coR5MFpR*Vn')
            decrypt_file( MEDIA_FILE,  os.path.join(BASE_DIR, 'media/file.jpg' ), b'my private key')
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('liss'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    """ 
   return render_to_response(
        'list.html',
        {'documents': documents, 'form': form },
        context_instance=RequestContext(request)
    )
    """
    return render(request, 
        'myapp/list.html', 
        {'documents': documents, 'form': form }
    )


def encc(request):
    pass
    

def dencc(request):
    pass
