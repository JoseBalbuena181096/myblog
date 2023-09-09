from applications.home.models import Home

# Proceso para recuperar telefono y correo del registro
def home_contact(request):
    home = Home.objects.latest('created')

    return {
        'phone': home.phone,
        'correo': home.contact_email,
        'youtube': home.youtube,
        'tiktok': home.tiktok,
    } 
     