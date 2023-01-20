from django import forms
from .models import Course

class CourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = '__all__'
		labels = {
			'course_id': 'COURSE ID',
			'c_name': 'COURSE NAME',
			'c_fees':'COURSE FEES'
		}
