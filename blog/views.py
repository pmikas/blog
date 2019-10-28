from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	return render(request, 'blog/home.html')

def pt_cv(request):
	return render(request, 'blog/resume/pt_cv.html')

def en_cv(request):
	return render(request, 'blog/resume/en_cv.html')

def projects(request):
	return render(request, 'blog/projects.html')

def ml(request):
	return render(request, 'blog/ml.html')

def reg_diamonds(request):
	return render(request, 'blog/ml/diamonds.html')

def clas_digit_reco(request):
	return render(request, 'blog/ml/digit_reco.html')

def clas_mushroom(request):
	return render(request, 'blog/ml/mushroom.html')

def cs(request):
	return render(request, 'blog/cs.html')

def cs_mis(request):
	return render(request, 'blog/cs/mis.html')

def cs_agile(request):
	return render(request, 'blog/cs/agile.html')

def cs_tsql(request):
	return render(request, 'blog/cs/tsql.html')

def cs_ml(request):
	return render(request, 'blog/cs/csml.html')

def django(request):
	return render(request, 'blog/cs/django.html')

def surf(request):
	return render(request, 'blog/surf.html')

def contact(request):
	return render(request, 'blog/contact.html')