from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Brewery, Beer, Event, Event_Brewery, Event_Beer


class BreweryForm(forms.ModelForm):
    class Meta:
        model = Brewery
        fields = ('brewery_name', 'brewery_full_name', 'city', 'state_province', 'country',
                  'website', 'wordpress_logo_url', 'logo',)

    def __init__(self, *args, **kwargs):
        super(BreweryForm, self).__init__(*args, **kwargs)
        self.fields['brewery_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['brewery_full_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['state_province'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['website'].widget.attrs.update({'class': 'form-control'})
        self.fields['wordpress_logo_url'].widget.attrs.update({'class': 'form-control'})


class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ('brewery', 'beer_name', 'style', 'abv', 'description', 'website',
                  'untappd_url', 'beer_advocate_url', 'rate_beer_url',)

    def __init__(self, *args, **kwargs):
        super(BeerForm, self).__init__(*args, **kwargs)
        self.fields['brewery'].widget.attrs.update({'class': 'form-control'})
        self.fields['beer_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['style'].widget.attrs.update({'class': 'form-control'})
        self.fields['abv'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['website'].widget.attrs.update({'class': 'form-control'})
        self.fields['untappd_url'].widget.attrs.update({'class': 'form-control'})
        self.fields['beer_advocate_url'].widget.attrs.update({'class': 'form-control'})
        self.fields['rate_beer_url'].widget.attrs.update({'class': 'form-control'})


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'date',)


class EventBreweryForm(forms.ModelForm):
    class Meta:
        model = Event_Brewery
        fields = ('event', 'brewery', 'area', 'booth',)

    def __init__(self, *args, **kwargs):
        super(EventBreweryForm, self).__init__(*args, **kwargs)
        self.fields['event'].widget.attrs.update({'class': 'form-control'})
        self.fields['brewery'].widget.attrs.update({'class': 'form-control'})
        self.fields['area'].widget.attrs.update({'class': 'form-control'})
        self.fields['booth'].widget.attrs.update({'class': 'form-control'})


class EventBeerForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.all())
    brewery = forms.ModelChoiceField(queryset=Brewery.objects.all())
    beer = forms.ModelChoiceField(queryset=Beer.objects.all())

    class Meta:
        model = Event_Beer
        fields = ('event', 'brewery', 'beer', 'vip', 'bottle_row', 'brewmaster',)

    def __init__(self, *args, **kwargs):
        super(EventBeerForm, self).__init__(*args, **kwargs)
        self.fields['event'].widget.attrs.update({'class': 'form-control'})
        self.fields['brewery'].widget.attrs.update({'class': 'form-control'})
        self.fields['beer'].widget.attrs.update({'class': 'form-control'})
        #self.fields['vip'].widget.attrs.update({'class': 'form-control'})
        #self.fields['bottle_row'].widget.attrs.update({'class': 'form-control'})
