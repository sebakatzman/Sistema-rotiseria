from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.views.generic import CreateView, ListView
from rotiseria.models import Mapa

=======
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
>>>>>>> 186ac17ff88c30247a19ca22abae5481b317eba3
def mapa(request):
    return render (request,'Repartidor/index.html')

class ListarDatosMapa (ListView):
    model = Mapa
    template_name = "Repartidor/index.html"

    def get(self, request, *args, **kwargs):
        mapas = Mapa.objects.all()
        print(mapas)
        context_dict = {'mapas': mapas}
        return render(request, self.template_name, context=context_dict)