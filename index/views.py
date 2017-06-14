from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.views.generic import View
from .models import StarDetail, Comment
from account.models import BaskUser
from django.contrib.auth.models import User
import json

from .forms import CommentForm, StarDetailForm

def index(requests):
    return render(requests,"index.html")

def detail(requests):
    forms = CommentForm()
    star_id = requests.GET['id']
    login = requests.user
    islogin = 1
    try:
        user = BaskUser.objects.get(user=user)
    except:
        islogin = 0
    comment = Comment.objects.filter(article__id=star_id)
    info = [{'nick': BaskUser.objects.get(user=User.objects.get(email=i.user_email)).nick,'content': i.content} for i in comment]
    return render(requests,"detail.html", locals())

def comment(requests):
    i = requests.POST['id']
    content = requests.POST['content']
    Comment.objects.create(article=StarDetail.objects.get(id=i), user_email=requests.user.email, content=content)
    return HttpResponseRedirect('/detail?id='+i)

def loginPage(requests):
    return render(requests, "login.html")

class DetailViewer(View):
    def get(self, requests):
        star_id = requests.GET['id']
        star = StarDetail.objects.get(id=star_id)
        detail = {
            'name': star.name,
            'introduce': star.introduce
        }
        return HttpResponse(json.dumps(detail), content_type="Application/json")

def manage(requests):
    article = StarDetail.objects.all()
    return render(requests, 'manage.html', locals())

def downAllpic(requests):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, "rb") as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name = "index/download/imgs.rar"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response
