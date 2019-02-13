from django import forms
from django.forms.widgets import (	EmailInput,
									TextInput,
									Textarea,
									NumberInput,
									DateInput,
									Select
								)
from .models import (	RegisteredUser,
						class_choices,
						reference_choices,
						state_choices
					)


class RegisterForm(forms.ModelForm):

	class Meta:
		model = RegisteredUser

		fields = [	'email','full_name','father_name','date_of_birth',
					'school_name','student_class','contact_no','reference',
					'address','city','pin_code'
				]

		widgets = {
					'email' : EmailInput(
						attrs={
							'class' : 'form-control studen-email',
							'placeholder': 'Your Email'
						}
					),

					'full_name': TextInput(
						attrs = {
							'class':'form-control student-title',
							'placeholder':'Your title'
						}
					),

					'father_name':TextInput(
						attrs = {
							'class':'form-control student-father_name',
							'placeholder':"Father's Name"
						}
					),
					'date_of_birth':DateInput(
						attrs = {
							'class':'form-control student-d_o_b ',
							}
					),
					'school_name':TextInput(
						attrs= {
							'class':'form-control student-school'
							}
						),
					'student_class':Select(
						attrs={
							'class':'form-control student-class'
							}
						),
					'contact_no':NumberInput(
						attrs ={
							'class':'form-control student-contact'
							}
						),
					'reference':Select(
						attrs={
							'class':'form-control student-reference',
							'placeholder':'Website'
							}
						),
					'address':Textarea(
						attrs={
							'rows':2,
							'class':'form-control student-address',
							}
						),
					'city': Select(
						attrs = {
							'class':'form-control student_city',
							}
						),
					'pin_code':NumberInput(
						attrs={
							'class':'form-control student-pin_code',
							}
						),
					}



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
