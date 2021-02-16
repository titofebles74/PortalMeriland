from django.forms import ModelForm
from meriland.models import Comentarios

class ComentariosForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nombre', 'email', 'telefono', 'mensaje', 'motivo']

