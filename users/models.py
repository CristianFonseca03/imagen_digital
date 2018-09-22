from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''
    User model
    '''
    def number_invoices(self):
        '''Returns the number of invoices'''
        invoices=999
        return invoices
