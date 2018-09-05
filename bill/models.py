from django.db import models
from person.models import Person
from django.contrib.auth.models import User

class Bill(models.Model):
    """
    Models from bill
    """
    event_name = models.CharField('Nombre del evento', max_length=255)
    seller = models.OneToOneField(User,verbose_name='Vendedor',on_delete=models.PROTECT)
    number_book = models.IntegerField('Numero de talonario')
    person = models.OneToOneField(Person,verbose_name='Cliente',on_delete=models.PROTECT)
    number_bill = models.IntegerField('Numero de factura')
    quantity = models.IntegerField('Cantidad de fotos')
    sale_date = models.DateField('Fecha de venta')
    event_date = models.DateField('Fecha del evento')
    observations = models.TextField('Observaciones')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return self.number_bill