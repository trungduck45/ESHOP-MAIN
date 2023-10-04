from django.shortcuts import render
def send_mail(request):
    return render(request,'send_mail.html')