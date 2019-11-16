from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.



gain_program = {
    'Texas Method' : 'https://www.t-nation.com/training/texas-method', 
    'Madcow 5x5' : 'https://stronglifts.com/madcow-5x5/',
    '5/3/1' : 'https://www.t-nation.com/workouts/531-how-to-build-pure-strength',
}

cardio = {
    'Running' : 'https://rockay.com/blog/how-to-go-from-couch-to-5k-training-plan/',
    'Swimming' : 'https://www.liveabout.com/workout-plan-for-beginner-swimmers-3169364',
}

fat_loss = {
    'Starting Strength' : 'https://startingstrength.com/get-started/programs',
    'Strong Lifts' : 'https://stronglifts.com/5x5/',
    'All Pro\'s' : 'https://forum.bodybuilding.com/showthread.php?t=4195843',

}
def index(request):

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'fitboi_photo/index.html', {'form': form})
    # context = {'test': 'HELLO THIS IS A TEST'}
    # return render(request, 'fitboi_photo/index.html', context)


def user_image_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'fitboi_photo/user_image_form.html', {'form': form})


def success(request):
    return render(request, 'fitboi_photo/success.html')
    # return HttpResponse('successfully uploaded')
    # context = {'test' : 'HELLO THIS IS A TEST'}
    # return render(request, 'fitboi_photo/index.html', context)

# def submit(request):
#     return HttpResponse("Information Submitted")

# def result(request):
#     return HttpResponse("Results")
