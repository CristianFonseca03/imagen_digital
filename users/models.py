from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''
    User model
    '''
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    def number_invoices(self):
        '''Returns the number of invoices'''
        invoices=999
        return invoices
