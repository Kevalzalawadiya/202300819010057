from django.db import models

        
# Create your models here.
class Inquiry(models.Model):
    InquiryStatus = (
        (0, 'Initilize'),
        (1, 'In progress'),
        (2, 'Client Approval'),
        (3, 'Close'),
        (4, 'Re-Open')
    )
    
        
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    comment = models.TextField()
    status = models.IntegerField(choices=InquiryStatus , default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    
class CourseRegistration(models.Model):
    Courses = (
        (0, "Basics to Programming and project management tools"),
        (1, "Advance Python / Django"),
        (2, "Full Stack API & React JS"),
        (3, "Mobile Development with Flutter"),
        (4, "Artificial Intelligence and Machine Learning"),
        (5, "AWS Cloud Engineering")
    )
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    course = models.IntegerField(choices=Courses , default=0)
    address = models.TextField(max_length=600)
    reference_by = models.CharField(max_length=100, blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)
    