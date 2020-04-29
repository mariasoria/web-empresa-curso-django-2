from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

# esta funcion nos permite manipular 
# 1 - tanto el formulario que se muestra
# 2 - como la información que se envía a través de él (el formulario cumplimentado)
def contact(request):
    
    # 1 - definimos la plantilla del formulario vacía para que la muestre cada vez
    contact_form = ContactForm()

    # 2 - Ahora manipulamos el request (que contiene la info enviada a traves del form)
    # tenemos que asegurarnos de que la peticion es de tipo POST, ya que lo normal es que sea GET
    # Podemos verlo en consola
    # print("Tipo de peticion: {}".format(request.method))
    # Comprobamos si es POST
    if request.method == "POST":
        # Recuperamos automaticam+ la información enviada a través del formulario
        contact_form = ContactForm(data=request.POST)
        # Devolvera True si todos los campos son correctos y 
        # asignamos cada campo del form a cada variable
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            # Después de configurar en settings.py el correo de prueba que voy a usar
            # Y con la información del formulario recuperada podemos mandar el email
            email = EmailMessage(
                "H4 Idiomas y ocio: Nuevo mensaje de pagina web", 
                "De {} <{}>\n\nEscribio\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["maria.it3@gmail.com"],
                reply_to= [email]
            )
            try:
                email.send()
                # Informar al usuario de que su email se ha enviado correctamente
                # redireccionando el email a la pagina contact pero enviando una variable OK a través de GET
                # return redirect('/contact/?ok')
                
                # mejor hacerlo con reverse (por si cambiara la url del html), pasándole:
                # - el path de contact
                # - la cadena que queremos enviarle
                return redirect(reverse('contact')+"?ok")
            
            except:
                #algo no ha ido bien, redireccionamos a FAIL
                return redirect('/contact/?fail')
                
    return render(request, "contact/contact.html", {'form': contact_form})