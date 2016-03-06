from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Brewery, Beer, Event, Event_Brewery, Event_Beer
from .forms import BreweryForm, BeerForm, EventForm, EventBreweryForm, EventBeerForm
import forms
import simplejson


def index(request):
    return render(request, 'lbtf/index.html', )


def brewery_list(request):
    breweries = Brewery.objects.filter()
    return render(request, 'lbtf/brewery_list.html', {'breweries': breweries})

@login_required
def brewery_new(request):
    if request.method == "POST":
        form = BreweryForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pre_save(request)
            post.save()
            return redirect('brewery_list')
    else:
        form = BreweryForm()
    return render(request, 'lbtf/brewery_edit.html', {'form': form})


def beer_list(request):
    beers = Beer.objects.filter()
    return render(request, 'lbtf/beer_list.html', {'beers': beers})


@login_required
def beer_new(request):
    if request.method == "POST":
        form = BeerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pre_save(request)
            post.save()
            return redirect('beer_list')
    else:
        form = BeerForm()
    return render(request, 'lbtf/beer_edit.html', {'form': form})


@login_required
def event_new(request):
    form = EventForm()
    return render(request, 'lbtf/event_edit.html', {'form': form})


@login_required
def event_brewery_new(request):
    form = EventBreweryForm()
    if request.method == "POST":
        form = EventBreweryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pre_save(request)
            post.save()
            return redirect('event_brewery_edit')
    return render(request, 'lbtf/event_brewery_edit.html', {'form': form})


@login_required
def event_beer_new(request):
    print("event_beer_new")
    if request.method == "POST":
        form = EventBeerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pre_save(request)
            post.save()
            return redirect('event_beer_edit')
    return render(request, 'lbtf/event_brewery_edit.html', {'form': form})


def event_brewery_list(request):
    event_breweries = Event_Brewery.objects.select_related()
    return render(request, 'lbtf/event_brewery_list.html',
                  {'event_breweries': event_breweries})


def event_brewery_list(request, event_id):
    event = Event.objects.get(pk=event_id)
    event_breweries = Event_Brewery.objects.select_related().filter(event=event)
    return render(request, 'lbtf/event_brewery_list.html',
                  {'event_breweries': event_breweries})


#def event_beer_list(request):
#    event_beers = Event_Beer.objects.select_related()
#    return render(request, 'lbtf/event_beer_list.html',
#                  {'event_beers': event_beers})


def event_beer_list(request, event_id):
    event = Event.objects.get(pk=event_id)
    event_beers = Event_Beer.objects.select_related().filter(event_brewery__event=event)
    return render(request, 'lbtf/event_beer_list.html',
                  {'event_beers': event_beers})


def event_select(request):
    form = EventForm()
    return render(request, 'lbtf/event_select.html', {'form': form})


def get_event_list(request):
    events = Event.objects.all()
    event_dict = {}
    for event in events:
        event_dict[str(event.id)] = event.date.strftime('%Y') + " " + event.event_name

    print(simplejson.dumps(event_dict))
    return HttpResponse(simplejson.dumps(event_dict), content_type='application/json')


def get_breweries_at_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event_breweries = Event_Brewery.objects.select_related().filter(event=event)
    brewery_dict = {}
    for event_brewery in event_breweries:
        brewery_dict[str(event_brewery.brewery.id)] = event_brewery.brewery.brewery_name

    print(simplejson.dumps(brewery_dict))
    return HttpResponse(simplejson.dumps(brewery_dict), content_type='application/json')


def get_beers_at_event_by_brewery(request, brewery_id):
    brewery = Brewery.objects.get(pk=brewery_id)
    beers = Beer.objects.filter(brewery=brewery)
    beer_dict = {}
    for beer in beers:
        beer_dict[beer.id] = beer.beer_name
    return HttpResponse(simplejson.dumps(beer_dict), content_type="application/json")


def get_event_name(request, event_brewery_id):
    event_beer = Event_Beer.objects.select_related().get(pk=event_brewery_id)
    event_dict = {}
    event_dict[str(event_beer.event_brewery.event.id)] = str(event_beer.event_brewery.event)
    return HttpResponse(simplejson.dumps(event_dict), content_type='application/json')


def get_brewery_name(request, event_brewery_id):
    event_beer = Event_Beer.objects.select_related().get(pk=event_brewery_id)
    brewery_dict = {}
    brewery_dict[str(event_beer.beer.brewery.id)] = str(event_beer.beer.brewery)
    return HttpResponse(simplejson.dumps(brewery_dict), content_type='application/json')


def get_beer_name(request, event_brewery_id):
    event_beer = Event_Beer.objects.select_related().get(pk=event_brewery_id)
    beer_dict = {}
    beer_dict[str(event_beer.beer.id)] = str(event_beer.beer)
    return HttpResponse(simplejson.dumps(beer_dict), content_type='application/json')


