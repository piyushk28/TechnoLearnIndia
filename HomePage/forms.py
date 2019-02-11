from django import forms
from django.forms.widgets import EmailInput,TextInput,NumberInput
from .models import (RegisteredUser,class_choices,reference_choices,state_choices)


class RegisterForm(forms.ModelForm):

	class Meta:
		model = RegisteredUser

		fields = [	'email','full_name','father_name','date_of_birth',
					'school_name','student_class','contact_no','reference',
					'address','city','pin_code'
				]

        		

	def clean_contact_no(self):
		num  =self.cleaned_data.get('contact_no')

		if num<1111111111:
			raise forms.ValidationError('Invalid Contact Number')	

		if num>9999999999:
			raise forms.ValidationError('Invalid Contact Number, Try removing any country code from the Number......')


		return num


	def clean_pin_code(self):
		pin = self.cleaned_data.get('pin_code')

		if pin<=99999 or pin>=1000000:
			raise forms.ValidationError('Invalid Pin-Code, Please provide your correct Pin-Code')

		return pin
