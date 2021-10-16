from django.urls import path 
from .views import EmployeesAPIView ,EmployeesDetails
urlpatterns = [
    #path('article/', article_liste),
    path('employes/', EmployeesAPIView.as_view()),
    #path('generic/article/', GenericAPIView.as_view()),
    #path('detail/<str:pk>' , article_detail )
    path('employes/<str:pk>' , EmployeesDetails.as_view() )
]
