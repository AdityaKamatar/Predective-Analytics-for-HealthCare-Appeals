from django.db import models
from django.db.models import Avg

# Create your models here.


class AggregateCase(models.Model):
    fiscal_year = models.CharField(max_length=4)
    claims = models.IntegerField()
    request_type = models.CharField(max_length=200)
    appeal_category = models.CharField(max_length=200)
    medicare_part = models.CharField(max_length=200)
    requestor_type = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    otr = models.CharField(max_length=200)
    psc_zpic = models.CharField(max_length=200)
    rac = models.CharField(max_length=200)
    hearing_type = models.CharField(max_length=200)
    procedure_code = models.CharField(max_length=200)
    disposition = models.CharField(max_length=1)

    @staticmethod
    def get_distinct_values(attribute):
        return AggregateCase.objects.order_by(attribute).values_list(attribute).distinct()

    @staticmethod
    def get_mean_favorable_scores(args):
        return AggregateCase.objects.filter(**args).aggregate(Avg('disposition'))
