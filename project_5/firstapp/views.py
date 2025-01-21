from django.shortcuts import render
from .forms import ContactForm,studentData,PasswordValidation

# Create your views here.
def index(request):
    data = [{
"userId": 1,
"id": 1,
"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
"body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
},
{
"userId": 1,
"id": 2,
"title": "qui est esse",
"body": "est rerum tempore vitae sequi sint nihil reprehenderit dolor beatae ea dolores neque fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis qui aperiam non debitis possimus qui neque nisi nulla"
},
]
    return render(request, 'index.html', {'data': data})

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        selcet = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'select': selcet})
    return render(request, 'about.html')

def submit_form(request):
    return render(request, 'form.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./firstapp/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request, 'django-form.html', {'form' : form})

def StudentForm(request):
    if request.method == 'POST':
        form = studentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = studentData()
    return render(request, 'django-form.html', {'form' : form})

def Password_Validation(request):
    if request.method == 'POST':
        form = PasswordValidation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidation()
    return render(request, 'django-form.html', {'form' : form})