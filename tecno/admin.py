from django.contrib import admin
from tecno.models import Asistencia, Curso,CursoDocente,Docente,Estudiante

# Register your models here.

admin.site.register(Asistencia)
admin.site.register(Curso)
admin.site.register(CursoDocente)
admin.site.register(Docente)
admin.site.register(Estudiante)