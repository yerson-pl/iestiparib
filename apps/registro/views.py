from django.shortcuts import render, redirect
from django.conf import settings

from .forms import PostulanteForm

from django.views.generic import TemplateView
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.


def send_email(email):
    context = {'email': email}

    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo de prueba',
        'Ichuña',
        settings.EMAIL_HOST_USER,
        [email],
        
    )

    email.attach_alternative(content, 'text/html')
    email.send()


class Index(TemplateView):
	template_name = 'index.html'
	def get(self,request,*args,**kwargs):
	
		return render(request, self.template_name)


def crearPostulante(request):
    if request.method == 'POST':
        postulante_form = PostulanteForm(request.POST or None, request.FILES or None)
        mail = request.POST.get('email')
        if postulante_form.is_valid():
            postulante_form.save()
            send_email(mail)
            return redirect('index')
        postulante_form = PostulanteForm()
        print(postulante_form)
    else:
    	postulante_form = PostulanteForm
    return render(request, 'index.html', {'postulante_form':postulante_form})