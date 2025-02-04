
from django.shortcuts import render

from django.http import HttpResponse

from django.views import View
from .models import Book
class Another(View):

    books=Book.objects.filter(is_published=True)
    output=''
    for book in books:
        output+=f"We have book title {book.title} and book id {book.id}"
    def get(self,request):
        return HttpResponse(self.output)

def first(request):
    return render(request,'first_temp.html')