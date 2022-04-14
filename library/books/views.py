from rest_framework import viewsets
from rest_framework import permissions
import base64
from rest_framework.response import Response
from library.books.serializers import *

# # class ThingViewSet(viewsets.ModelViewSet):
# #     queryset = Thing.objects.all().order_by('id')
# #     serializer_class = ThingSerializer
# #     def create(self, request, *args):
# #         name = request.data['name']
# #         image = base64.b64encode(request.data['image'])
# #         sz = serializer_class.create(name = name, image = image)
# #         print('SERIALIZER', sz)
# #         response = Response()

# #         response.data = {
# #             'name': name,
# #             # 'image': 
# #         }

# #         return response

#     permission_classes = []

class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all().order_by('id')
    serializer_class = ThingSerializer
    permission_classes = []

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = []

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = []

class BooksAuthorsViewSet(viewsets.ModelViewSet):
    queryset = BooksAuthors.objects.all()
    serializer_class = BooksAuthorsSerializer
    permission_classes = []

class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
    permission_classes = []

class LanguageViewSet(viewsets.ModelViewSet):

    queryset = Language.objects.all().order_by('id')
    serializer_class = LanguageSerializer
    permission_classes = []

class EditorialViewSet(viewsets.ModelViewSet):

    queryset = Editorial.objects.all().order_by('id')
    serializer_class = EditorialSerializer
    permission_classes = []
    
    