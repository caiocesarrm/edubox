from edubox.base.serializers import *
from edubox.base.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from edubox.base.serializers import *

class PostsListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CourseListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class AssignmentListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

