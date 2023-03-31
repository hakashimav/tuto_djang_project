from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from myApp.modelClasses.model_Post import PostClass

# Create your views here.
def login(request):
    try:

        response =  TemplateResponse(request, 'page/login.html', {})
        return response
    except Exception:
        return HttpResponse("ERROR")

def index(request):
    try:
        model=PostClass.listPosts()
        dic={
            'model':model
        }
        response =  TemplateResponse(request, 'index.html', dic)
        return response
    except Exception:
        return HttpResponse("ERROR")



# def selectedPost(request,id):
#     try:
#         id=int(id)
#         model=PostClass.getPosts(id)
#         dic={
#             'post':model
#         }
#         response =  TemplateResponse(request, 'selected_item.html', dic)
#         return response
#     except Exception:
#         return HttpResponse("ERROR")