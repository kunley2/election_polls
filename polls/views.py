from django.shortcuts import render
from .forms import PollUnitForm,LGAForm,CreatePollForm
from .models import AnnouncedPuResults,Lga,PollingUnit
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    unit_no = ''
    if request.method == 'POST':
        form = PollUnitForm(request.POST)
        if form.is_valid():
            unit_no = form.cleaned_data['poll_unit_no']
    else:
        form = PollUnitForm()
    HttpResponseRedirect(reverse('index'))

    no = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit_no)
    context = {'form':form,'no':no}
    return render(request,'home.html',context)


def lga(request):
    pdp = []
    dpp = []
    acn = []
    ppa = []
    cdc = []
    jp = []
    anpp = []
    labo = []
    cpp = []
    data = LGAForm()
    if request.method == 'POST':
        lga = request.POST['lga']
        lga_id= Lga.objects.filter(lga_name=lga).values('lga_id')
        poll_unit_no = PollingUnit.objects.filter(lga_id__in=lga_id)#.values_list('polling_unit_id')

        for l in poll_unit_no:
            party = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid).values_list('party_abbreviation',flat=True)
            dpp_votes = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid,
                                                               party_abbreviation="DPP").values_list('party_score',
                                                                                                  flat=True)
            pdp_votes = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid,
                                                               party_abbreviation="PDP").values_list('party_score',
                                                                                                     flat=True)
            acn_votes = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid,
                                                               party_abbreviation="ACN").values_list('party_score',
                                                                                                     flat=True)
            ppa_votes = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid,
                                                               party_abbreviation="PPA").values_list('party_score',
                                                                                                     flat=True)
            cdc_votes = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid,
                                                               party_abbreviation="CDC").values_list('party_score',
                                                                                                     flat=True)
            jp_votes = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid,
                                                               party_abbreviation="JP").values_list('party_score',
                                                                                                     flat=True)
            anpp_votes = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid,
                                                               party_abbreviation="ANPP").values_list('party_score',
                                                                                                     flat=True)
            labo_votes = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid,
                                                               party_abbreviation="LABO").values_list('party_score',
                                                                                                     flat=True)
            cpp_votes = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=l.uniqueid,
                                                               party_abbreviation="CPP").values_list('party_score',
                                                                                                     flat=True)
            k = [pdp.append(l) for l in pdp_votes]
            k = [acn.append(l) for l in acn_votes]
            k = [jp.append(l) for l in jp_votes]
            k = [ppa.append(l) for l in ppa_votes]
            k = [cdc.append(l) for l in cdc_votes]
            k = [anpp.append(l) for l in anpp_votes]
            k = [labo.append(l) for l in labo_votes]
            k = [cpp.append(l) for l in cpp_votes]
            k = [dpp.append(l) for l in dpp_votes]
            HttpResponseRedirect(reverse('lga'))
    pdp = sum(pdp)
    acn = sum(acn)
    jp = sum(jp)
    ppa = sum(ppa)
    cdc = sum(cdc)
    anpp = sum(anpp)
    labo = sum(labo)
    cpp = sum(cpp)
    dpp = sum(dpp)
    context = {'data':data,'pdp':pdp,'acn':acn,
               'jp':jp,'ppa':ppa,'cdc':cdc,'anpp':anpp,'labo':labo,'cpp':cpp,'dpp':dpp,}
    return render(request,'lga.html',context)


def poll_unit(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            poll_no = form.cleaned_data['poll_unit']
            party = form.cleaned_data['party']
            vote = form.cleaned_data['votes']
            party2 = form.cleaned_data['party2']
            vote2 = form.cleaned_data['votes2']
            party3 = form.cleaned_data['party3']
            vote3 = form.cleaned_data['votes3']
            party4 = form.cleaned_data['party4']
            vote4 = form.cleaned_data['votes4']
            party5 = form.cleaned_data['party5']
            vote5 = form.cleaned_data['votes5']
            party6 = form.cleaned_data['party6']
            vote6 = form.cleaned_data['votes6']
            party7 = form.cleaned_data['party7']
            vote7 = form.cleaned_data['votes7']
            party8 = form.cleaned_data['party8']
            vote8 = form.cleaned_data['votes8']
            party9 = form.cleaned_data['party9']
            vote9 = form.cleaned_data['votes9']
            name = form.cleaned_data['user']
            poll = AnnouncedPuResults(polling_unit_uniqueid=poll_no,party_abbreviation=party,
                                      party_score=vote,entered_by_user=name)
            poll2 = AnnouncedPuResults(polling_unit_uniqueid=poll_no, party_abbreviation=party2,
                                      party_score=vote2, entered_by_user=name)
            poll3 = AnnouncedPuResults(polling_unit_uniqueid=poll_no, party_abbreviation=party3,
                                      party_score=vote3, entered_by_user=name)
            poll4 = AnnouncedPuResults(polling_unit_uniqueid=poll_no, party_abbreviation=party4,
                                      party_score=vote4, entered_by_user=name)
            poll5 = AnnouncedPuResults(polling_unit_uniqueid=poll_no, party_abbreviation=party5,
                                      party_score=vote5, entered_by_user=name)
            poll6 = AnnouncedPuResults(polling_unit_uniqueid=poll_no, party_abbreviation=party6,
                                      party_score=vote6, entered_by_user=name)
            poll7 = AnnouncedPuResults(polling_unit_uniqueid=poll_no, party_abbreviation=party7,
                                      party_score=vote7, entered_by_user=name)
            poll8 = AnnouncedPuResults(polling_unit_uniqueid=poll_no, party_abbreviation=party8,
                                      party_score=vote8, entered_by_user=name)
            poll9 = AnnouncedPuResults(polling_unit_uniqueid=poll_no, party_abbreviation=party9,
                                       party_score=vote9, entered_by_user=name)
            poll.save()
            poll2.save()
            poll3.save()
            poll4.save()
            poll5.save()
            poll6.save()
            poll7.save()
            poll8.save()
            poll9.save()
            HttpResponseRedirect(reverse('create'))
    else:
        form = CreatePollForm()

    context = {'form':form}
    return render(request,'poll.html',context)