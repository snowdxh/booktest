from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status,decorators
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from django.utils import timezone
from datetime import timedelta
# Create your views here.

class BookView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    # 借书api
    @decorators.action(detail=True, methods=['POST'])
    def give_book(self,request,pk=None):
        book = self.get_object()
        if book.is_break:
            return Response({'message':'Book is already given'},status=status.HTTP_400_BAD_REQUEST)
        user = request.data.get('user_id')
        book.user_id = user
        book.is_break = True
        book.return_date = timezone.localtime(timezone.now()) + timedelta(days=30)
        print(book.return_date)
        book.save()
        return Response({'message':'Book is given'},status=status.HTTP_200_OK)

    # 还书api
    @decorators.action(detail=True, methods=['POST'])
    def give_break_book(self,request,pk=None):
        book = self.get_object()
        if not book.is_break:
            return Response({'message':'Book is not given'},status=status.HTTP_400_BAD_REQUEST)
        if book.return_date < timezone.now():
            return Response({'message':'Book is overdue, please concat admin'},status=status.HTTP_400_BAD_REQUEST)
        book.is_break = False
        book.user_id = 0
        book.return_date = timezone.now()
        book.save()
        return Response({'message':'Book is returned'},status=status.HTTP_200_OK)


