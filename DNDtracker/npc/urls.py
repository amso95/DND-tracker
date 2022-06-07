from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='npc-home'),
    path('base/', views.test, name='npc-home'),
    path('create/race/', views.createRace, name='npc-createRace'),
    path('create/name/', views.createName, name='npc-createName'),
    path('create/femalename/', views.createFemaleName, name='npc-createFemaleName'),
    path('create/malename/', views.createMaleName, name='npc-createMaleName'),
    path('create/familyname/', views.createFamilyName, name='npc-createFamilyName'),
    path('list/npc/', views.listNPC, name='npc-listNPC'),
    path('list/race/', views.listRace, name='npc-listRace'),
    path('list/name/', views.listName, name='npc-listName'),
    path('list/femalename/', views.listFemaleName, name='npc-listFemaleName'),
    path('list/malename/', views.listMaleName, name='npc-listMaleName'),
    path('list/familyname/', views.listFamilyName, name='npc-listFamilyName'),
    url(r'^list/npc/(?P<pk>\d+)/$', views.editNPC, name='npc-editNPC'),
    url(r'^list/race/(?P<pk>\d+)/$', views.editRace, name='npc-editRace'),
    url(r'^list/name/(?P<pk>\d+)/$', views.editName, name='npc-editName'),
    url(r'^list/femalename/(?P<pk>\d+)/$', views.editFemaleName, name='npc-editFemaleName'),
    url(r'^list/malename/(?P<pk>\d+)/$', views.editMaleName, name='npc-editMaleName'),
    url(r'^list/familyname/(?P<pk>\d+)/$', views.editFamilyName, name='npc-editFamilyName'),

    url(r'^list/familyname/(?P<pk>\d+)/delete/$', views.deleteFamilyName, name='npc-deleteFamilyName'),
    url(r'^list/femalename/(?P<pk>\d+)/delete/$', views.deleteFemaleName, name='npc-deleteFemaleName'),
    url(r'^list/malename/(?P<pk>\d+)/delete/$', views.deleteMaleName, name='npc-deleteMaleName'),
    url(r'^list/name/(?P<pk>\d+)/delete/$', views.deleteName, name='npc-deleteName'),
    url(r'^list/npc/(?P<pk>\d+)/delete/$', views.deleteNPC, name='npc-deleteNPC'),
    url(r'^list/race/(?P<pk>\d+)/delete/$', views.deleteRace, name='npc-deleteRace')
]