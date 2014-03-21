from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre = models.TextField(max_length=60)
    codigo = models.TextField()
    creditos = models.IntegerField()
    
    
    def __unicode__(self):
        return self.nombre + " con codigo:" + self.codigo
    
class Docente(models.Model):
    nombre = models.TextField()
    email = models.EmailField()
    
    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.email)
    
class Estudiante(models.Model):
    usuario = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.usuario.username

    
class CursoDocente(models.Model):
    curso = models.ForeignKey(Curso)
    docente = models.ForeignKey(Docente)
    estudiantes = models.ManyToManyField(Estudiante)
    anio = models.IntegerField()

class Asistencia(models.Model):
    curso_docente = models.ManyToManyField(CursoDocente)
    presentes = models.ManyToManyField(Estudiante)
    fecha = models.DateField()
        
    