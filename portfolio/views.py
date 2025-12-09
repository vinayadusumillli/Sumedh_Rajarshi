from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from .models import AboutMe, Experience, BombayShark, Certification, CompanyLogo
from .forms import ContactForm


class HomeView(TemplateView):
    """
    Main portfolio landing page
    """
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get all portfolio content
        context['about_me'] = AboutMe.objects.first()
        context['experiences'] = Experience.objects.all()
        context['bombay_sharks'] = BombayShark.objects.first()
        context['certifications'] = Certification.objects.all()
        context['companies'] = CompanyLogo.objects.filter(display_on_homepage=True)
        context['contact_form'] = ContactForm()
        
        return context


def contact_submit(request):
    """
    Handle contact form submission
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 
                           'Thank you for your message! We will get back to you soon.')
            return redirect('home')
        else:
            messages.error(request, 
                         'There was an error with your submission. Please check the form.')
            # Return to home with form errors
            return render(request, 'portfolio/home.html', {
                'contact_form': form,
                'about_me': AboutMe.objects.first(),
                'experiences': Experience.objects.all(),
                'bombay_sharks': BombayShark.objects.first(),
                'certifications': Certification.objects.all(),
                'companies': CompanyLogo.objects.filter(display_on_homepage=True),
            })
    
    return redirect('home')
