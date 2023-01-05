from django.urls import path
from . import views
urlpatterns = [
path('patients/', views.index, name='patients'),
path('patients/del_pat/<int:id>', views.del_pat,name='del_pat'),
path('services/', views.list_ser, name='services'),
path('services/del_ser/<int:id>', views.del_ser,name='del_ser'),
path('patients/update_pat/<int:id>', views.update_pat,name='update_pat'),
path('patients/update_pat/update_pat_action/<int:id>',views.update_pat_action, name='update_pat_action'),
path('patients/addPatient/', views.add, name='add'),
path('patients/patient/addp/add_pat/', views.add_pat, name='add_pat'),
path('users/', views.list_users, name='user'),
path('user/createUser/', views.create_compte, name='create_compte'),
path('user/createUser/add_user_action/', views.create_user_action,name='create_user_action'),
path('user/del_user/<int:id>', views.del_user, name='del_user'),
path('', views.connexion, name='connexion'),
path('connexion/', views.signIn, name='signIn'),
path('connexion/connexion/', views.signIn, name='signIn'),
path('deconnexion/', views.signOut, name='deconnexion'),
path('deconnexion/', views.signOut, name='deconnexion'),
path('user/update_user/<int:id>', views.update_user, name='update_user'),
path('user/update_user/update_user_action/<int:id>',views.update_user_action, name='update_user_action'),
path('patients/patient/addp/', views.addp, name='addp'),
]
