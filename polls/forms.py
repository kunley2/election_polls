from django import forms
from .models import AnnouncedPuResults,Lga,Party
import datetime

choices = [tuple([x,x]) for x in range(8,28)]
parties = [('PDP',"PDP"),
         ('DPP','DPP'),
         ('ACN','ACN'),
         ('PPA','PPA'),
         ('CDC','CDC'),
         ('JPP','JPP'),
         ('ANPP','ANPP'),
         ('LABOUR','LABOUR'),
          ('CPP','CPP'),]

class PollUnitForm(forms.Form):
    poll_unit_no = forms.IntegerField(label=' poll unit id ',
                                      widget=forms.Select(choices=choices))


class LGAForm(forms.Form):
    lga = forms.ModelChoiceField(queryset=Lga.objects.values_list('lga_name',flat=True))


class CreatePollForm(forms.Form):
    user = forms.CharField(label='type your full name')
    poll_unit = forms.IntegerField()
    party = forms.CharField(label='Party',widget=forms.Select(choices=parties))
    votes = forms.IntegerField(label='Results')
    party2 = forms.CharField(label='Party',widget=forms.Select(choices=parties))
    votes2 = forms.IntegerField(label='Results')
    party3 = forms.CharField(label='Party',widget=forms.Select(choices=parties))
    votes3 = forms.IntegerField(label='Results')
    party4 = forms.CharField(label='Party',widget=forms.Select(choices=parties))
    votes4 = forms.IntegerField(label='Results')
    party5 = forms.CharField(label='Party',widget=forms.Select(choices=parties))
    votes5 = forms.IntegerField(label='Results')
    party6 = forms.CharField(label='Party',widget=forms.Select(choices=parties))
    votes6 = forms.IntegerField(label='Results')
    party7 = forms.CharField(label='Party',widget=forms.Select(choices=parties))
    votes7 = forms.IntegerField(label='Results')
    party8 = forms.CharField(label='Party',widget=forms.Select(choices=parties))
    votes8 = forms.IntegerField(label='Results')
    party9 = forms.CharField(label='Party', widget=forms.Select(choices=parties))
    votes9 = forms.IntegerField(label='Results')