class EventBreweryCreate(CreateView):
    model = Event_Brewery
    template_name = 'lbtf/event_brewery_edit.html'
    form_class = forms.EventBreweryForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not obj.id:
            obj.added_by = self.request.user

        obj.updated_by = self.request.user
        #obj.event_brewery = Event_Brewery.objects.get(event=form.cleaned_data['event'],
        #                                              brewery=form.cleaned_data['brewery'])
        obj.save()
        return redirect('event_brewery_list')
        #return reverse(self.get_success_url())

    # def form_invalid(self, form):
    #     print "form is invalid"
    #     return HttpResponse("form is invalid.. this is just an HttpResponse object")

    def get_success_url(self):
        return redirect('event_brewery_list')
        #return reverse('event_beer_list')


class EventBeerCreate(CreateView):
    model = Event_Beer
    template_name = 'lbtf/event_beer_edit.html'
    form_class = forms.EventBeerForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not obj.id:
            obj.added_by = self.request.user

        obj.updated_by = self.request.user
        obj.event_brewery = Event_Brewery.objects.get(event=form.cleaned_data['event'],
                                                      brewery=form.cleaned_data['brewery'])
        obj.save()
        return redirect('event_beer_list')
        #return reverse(self.get_success_url())

    # def form_invalid(self, form):
    #     print "form is invalid"
    #     return HttpResponse("form is invalid.. this is just an HttpResponse object")

    def get_success_url(self):
        return redirect('event_beer_list')
        #return reverse('event_beer_list')


class EventBreweryUpdate(UpdateView):
    model = Event_Brewery
    template_name = 'lbtf/event_brewery_edit.html'
    form_class = forms.EventBreweryForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not obj.id:
            obj.added_by = self.request.user
        obj.updated_by = self.request.user
        #obj.event_brewery = Event_Brewery.objects.get(event=form.cleaned_data['event'],
        #                                              brewery=form.cleaned_data['brewery'])
        obj.save()
        return redirect('event_brewery_list')

    def form_invalid(self, form):
        return HttpResponse(form.errors.as_ul())

    def get_success_url(self):
        return reverse('event_brewery_list')

    def get_context_data(self, **kwargs):
        context = super(EventBreweryUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('event_brewery_edit',
                                    kwargs={'pk': self.get_object().id})
        return context


class EventBeerUpdate(UpdateView):
    model = Event_Beer
    template_name = 'lbtf/event_beer_edit.html'
    form_class = forms.EventBeerForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not obj.id:
            obj.added_by = self.request.user
        obj.updated_by = self.request.user
        obj.event_brewery = Event_Brewery.objects.get(event=form.cleaned_data['event'],
                                                      brewery=form.cleaned_data['brewery'])
        obj.save()
        return redirect('event_beer_list')

    def form_invalid(self, form):
        return HttpResponse(form.errors.as_ul())

    def get_success_url(self):
        return reverse('event_beer_list')

    def get_context_data(self, **kwargs):
        context = super(EventBeerUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('event_beer_edit',
                                    kwargs={'pk': self.get_object().id})
        return context


class BreweryCreate(CreateView):
    model = Brewery
    template_name = 'lbtf/brewery_edit.html'
    form_class = forms.BreweryForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not obj.id:
            obj.added_by = self.request.user

        obj.updated_by = self.request.user
        obj.save()
        return redirect('brewery_list')
        #return reverse(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponse(form.errors.as_ul())

    def get_success_url(self):
        return redirect('brewery_list')
        #return reverse('event_beer_list')


class BreweryUpdate(UpdateView):
    model = Brewery
    template_name = 'lbtf/brewery_edit.html'
    form_class = forms.BreweryForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not obj.id:
            obj.added_by = self.request.user
        obj.updated_by = self.request.user
        obj.save()
        return redirect('brewery_list')

    def form_invalid(self, form):
        return HttpResponse(form.errors.as_ul())

    def get_success_url(self):
        return reverse('brewery_list')

    def get_context_data(self, **kwargs):
        context = super(BreweryUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('brewery_edit',
                                    kwargs={'pk': self.get_object().id})
        return context


class BeerUpdate(UpdateView):
    model = Beer
    template_name = 'lbtf/beer_edit.html'
    form_class = forms.BeerForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not obj.id:
            obj.added_by = self.request.user
        obj.updated_by = self.request.user
        obj.save()
        return redirect('beer_list')

    def form_invalid(self, form):
        return HttpResponse(form.errors.as_ul())

    def get_success_url(self):
        return reverse('beer_list')

    def get_context_data(self, **kwargs):
        context = super(BeerUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('beer_edit',
                                    kwargs={'pk': self.get_object().id})
        return context
