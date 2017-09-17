from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='in'),
    url(r'^history/$', views.history, name='hi' ),
    url(r'^animals/mouse/$', views.animals, name='an' ),
    url(r'^solutions/$', views.solutions, name='so' ),

    url(r'^animals/rabbit/$', views.rabbit, name='ra' ),
    url(r'^animals/dog/$', views.dog, name='do' ),
    url(r'^animals/monkey/$', views.monkey, name='mo' )
]

    #patterns('', url(r'^history/', 'animals.views.history', name='history'),)
