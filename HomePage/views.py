from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404,JsonResponse,HttpResponse
from .models import HomePage, HomeImage, RegisteredUser
from .forms import RegisterForm

def home_redirect_view(request):
	try:
		instance = HomePage.objects.get(is_active= True)


	except HomePage.DoesNotExist:
		raise Http404("Server Error")

	except HomePage.MultipleObjectsReturned:
		qs= HomePage.objects.filter(is_active= True)
		instance = qs.first()


	return redirect(reverse('homepage:home', kwargs={'pk':instance.pk}))


# class HomePageView(DetailView):
# 	model = HomePage
# 	template_name='index.html'

# 	def get_object(self, *args, **kwargs):
		

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomePageView, self).get_context_data(*args, **kwargs)

		




def home_view(request, *args, **kwargs ):
	pk = kwargs.get('pk')

	instance = get_object_or_404(HomePage,pk=pk,is_active= True)
	context={'object': instance}

	form = RegisterForm(request.POST or None)

	context['form']= form
	if request.method == 'POST':
		print(request.method)
		if form.is_valid():
			form.save()
			# print('inside')
			if request.is_ajax():
				return JsonResponse({'success':'true'})
			return redirect('home_redirect')
		else:
			error = form.errors
			if request.is_ajax():
				return JsonResponse({'error':error})


	image_qs=HomeImage.objects.filter(home_page=instance).first()
	# if(image_qs.count <= 6):
	# 	context['image']=image_qs
	
	# else:
	# 	context['image'] = image_qs[0:6]

	if image_qs:
		context['image']=image_qs
	return render(request,'index.html',context)
