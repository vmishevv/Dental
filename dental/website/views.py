from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'pages/index.html', {})


def about(request):
    return render(request, 'pages/about.html', {})


def service(request):
    return render(request, 'pages/service.html', {})


def pricing(request):
    return render(request, 'pages/pricing.html', {})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name'] 
		message_email = request.POST['message-email'] 
		message = request.POST['message'] 

		send_mail(
			message_name,
			message,
			message_email,
			['dentalc.info@gmail.com'],
			fail_silently=False,
		)


		return render(request, 'pages/contact.html', {})

	
	else:
		return render(request, 'pages/contact.html', {})


def blog(request):
    return render(request, 'pages/blog.html', {})


def blog_details(request):
    return render(request, 'pages/blog-details.html', {})
