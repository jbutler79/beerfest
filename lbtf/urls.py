from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

import views
from .views import BreweryCreate, BreweryUpdate, BeerUpdate
from .views import EventBeerCreate, EventBeerUpdate, EventBreweryCreate, EventBreweryUpdate

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lbtf/index$', views.index, name='index'),
    url(r'^lbtf/brewery/list$', views.brewery_list, name='brewery_list'),
    #url(r'^lbtf/brewery/new$', views.brewery_new, name='brewery_new'),
    url(r'^lbtf/brewery/new$', login_required(BreweryCreate.as_view()), name='brewery_new'),
    url(r'^lbtf/brewery/(?P<pk>\d+)/edit$', login_required(BreweryUpdate.as_view()), name='brewery_edit',),
    url(r'^lbtf/beer/list$', views.beer_list, name='beer_list'),
    url(r'^lbtf/beer/new$', views.beer_new, name='beer_new'),
    url(r'^lbtf/beer/(?P<pk>\d+)/edit$', login_required(BeerUpdate.as_view()), name='beer_edit',),
    url(r'^lbtf/event/brewery/list$', views.event_brewery_list, name='event_brewery_list'),
    url(r'^lbtf/event/(?P<event_id>\d+)/brewery/list$', views.event_brewery_list, name='event_brewery_list'),
    #url(r'^lbtf/event/brewery/new$', views.event_brewery_new, name='event_brewery_new'),
    url(r'^lbtf/event/brewery/new$', login_required(EventBreweryCreate.as_view()), name='event_brewery_new'),
    url(r'^lbtf/event/brewery/(?P<pk>\d+)/edit$', login_required(EventBreweryUpdate.as_view()), name='event_brewery_edit',),
    url(r'^lbtf/event/beer/list$', views.event_beer_list, name='event_beer_list'),
    url(r'^lbtf/event/(?P<event_id>\d+)/beer/list$', views.event_beer_list, name='event_beer_list'),
    url(r'^lbtf/event/beer/new$', login_required(EventBeerCreate.as_view()), name='event_beer_new'),
    url(r'^lbtf/event/beer/(?P<pk>\d+)/edit$', login_required(EventBeerUpdate.as_view()), name='event_beer_edit',),

    #Get Events and Brewerys for Add Beer to Event
    url(r'^lbtf/event/beer/get_breweries_at_event(?P<event_id>\d+)/$',
        views.get_breweries_at_event, name='get_breweries_at_event'),
    url(r'^lbtf/event/beer/get_beers_at_event_by_brewery(?P<brewery_id>\d+)/$',
        views.get_beers_at_event_by_brewery, name='get_beers_at_event_by_brewery'),

    #Get Event, Brewery, and Beer for Edit Beer at Event
    url(r'^lbtf/event/beer/get_event_name(?P<event_brewery_id>\d+)/$',
        views.get_event_name, name='get_event_name'),
    url(r'^lbtf/event/beer/get_brewery_name(?P<event_brewery_id>\d+)/$',
        views.get_brewery_name, name='get_brewery_name'),
    url(r'^lbtf/event/beer/get_beer_name(?P<event_brewery_id>\d+)/$',
        views.get_beer_name, name='get_beer_name'),

    url(r'^lbtf/event/get_event_list/$',
        views.get_event_list, name='get_event_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
