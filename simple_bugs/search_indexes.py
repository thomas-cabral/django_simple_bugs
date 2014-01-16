__author__ = 'Thomas'
import datetime
from haystack import indexes
from .models import Case


class CaseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    created_on = indexes.DateTimeField(model_attr='created_on')

    def get_model(self):
        return Case

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_on__lte=datetime.datetime.now())