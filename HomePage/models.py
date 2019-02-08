from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
import os, random

class HomePage(models.Model):
	title					= models.CharField(max_length=30)
	about_title_first		= models.CharField(max_length=70)
	about_first				= models.TextField(max_length=300)
	about_title_second		= models.CharField(max_length=70)
	about_second 			= models.TextField(max_length=300)
	contact_no				= models.BigIntegerField()
	conatct_email			= models.EmailField()
	facebook_url 			= models.URLField(blank= True, null= True, help_text= 'Optional,  If added respective site icon will be shown on the home page')
	instagram_url 			= models.URLField(blank= True, null= True, help_text= 'Optional,  If added respective site icon will be shown on the home page')
	twitter_url 			= models.URLField(blank= True, null= True, help_text= 'Optional,  If added respective site icon will be shown on the home page')
	slug					= models.SlugField(blank = True, null = True)


	def __str__(self):
		return self.id


def pre_save_slug_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_slug_receiver, sender= HomePage)

class HomeImage(models.Model):

	def get_filename_ext(filepath):
	    base_name=os.path.basename(filepath)
	    name, ext=os.path.splitext(base_name)
	    return name, ext

	# To return a  new  path for  image
	def upload_image_path(instance,filename):
	    new_filename=random.randint(1,2345356465)
	    name, ext =  get_filename_ext(filename)
	    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	    return 'student/{new_filename}/{final_filename}'.format(
	            new_filename=new_filename,
	            final_filename=final_filename
	            )

	home_page	= models.ForeignKey(HomePage, on_delete= models.CASCADE)
	image 		= models.ImageField(upload_to=upload_image_path)

	def __str__(self):
		return self.id



class RegisteredUser(models.Model):

	class_choices 	=(	('5th',	'V'),
						('6th', 'VI'),
						('7th', 'VII'),
						('8th', 'VIII'),
						('9th', 'IX'),
						('10th', 'X'),
						('11th', 'XI'),
						('12th', 'XII'),
						('Other', 'Other'),
		)
	other_ref_value ='Other'

	reference_choices	= ( ('social_site','Social Site'),
							('pamphlet', 'Pamphlet'),
							('website', 'Website'),
							('friend','Friend'),
							('Other', other_ref_value),
		)

	state_choices = (	('Delhi', 'Delhi'),
						('Gurgaon','Gurgaon'),
						('Noida','Noida'),
						('Faridabad ', 'Faridabad '),
						('Ghaziabad', 'Ghaziabad'),
						('Jaipur', 'Jaipur'),
						('Other','Other')
	)
 


	email 			= models.EmailField(unique= True)				
	contact_no		= models.BigIntegerField()
	full_name		= models.CharField(max_length= 60)
	father_name		= models.CharField(max_length= 60)
	date_of_birth	= models.DateField()
	address			= models.TextField(max_length= 250)
	city 			= models.CharField(choices=state_choices,max_length=255)
	pin_code		= models.PositiveIntegerField()
	school_name		= models.CharField(max_length= 100)
	student_class	= models.CharField(max_length=15,choices=class_choices)
	reference		= models.CharField(max_length= 50, choices = reference_choices)

	def __str__(self):
		return self.email

