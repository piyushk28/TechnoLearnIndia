from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import Http404
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


class HomePageView(DetailView):
	model = HomePage
	template_name='index.html'

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')

		instance = get_object_or_404(HomePage,pk=pk,is_active= True)

		return instance


def register_user(request):
	form = RegisterForm(request.POST or None)
	context = {'form':form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('home_redirect')
	return render(request,'HomePage/register.html', context)

