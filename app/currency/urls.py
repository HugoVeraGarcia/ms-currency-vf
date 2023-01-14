from django.urls import path
from currency.views import  CurrenciesView, Check_exchange_rateView, Change_currencyView, TrackFeeView, SetupView
from . import views

urlpatterns = [
    # GET: ruta para obtener todas las monedas
    path('v1/currencies/', views.CurrenciesView.as_view()),
    # GET: ruta para obtener datos de una moneda
    path('v1/currencies/<str:name>/', views.CurrenciesView.as_view()),
    # GET: ruta para obtener la equivalencia entre monedas
    path('v1/currencies/check/<str:base>/<str:quote>/', views.Check_exchange_rateView.as_view()),
    # POST: ruta para realizar una operación de intercambio
    path('v1/exchange/', views.Change_currencyView.as_view()),
    # GET: ruta para obtener el seguimiento de todas las operaciones
    path('v1/track_fee/', views.TrackFeeView.as_view()),
    # POST: ruta para iniciar la bd con las monedas, valores, fees, etc.
    path('v1/setup/', views.SetupView.as_view()),
]