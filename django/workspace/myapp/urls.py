from django.conf.urls import patterns, include, url

#urlpatterns = patterns('', url(r'^hello/', 'myapp.views.hello', name = 'hello'),)
from django.conf.urls import url, include
from . import views

urlpatterns = patterns('myapp.views',
   #Examples
   #url(r'^$', 'myproject.view.home', name = 'home'),
   #url(r'^blog/', include('blog.urls')),
   url(r'^test/',views.test),
   url(r'^login/',views.get_name),
   url(r'^charts/',views.charts, name='charts'),
   url(r'^main/',views.SearchStudents, name='main'),
   url(r'^form/',views.get_name),
   url(r'^base/',views.base),
   url(r'^addStudent/',views.add_student, name='addStudent'),
   url(r'^moreInfo/',views.moreIn, name='moreInfo'),
)