from django.shortcuts import render
def home(request):
    return render(request=request,
template_name="facebook/index")
def add(request):

    if request.method == 'POST':
        email=request.POST["email"]
        text=request.POST["text1"]
        print(email)
        print(text)

    return render(request=request,
template_name="facebook/facebook1")
