from django.shortcuts import render
from .forms import FeedbackForm
# Create your views here.

def feed(request):
	form = FeedbackForm(request.POST or None)
	title = "Feedback Form"
	context = {
		'title' : title,
		'form' : form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		context = {
			'title' : "Thanks",
		}
		return render(request, "thanks.html",context)

	return render(request, "feedback.html",context)