from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from .forms import *
from .models import AggregateCase

import pickle
import pandas as pd
import os

# Create your views here.

MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictive_framework/model/finalmodel.pkl')
INITIAL_RATE = 50
BINS = [-12.211, 1526.375, 3052.75, 4579.125, 6105.5, 7631.875, 9158.25, 10684.625, 12211.]


def predictive_home(request):
    return render(request, 'predictive_framework/predict_home.html', context={'form': PredictForm})


def aggregate_home(request):
    fiscal_years = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('fiscal_year')]
    claims = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('claims')]
    request_types = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('request_type')]
    appeal_categories = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('appeal_category')]
    medicare_parts = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('medicare_part')]
    requestor_types = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('requestor_type')]
    states = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('state')]
    otrs = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('otr')]
    psc_zpics = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('psc_zpic')]
    racs = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('rac')]
    hearing_types = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('hearing_type')]
    procedure_codes = [data_tuple[0] for data_tuple in AggregateCase.get_distinct_values('procedure_code')]

    return render(request, 'predictive_framework/aggregate_home.html',
                  context={'fiscal_years': fiscal_years, 'claims': claims, 'request_types': request_types,
                           'appeal_categories': appeal_categories, 'medicare_parts': medicare_parts,
                           'requestor_types': requestor_types, 'states': states, 'otrs': otrs, 'psc_zpics': psc_zpics,
                           'racs': racs, 'hearing_types': hearing_types, 'procedure_codes': procedure_codes})


def predict(request):
    form = PredictForm(request.POST)

    if not form.is_valid():
        return render(request, 'predictive_framework/predict_home.html', context={'form': PredictForm})

    # predict
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    user_input = pd.read_csv(os.path.join(settings.BASE_DIR, 'predictive_framework/model/defaultuserinput.csv'))
    data = form.cleaned_data

    vector = process_data(int(data['claims']), data['appeal_category'], data['medicare_part'], data['requestor_type'],
                          data['state'], data['psc_zpic'], data['rac'], data['procedure_code'], user_input)

    favorable = float(model.predict_proba(vector)[0, 1]) * 100
    unfavorable = 100 - favorable
    return JsonResponse({'favorable': favorable, 'unfavorable': unfavorable})


def aggregate(request):
    args = {}
    for key, value in request.POST.items():
        args[key] = value

    dic = AggregateCase.get_mean_favorable_scores(args)

    if dic['disposition__avg'] is not None:
        favorable = float(dic['disposition__avg']) * 100
        unfavorable = 100 - favorable
        is_empty = False

    else:
        favorable = INITIAL_RATE
        unfavorable = INITIAL_RATE
        is_empty = True

    return JsonResponse({'favorable': favorable, 'unfavorable': unfavorable, 'is_empty': is_empty})


def assignClaims(c):
    for i in range(1, len(BINS)):
        if c < BINS[i]:
            level = "level{}".format(i - 1)
            return level
    return "level8"


def process_data(claims, appeal_category, medicare_part, requestor_type,
                 state, psc_zpic, rac, procedure_code, user_input):

    col_names = user_input.columns

    if 'Requestor Type_' + requestor_type in col_names:
        user_input['Requestor Type' + "_" + requestor_type] = 1

    if 'Medicare Part_' + medicare_part in col_names:
        user_input['Medicare Part_' + medicare_part] = 1

    if 'Appeal Category_' + appeal_category in col_names:
        user_input['Appeal Category_' + appeal_category] = 1

    if 'State_' + state in col_names:
        user_input['State_' + state] = 1

    if 'PSC/ZPIC_' + psc_zpic in col_names:
        user_input['PSC/ZPIC_' + psc_zpic] = 1

    if 'RAC_' + rac in col_names:
        user_input['RAC_' + rac] = 1

    if 'Procedure Code_' + procedure_code in col_names:
        user_input['Procedure Code_' + procedure_code] = 1

    level = assignClaims(claims)

    if 'Claims_' + level in col_names:
        user_input['Claims_' + level] = 1

    return user_input
