from django.shortcuts import render


from .models import User
from .forms import (
    CreateUserForm,
    UserNameForm,
    UserCsvForm,
)
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseForbidden

from django.http import HttpResponse

from .csv import read_and_decode_csv, csv_rows_to_db
#users = []



def get_users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }

    return render(
        request,
        template_name='users.html',
        context=context,
    )


def add_user(request):

    form = CreateUserForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = User(
                username=form.cleaned_data['username'],
                e_mail=form.cleaned_data['e_mail'],
            )

            user.save()

            #users.append(user)

            context = {
                'user': user,
            }

            return render(
                request,
                template_name='user.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_user.html',
        context=context,
    )

def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
    }

    return render(
        request,
        template_name='user.html',
        context=context,
    )


def filtred_users_by_username(request):

    #form = UserNameForm(request.POST or None)
    form = UserNameForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user_names = form.cleaned_data['username']
            #user_names = form.cleaned_data['username']

            users = User.objects.filter(username = user_names)
            print(user_names)
            print(users)
            print('usrname')
            if not users:
                #pass
                return HttpResponseForbidden('Users not found')

            context = {
                'users': users,
            }
            #print('forma')
            return render(
                request,
                template_name='users.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_user.html',
        context=context,
    )


def add_user_csv(request):

    form = UserCsvForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':

        if form.is_valid():
            decoded_csv = read_and_decode_csv(request.FILES['csv'])
            csv_rows_to_db(decoded_csv)
            #return HttpResponse('OK')


    return render(
        request,
        template_name='add_user.html',
        context={'form': form}
    )