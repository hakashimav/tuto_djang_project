from myApp.models import *

class PostClass(object):
    @staticmethod
    def listPosts():
        try:
            return Post.objects.all()
        except Exception as e:
            print(e)
            return None
            
    @staticmethod
    def getPosts(id):
        try:
            return Post.objects.get(ok=id)
        except Exception as e:
            print(e)
            return None