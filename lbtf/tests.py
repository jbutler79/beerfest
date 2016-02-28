from django.test import TestCase
from django.contrib.auth.models import User
from .models import Brewery, Beer, Event, Event_Brewery, Event_Beer


class BreweryTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create_user('test_user', 'testuser@test.com', 'password')
        test_brewery1 = Brewery.objects.create(brewery_name="Stone Brewing Company",
                                               city="Escondido", state_province="CA",
                                               country="United States",
                                               added_by=test_user, updated_by=test_user)
        Brewery.objects.create(brewery_name="Russian River Brewing Company",
                               city="Santa Rosa", state_province="CA",
                               country="United States",
                               added_by=test_user, updated_by=test_user)
        Brewery.objects.create(brewery_name="Free Will Brewing Company",
                               city="Perkasie", state_province="PA",
                               country="United States",
                               added_by=test_user, updated_by=test_user)
        test_brewery2 = Brewery.objects.create(brewery_name="Victory Brewing",
                                               city="Downingtown", state_province="PA",
                                               country="United States",
                                               added_by=test_user, updated_by=test_user)
        test_event1 = Event.objects.create(event_name="Lansdale Beer Testing Festival",
                                           date="2016-06-25",
                                           added_by=test_user, updated_by=test_user)
        test_event2 = Event.objects.create(event_name="Lansdale Beer Testing Festival",
                                           date="2015-06-27",
                                           added_by=test_user, updated_by=test_user)
        Event_Brewery.objects.create(event=test_event1, brewery=test_brewery1,
                                     added_by=test_user, updated_by=test_user)
        Event_Brewery.objects.create(event=test_event1, brewery=test_brewery2,
                                     added_by=test_user, updated_by=test_user)
        Event_Brewery.objects.create(event=test_event2, brewery=test_brewery2,
                                     added_by=test_user, updated_by=test_user)

    def test_get_event_list_and_breweries_by_event(self):
        event_list = Event().get_event_list()

        for event in event_list:
            print(event.date.strftime('%Y ') + event.event_name)
            breweries_by_event = Event_Brewery().get_brewery_list_by_event(event)
            for b in breweries_by_event:
                print("-- " + b.brewery.brewery_name)
            breweries_by_event = ""
