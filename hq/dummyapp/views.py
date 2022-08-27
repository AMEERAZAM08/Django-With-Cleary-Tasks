from django.shortcuts import render
from django.http import HttpResponse
#json 
from  .models import Test
from django.http import JsonResponse
from  django.views.decorators.csrf import csrf_exempt
from  .model_Iris import  predict
# model=
# Create your views here.
@csrf_exempt
def add(request):
    a = request.POST['a']
    b = request.POST['b']
    c = int(a) + int(b)
    return JsonResponse({'result':c})


#intesrt data into Test 
@csrf_exempt
def insert(request):
    name = request.POST['name']
    age = request.POST['age']   
    image = request.FILES['image']

    Test.objects.create(name=name,age=age,user_image=image)
    return JsonResponse({'result':'success'})


#show data from Test
@csrf_exempt
def show(request):
    data = Test.objects.all()
    return JsonResponse({'result':list(data.values())})

@csrf_exempt
def show_by_age(request):
    age = request.POST['age']
    #find all  age equal to age
    data = Test.objects.filter(age=age)
    return JsonResponse({'result':list(data.values())})

def about(request):
    return HttpResponse("<h1>About</h1>")

def homepage(request):
    return render(request,'homepage.html')



@csrf_exempt
def predict_model(request):
    sepal_length = request.POST['sepal_length']
    sepal_width = request.POST['sepal_width']
    petal_length = request.POST['petal_length']
    petal_width = request.POST['petal_width']
    print(sepal_length,sepal_width,petal_length,petal_width)
    result = predict(sepal_length,sepal_width,petal_length,petal_width)
    return JsonResponse({'result':result})