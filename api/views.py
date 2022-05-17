
from api.models import Article
from .serializers import ArticleSerializer,UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

#6
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class =ArticleSerializer
    # Token...
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =UserSerializer














































# from django.shortcuts import render, HttpResponse
# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import APIView
# from rest_framework import generics,mixins
# from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
# csrf when without TOKEN



# 5
'''
class ArticleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,
                     mixins.CreateModelMixin,mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class =ArticleSerializer
 '''   

# 4
'''
class ArticleViewSet(viewsets.ViewSet):
    def list(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many = True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
    
# 3
"""
class ArticleList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

    
class ArticleDetails(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # importent without can't see the field 'id'
    lookup_field = 'id'
    
    def get(self, request,id):
        return self.retrieve(request,id=id)
    
    def put(self, request,id):
        return self.update(request,id=id)
    
    def delete(self, request,id):
        return self.destroy(request,id=id)
"""

# 2
'''
class ArticleList(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ArticleDetails(APIView):
    def get_object(self,id):
      try:
        #   objects.get(param)
        return Article.objects.get(id=id)

      except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
    
    def put(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        article = self.get_object(id)
        print(article)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
'''

# 1
'''
@api_view(['GET','POST'])
def article_list(request):
    # get all articles
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # get article by id
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # update aticle by id
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == "DELETE":
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
'''
