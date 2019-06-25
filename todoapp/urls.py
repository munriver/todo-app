from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from todoapp import views


urlpatterns = [
    url(r'^todolist/$', views.TaskList.as_view()),
    url(r'^todolist/(?P<pk>\d+)/$', views.TaskDetail.as_view()),
    url(r'^csrf/$', views.csrf),
    url(r'^currentuser/$', views.current_user),
]


urlpatterns = format_suffix_patterns(urlpatterns)
