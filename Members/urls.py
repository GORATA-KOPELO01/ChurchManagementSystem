from django.urls import path
from django import views
from .import views

urlpatterns = [
    #path('members/', MemberListView.as_view(), name='member_list'),
    #path('members/add/', MemberCreateView.as_view(), name='member_create'),
    #path('members/<int:pk>/update/', MemberUpdateView.as_view(), name='member_update'),
    #path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='member_delete'),
    path('upcoming-birthdays/', views.upcoming_birthdays, name='upcoming_birthdays'),
    path('add_member/', views.createuser,name='add_member'),
    path('update_user/<int:user_id>/',views.update_user, name='update_user'),
    path('member_list/',views.member_list,name='member_list'),
    path('delete_member/<str:pk>/',views.deleteUser,name='delete_member'),
]