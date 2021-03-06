from django.shortcuts import render
from django.views import generic
from sales.models import Game

# Create your views here.

class GameListView(generic.ListView):
    '''
    This class renders the game list
    '''
    template_name = 'pages/game-list.html'
    context_object_name = 'game_list'
    paginate_by = 24
    model = Game
