from django.shortcuts import render
from .models import Inquiry, CourseRegistration
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.

class InquiryView(CreateView):
    model = Inquiry
    fields = ['first_name', 'last_name','email','comment']
    
    def get_success_url(self):
        return reverse('home')
    

class CourseRegistrationView(CreateView):
    model = CourseRegistration
    template_name = 'registrations.html'
    success_url = reverse_lazy('home')
    fields = ['first_name', 'last_name','email','phone', 'address', 'course']   
    
    # def get_success_url(self):
    #     return reverse('home')
    
    def get(self, request, *args, **kwargs):
        # Logic for handling GET request
        return render(request, self.template_name)