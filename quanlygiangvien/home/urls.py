from django.contrib import admin
from django.urls import path, include
from .views import HomeClass, LoginClass,InstructorDetailView, ArticlePost, ArticleDetailView, ForumView, myForum
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from . import views

urlpatterns = [
   
    path('login/', LoginClass.as_view(), name='login'),
    path('home/', HomeClass.as_view(), name='home'),    
    path('instructor/<str:instructor_id>/', InstructorDetailView.as_view(), name='instructor'),
    path('articlepost/', ArticlePost.as_view(), name='articlepost'),
    path('article/<str:instructor_id>/', ArticleDetailView.as_view(), name='article'),
    path('forumad/', ForumView.as_view(), name='forumad'),
    path('myforum/', myForum.as_view(), name='myforum'),
    # path('forumins/<str:instructor_id>/', ForumDetailViewIns.as_view(), name='forumins'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        