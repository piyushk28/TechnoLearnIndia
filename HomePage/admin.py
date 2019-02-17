from django.contrib.auth.models import Group
from django.contrib import admin

from .models import HomePage, HomeImage, RegisteredUser


admin.site.unregister(Group)
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
	list_display = ['title', 'about_title_first', 'is_active', 'created']

	list_filter = ('created',)

	fields = [	'title',
				('about_title_first','about_first'),
				('about_title_second','about_second'),
				('contact_no','contact_email'),
				('facebook_url','instagram_url', 'twitter_url'),
				'is_active','created',
				]

	readonly_fields =['created',]

	search_fields= ['title','id']

admin.site.register(HomePage,HomeAdmin)



class ImageAdmin(admin.ModelAdmin):
    list_display = ['home_page', 'created']

    fields = ['home_page','image', 'created',]
    readonly_fields = ['created',]

    title = ['home_page','id']

admin.site.register(HomeImage,ImageAdmin)

class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'city', 'contact_no']

    list_filter=('created',)

    title = ['email','full_name','contact_no','id']

    fields = [	'email','contact_no',
   				'full_name','father_name',
   				'date_of_birth','address',
   				'city','pin_code',
   				'school_name','student_class',
   				'reference','created'
   			]
    readonly_fields = [	'email','contact_no',
    					'full_name','father_name',
    					'date_of_birth','address',
    					'city','pin_code',
    					'school_name','student_class',
    					'reference','created'
    				]


admin.site.register(RegisteredUser,RegisteredUserAdmin)
