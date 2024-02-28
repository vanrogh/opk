from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.forms import ValidationError
import magic

ext_validator = FileExtensionValidator(['png', 'jpg', 'pdf'])

def validate_file_maintype(file):
    accept = ['image/png', 'image/jpg', 'application/pdf']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    print(file_mime_type)
    if file_mime_type not in accept:
        raise ValidationError('File type not supported')


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

class Document(models.Model):
    STATUS_CHOICES = (
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    document_passport = models.FileField(upload_to='uploads/', validators=[ext_validator, validate_file_maintype], max_length=256)
    school_documents = models.FileField(upload_to='uploads/', validators=[ext_validator, validate_file_maintype], max_length=256)
    upload_photo = models.ImageField(upload_to='uploads/', max_length=256)
    upload_certificate = models.FileField(upload_to='uploads/', validators=[ext_validator, validate_file_maintype], max_length=256)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"