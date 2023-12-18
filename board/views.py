from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HttpResponse

# Create your views here.


# def index(request):
#    return HttpResponse("Board index page.")

# 다음과 같이 수정
from .models import Board
from django.views import generic
from django.urls import reverse_lazy

def index(request):
    board_list = Board.objects.order_by('-create_date')
    context = {'board_list' : board_list}
    return render(request, 'board/board_list.html', context)

# http://localhost:8000/board/1
def detail(request, board_id):
    board = Board.objects.get(id = board_id)
    context = {'board' : board}
    return render(request, 'board/board_detail.html', context)

# http://localhost:8000/board/create
class create(generic.CreateView):
    model = Board
    fields = ['subject', 'content','create_date']
    success_url = reverse_lazy('board:list')
    template_name_suffix = '_create'