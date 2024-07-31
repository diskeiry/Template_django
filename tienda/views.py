from django.http import HttpResponse
from django.template import Template, Context

def renderizarHome(request):
    pantilla_home = open('C:/Users/PC/OneDrive/Escritorio/projectoDjango/tienda/tienda/templates/home.html')
    template = Template(pantilla_home.read())
    pantilla_home.close()
    contexto = Context()#el contexto recibe los valores que se van a ver en el html
    documento = template.render(contexto)
    return HttpResponse(documento)
    