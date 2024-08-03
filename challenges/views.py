from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def stage_one(request):
    if request.method == "POST":
        user_input = request.POST.get('code')
        if user_input == "GSNNCATTNFRNAOCF":
            return redirect('stage_two')
        else:
            return render (request, 'incorrect.html')
    return render(request, 'stage_one.html')

def stage_two(request):
    if request.method == "POST":
        user_input = request.POST.get('code')
        if user_input == "FCOANRFNTTACNNSG":
            return redirect('stage_three')
        else:
            return render (request, 'incorrect.html')
    return render(request, 'stage_two.html')

def stage_three(request):
    if request.method == "POST":
        user_input = request.POST.get('code')
        if user_input == "YVHTGKYGMMTVGGLZ":
            return redirect('stage_four')
        else:
            return render (request, 'incorrect.html')
    return render(request, 'stage_three.html')

def stage_four(request):
    if request.method == "POST":
        user_input = request.POST.get('code')
        if user_input == "YGGKVYGGHMLMTTZV":
            return redirect('stage_five')
        else:
            return render (request, 'incorrect.html')
    return render(request, 'stage_four.html')

def stage_five(request):
    if request.method == "POST":
        user_input = request.POST.get('code')
        if user_input == "BTTPEBTTSNONGGAE":
            return redirect('stage_six')
        else:
            return render (request, 'incorrect.html')
    return render(request, 'stage_five.html')

def stage_six(request):
    if request.method == "POST":
        user_input = request.POST.get('code')
        if user_input == "ZCVALNRCUYVZEPCP":
            return redirect('stage_seven')
        else:
            return render (request, 'incorrect.html')
    return render(request, 'stage_six.html')

def stage_seven(request):
    if request.method == "POST":
        user_input = request.POST.get('code')
        if user_input == "TENOLBHESYNTURER":
            return redirect('stage_eight')
        else:
            return render (request, 'incorrect.html')
    return render(request, 'stage_seven.html')

def stage_eight(request):
    if request.method == "POST":
        user_input = request.POST.get('code')
        if user_input == "GRABYOURFLAGHERE":
            return render (request, 'congratulations.html')
        else:
            return render (request, 'incorrect.html')
    return render(request, 'stage_eight.html')

# def congratulations(request):
