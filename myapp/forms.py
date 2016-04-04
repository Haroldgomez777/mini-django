# -*- coding: utf-8 -*-

from django import forms
from .models import Msg,Document



class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        fields = ('docfile',)

class MsgForm(forms.ModelForm):

    class Meta:
        model = Msg
        fields = ('user','public', 'encmsg',)
