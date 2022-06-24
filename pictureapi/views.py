from warnings import filters
from jmespath import search
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import PictureModel
from .serializers import PictureSerializer
from rest_framework import filters



class PictureView(viewsets.ModelViewSet):
    queryset = PictureModel.objects.all()
    serializer_class = PictureSerializer
    parser_classes = [MultiPartParser,FormParser]
    filter_backends = [filters.SearchFilter]
    search_fileds = ['=title']

