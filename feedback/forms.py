from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ["name", "contact_email", "contact_phone","feedback_text"]

	def clean_name(self):
		name = self.cleaned_data.get("name")
		return name


