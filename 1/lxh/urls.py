from django.conf.urls import patterns, include, url
from lxh import views
#c4
# Uncomment the next two lines to enable the admin:
#author :lxh

from django.contrib import admin
admin.autodiscover()
#b3
urlpatterns = patterns('',
    ('^$',views.main_sight),
    ('^show/$',views.show),
    ('^look/$',views.look),
    ('^deleteconfirm/$',views.deleteconfirm),
    ('^delete/$',views.delete),
    ('^add/$',views.add),
    ('^addbook/$',views.addbook),
    ('^author/$',views.author),
    ('^author1/$',views.author1),
    ('^addauthor/$',views.addauthor),
    ('^edit/$',views.edit),
    ('^editbooks/$',views.editbooks),
    ('^editauthors/$',views.editauthors),
    ('^search/$',views.search),
    ('^searchbooks/$',views.searchbooks),
    # Examples:
    # url(r'^$', 'lxh.views.home', name='home'),
    # url(r'^lxh/', include('lxh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
