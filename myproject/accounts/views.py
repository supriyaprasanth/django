from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	numbers = [1,2,3,4,5]
	name = 'Supriya Prasanth'
	args = {'myName': name , 'numb': numbers} 
	return render(request,'accounts/home.html',args)
	#return render(request,'accounts/login.html')