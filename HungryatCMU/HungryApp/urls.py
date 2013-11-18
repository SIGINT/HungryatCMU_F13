from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'HungryApp.views.home', name='home'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'HungryApp/login.html'}),
    url(r'^registration$', 'HungryApp.views.StudentRegistration'),
    url(r'^register$', 'HungryApp.views.StudentRegistration'),
    url(r'^signup$', 'HungryApp.views.StudentRegistration'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^forgotpassword$','HungryApp.views.forgotpassword'),
    url(r'^resetpassword$','HungryApp.views.resetpassword'),
    url(r'^confirm-registration/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', 'HungryApp.views.confirm_registration', name='confirm'),
    url(r'^invite-employee$','HungryApp.views.invite_employee', name='invite-employee'),
    url(r'^add-location$','HungryApp.views.add_location', name='add-location'),
    url(r'^register-employee/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', 'HungryApp.views.register_employee', name='register-employee'),
    url(r'^restaurants$','HungryApp.views.restaurants', name='restaurants'),
    url(r'^employees$','HungryApp.views.employees', name='employees'),
    url(r'^students$','HungryApp.views.students', name='students'),
    url(r'^activate-user/(?P<id>\d+)$','HungryApp.views.activate_user', name='activate-user'),
    url(r'^deactivate-user/(?P<id>\d+)$','HungryApp.views.deactivate_user', name='deactivate-user'),
    url(r'^account$','HungryApp.views.view_account'),
    url(r'^restaurant/(?P<id>\d+)$', 'HungryApp.views.view_restaurant'),
    url(r'^add-restaurant$','HungryApp.views.add_restaurant'),
    url(r'^edit-restaurant/(?P<id>\d+)$', 'HungryApp.views.edit_restaurant'),
    url(r'^restaurant-picture/(?P<id>\d+)$', 'HungryApp.views.get_restaurant_picture', name='restaurant-picture'),
    url(r'^add_fooditem/(?P<id>\d+)$', 'HungryApp.views.add_fooditem', name='add_fooditem'),
    url(r'^edit_fooditem/(?P<id>\d+)$', 'HungryApp.views.edit_fooditem', name='edit_fooditem'),
    url(r'^food-item_photo/(?P<id>\d+)$', 'HungryApp.views.get_fooditem_photo', name='fooditem_photo'),
    url(r'^display_fooditems/(?P<id>\d+)$', 'HungryApp.views.display_fooditems', name='display_fooditems'),
    url(r'^search$', 'HungryApp.views.search'),
)
