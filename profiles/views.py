from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from .forms import UserForm
from .models import Profile


def user_join(request):

    if request.method == 'GET':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            prof = Profile()
            prof.user = user
            
            # FIXME: UserForm에 gender필드를 지정하였고, POST로 넘어오는 것을 확인하였음에도
            # form.gender로 접근하면 에러 발생
            # 'UserForm' object has no attribute 'gender'

            # prof.gender = form.gender
            prof.gender = request.POST['gender']
            prof.save()

            return redirect('blog:list_posts')
        else:
            messages.add_message(request, messages.ERROR, form.errors)

    return render(request, 'user_join.html', {'form':form})