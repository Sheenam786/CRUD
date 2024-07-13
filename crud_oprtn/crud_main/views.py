from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import contactform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q


@login_required(login_url="/loginn/")
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        date = request.POST.get('date')
        cs = contactform(name=name, email=email, number=number, date=date)
        cs.save()
        return redirect('show_data')
    return render(request, 'index.html')



@login_required(login_url="/loginn/")
def show_data(request):
    if 'srch' in request.GET:
        srch = request.GET['srch']
        search_filter = Q(name__icontains=srch) | Q(email__icontains=srch) | Q(number__icontains=srch) | Q(date__icontains=srch)
        show_table_data = contactform.objects.filter(search_filter)
    else:    
        show_table_data = contactform.objects.all()
    context = {'show_table_data': show_table_data}
    return render(request, 'table.html', context)


def edit_btn(request, id):
    ed = contactform.objects.get(id=id)
    if request.method == 'POST':
        ed.name = request.POST.get('name')
        ed.email = request.POST.get('email')
        ed.number = request.POST.get('number')
        ed.date = request.POST.get('date')
        ed.save()
        return redirect('show_data')
    return render(request, 'edit.html', {'ed': ed})


def delete_btn(request, id):
        delt = contactform.objects.get(id=id)
        delt.delete()
        return redirect('show_data')


@login_required(login_url="/loginn/")
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        passwrd = request.POST.get('passwrd')
        # cpasswrd = request.POST.get('cpasswrd')

        # if len(name) <= 5 or name.isdigit() or  len(lname) <= 5 or lname.isdigit():
        #     messages.error(request, 'Invalid Name Try Again')
        #     return redirect('register')
        # if passwrd != cpasswrd:
        #     messages.error(request, 'Your password doesnt match Try again..')
        #     return redirect('register')

        
        if User.objects.filter(email=email).exists() or User.objects.filter(last_name=lname).exists():
            messages.error(request, 'Email already exists. Please try again with another Email!')
            return render(request, 'Registration.html')
        my_user = User.objects.create_user(username=email, password=passwrd, first_name=name, last_name=lname)
        my_user.save()
        messages.success(request, 'Your data has been saved successfully!')
        return redirect('loginn')
    return render(request, 'Registration.html')


def loginn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passwrd = request.POST.get('passwrd')

        user = authenticate(request, username=email, password=passwrd)
        if user is not None:
            login(request, user)
            return redirect('show_data')
        else:
            messages.error(request, 'Incorrect email or password.')
             
    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/loginn/')