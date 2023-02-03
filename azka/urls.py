from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.log_in,name='log_in'),
    path('sign/',views.sign_up,name='sign_up'),
    path("contact", views.contact, name="contact"),



    path('',views.home,name="home"),

    path('about/',views.about,name="about"),
    
    path('static_student/',views.static_student,name="static_student"),


    path('event/',views.event,name='event'),
    path('eventdetail/<int:id>',views.eventdetail,name="eventdetail"),


    path('project/',views.project,name='project'),
    path('projectdetail/<int:id>',views.projectdetail,name='projectdetail'),



    path('gallery/',views.gallery,name="gallery"),



    path('testimonial/',views.testimonial,name="testimonila"),
    path('add_testimonial/',views.add_testimonial,name='add_testimonial'),
    

    path('profile/<int:myid>',views.profile,name='profile'),
    path('logout/',views.log_out,name='log_out'),

    path('student/',views.student,name='student'),
    path('student_detail/<int:id>',views.student_detail,name='student_detail'),
    path('search_results/',views.search_results,name='search_results'),

    path('edit/<int:myid>',views.edit,name='edit')

]
