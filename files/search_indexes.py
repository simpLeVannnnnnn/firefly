import datetime
from haystack import indexes
from files.models import File
 
class FileIndex(indexes.SearchIndex, indexes.Indexable):
    
    text = indexes.CharField(document=True, use_template=True)

    title = indexes.CharField(model_attr='title')
    introduction = indexes.CharField(model_attr='introduction')
    developer = indexes.CharField(model_attr='developer')
    support_system = indexes.CharField(model_attr='support_system')
    language = indexes.CharField(model_attr='language')
    
    def get_model(self):
        return File
 
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()