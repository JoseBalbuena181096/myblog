from django.db import models
#apps third persons
from model_utils.models import TimeStampedModel

# Create your models here.
class Home(TimeStampedModel):
    """Modelo para datos de la pantalla principal"""
    title = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    youtube = models.TextField(blank=True, null=True)
    tiktok = models.TextField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    contact_email = models.EmailField('email de contacto', blank=True, null=True)
    phone = models.CharField('Telefono contacto', max_length=20)

    class Meta:
        verbose_name = 'Pagina principa'
        verbose_name_plural = 'Pagina princial'

    def __str__(self):
        return self.title
    

class Suscribers(TimeStampedModel):
    """Modelo para datos de suscriptores """
    
    email = models.EmailField()
    
    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'
    def __str__(self):
        return self.email
    
class Contact(TimeStampedModel):
        """Formulario de contacto """

        full_name = models.CharField('Nombres', max_length=60)
        email = models.EmailField()
        message = models.TextField()

        class Meta:
            verbose_name = 'Contacto'
            verbose_name_plural = 'Mensajes'

        def __str__(self):
            return self.full_name
        
