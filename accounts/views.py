from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from .forms import StudentRegistrationForm, LoginForm, DocumentUploadForm
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StudentProfile, Document
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
@login_required(login_url='/login')
def home(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.student = request.user.studentprofile
            document.save()
            messages.success(request, "You've successfully sent your documents! Wait for the approval.")
            return redirect('home')
        
    else:
        form = DocumentUploadForm()
    return render(request, 'accounts/dashboard.html', {'form': form})

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def list_docs(request):
    docs = Document.objects.all()
    context = {'docs': docs}
    return render(request, 'accounts/list_docs.html', context)

def user_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# login page
def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


@receiver(post_save, sender=User)
def create_or_update_student_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'studentprofile'):
        StudentProfile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)
    elif hasattr(instance, 'studentprofile'):
        instance.studentprofile.first_name = instance.first_name
        instance.studentprofile.last_name = instance.last_name
        instance.studentprofile.save()


# @receiver(post_save, sender=StudentProfile)
# def create_document_for_student(sender, instance, created, **kwargs):
#     instance.save()
#     # if created:
#     #     Document.objects.create(student=instance)