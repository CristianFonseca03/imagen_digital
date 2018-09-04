from django.db import models


class Person(models.Model):
    """
    Model from person
    """
    first_name = models.CharField('Nombres', max_length=255)
    last_name = models.CharField('Apellidos', max_length=255)
    address = models.CharField('Dirección', max_length=255)
    phone = models.CharField('Telefono',max_length=11)
    payment = models.DecimalField('Abono',max_digits=100,decimal_places=10)
    career = models.CharField('Carrera-Especialidad',max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
