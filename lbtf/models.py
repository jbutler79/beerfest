# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Brewery(models.Model):
    brewery_name = models.CharField(max_length=255)
    brewery_full_name = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField(default=None, blank=True, null=True)
    wordpress_logo_url = models.URLField(default=None, blank=True, null=True)
    logo = models.ImageField(upload_to="breweries", default=None, blank=True, null=True)
    added_by = models.ForeignKey(User, related_name='+')
    added_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='+')
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Brewery"
        verbose_name_plural = "Breweries"
        ordering = ['brewery_name']

    def pre_save(self, request):
        if not self.id:
            self.added_by = request.user
        self.updated_by = request.user

    def __str__(self):
        return self.brewery_name


class Beer(models.Model):
    STYLES = (
        (u'Altbier', u'Altbier'),
        (u'American Amber / Red Ale', u'American Amber / Red Ale'),
        (u'American Amber / Red Lager', u'American Amber / Red Lager'),
        (u'American Barleywine', u'American Barleywine'),
        (u'American Blonde Ale', u'American Blonde Ale'),
        (u'American Brown Ale', u'American Brown Ale'),
        (u'American IPA', u'American IPA'),
        (u'American Imperial / Double Stout', u'American Imperial / Double Stout'),
        (u'American Light Lager', u'American Light Lager'),
        (u'American Pale Ale', u'American Pale Ale'),
        (u'American Pale Wheat Ale', u'American Pale Wheat Ale'),
        (u'American Porter', u'American Porter'),
        (u'American Stout', u'American Stout'),
        (u'American Strong Ale', u'American Strong Ale'),
        (u'American Wild Ale', u'American Wild Ale'),
        (u'Applewine', u'Applewine'),
        (u'Australian Pale Ale', u'Australian Pale Ale'),
        (u'Australian Sparkling Ale', u'Australian Sparkling Ale'),
        (u'Baltic Porter', u'Baltic Porter'),
        (u'Belgian Blonde / Golden', u'Belgian Blonde / Golden'),
        (u'Belgian Brown Ale', u'Belgian Brown Ale'),
        (u'Belgian Dubbel', u'Belgian Dubbel'),
        (u'Belgian IPA', u'Belgian IPA'),
        (u'Belgian Pale Ale', u'Belgian Pale Ale'),
        (u'Belgian Quad', u'Belgian Quad'),
        (u'Belgian Strong Dark Ale', u'Belgian Strong Dark Ale'),
        (u'Belgian Strong Pale Ale', u'Belgian Strong Pale Ale'),
        (u'Belgian Tripel', u'Belgian Tripel'),
        (u'Berliner Weisse', u'Berliner Weisse'),
        (u'Bière de Champagne / Bière Brut', u'Bière de Champagne / Bière Brut'),
        (u'Bière de Garde', u'Bière de Garde'),
        (u'Black & Tan', u'Black & Tan'),
        (u'Black IPA / Cascadian Dark Ale', u'Black IPA / Cascadian Dark Ale'),
        (u'Black Lager', u'Black Lager'),
        (u'Blonde Ale', u'Blonde Ale'),
        (u'Blonde Lager', u'Blonde Lager'),
        (u'Bock', u'Bock'),
        (u'Braggot', u'Braggot'),
        (u'Burton Ale', u'Burton Ale'),
        (u'California Common', u'California Common'),
        (u'Chili Beer', u'Chili Beer'),
        (u'Cider', u'Cider'),
        (u'Cream Ale', u'Cream Ale'),
        (u'Cyser', u'Cyser'),
        (u'Czech Pilsener', u'Czech Pilsener'),
        (u'Dampfbier', u'Dampfbier'),
        (u'Dark Ale', u'Dark Ale'),
        (u'Doppelbock', u'Doppelbock'),
        (u'Dortmunder / Export Lager', u'Dortmunder / Export Lager'),
        (u'Dunkel Munich Lager', u'Dunkel Munich Lager'),
        (u'Dunkelweizen', u'Dunkelweizen'),
        (u'Eisbock', u'Eisbock'),
        (u'English Barleywine', u'English Barleywine'),
        (u'English Bitter', u'English Bitter'),
        (u'English Brown Ale', u'English Brown Ale'),
        (u'English IPA', u'English IPA'),
        (u'English Mild Ale', u'English Mild Ale'),
        (u'English Pale Ale', u'English Pale Ale'),
        (u'English Porter', u'English Porter'),
        (u'English Strong Ale', u'English Strong Ale'),
        (u'Euro Dark Lager', u'Euro Dark Lager'),
        (u'Euro Lager', u'Euro Lager'),
        (u'Extra Special / Strong Bitter', u'Extra Special / Strong Bitter'),
        (u'Faro', u'Faro'),
        (u'Flanders Oud Bruin', u'Flanders Oud Bruin'),
        (u'Flanders Red Ale', u'Flanders Red Ale'),
        (u'Foreign / Export Stout', u'Foreign / Export Stout'),
        (u'Fruit Beer', u'Fruit Beer'),
        (u'German Pilsner', u'German Pilsner'),
        (u'Ginger Beer', u'Ginger Beer'),
        (u'Gluten-Free', u'Gluten-Free'),
        (u'Golden Ale', u'Golden Ale'),
        (u'Golden Lager', u'Golden Lager'),
        (u'Gose', u'Gose'),
        (u'Gruit / Ancient Herbed Ale', u'Gruit / Ancient Herbed Ale'),
        (u'Grätzer / Grodziskie', u'Grätzer / Grodziskie'),
        (u'Gueuze', u'Gueuze'),
        (u'Happoshu', u'Happoshu'),
        (u'Harvest Ale', u'Harvest Ale'),
        (u'Hefeweizen', u'Hefeweizen'),
        (u'Hefeweizen Light / Leicht', u'Hefeweizen Light / Leicht'),
        (u'Helles Lager', u'Helles Lager'),
        (u'Herbed/Spiced Beer', u'Herbed/Spiced Beer'),
        (u'IPL (India Pale Lager)', u'IPL (India Pale Lager)'),
        (u'Imperial / Double Black IPA', u'Imperial / Double Black IPA'),
        (u'Imperial / Double Brown Ale', u'Imperial / Double Brown Ale'),
        (u'Imperial / Double IPA', u'Imperial / Double IPA'),
        (u'Imperial / Double Pilsner', u'Imperial / Double Pilsner'),
        (u'Imperial / Double Porter', u'Imperial / Double Porter'),
        (u'Imperial / Double Red Ale', u'Imperial / Double Red Ale'),
        (u'Imperial / Double Stout', u'Imperial / Double Stout'),
        (u'Imperial Oatmeal Stout', u'Imperial Oatmeal Stout'),
        (u'Irish Dry Stout', u'Irish Dry Stout'),
        (u'Irish Red Ale', u'Irish Red Ale'),
        (u'Japanese Rice Lager', u'Japanese Rice Lager'),
        (u'Kellerbier / Zwickelbier', u'Kellerbier / Zwickelbier'),
        (u'Kombucha', u'Kombucha'),
        (u'Kristallweizen', u'Kristallweizen'),
        (u'Kvass', u'Kvass'),
        (u'Kölsch', u'Kölsch'),
        (u'Lambic', u'Lambic'),
        (u'Maibock/Helles Bock', u'Maibock/Helles Bock'),
        (u'Malt Beer', u'Malt Beer'),
        (u'Malt Liquor', u'Malt Liquor'),
        (u'Mead', u'Mead'),
        (u'Melomel', u'Melomel'),
        (u'Milk / Sweet Stout', u'Milk / Sweet Stout'),
        (u'New Zealand Pale Ale', u'New Zealand Pale Ale'),
        (u'Non-Alcoholic', u'Non-Alcoholic'),
        (u'North American Adjunct Lager', u'North American Adjunct Lager'),
        (u'Oatmeal Stout', u'Oatmeal Stout'),
        (u'Oktoberfest/Festbier/Märzen', u'Oktoberfest/Festbier/Märzen'),
        (u'Old Ale', u'Old Ale'),
        (u'Oyster Stout', u'Oyster Stout'),
        (u'Pale Lager', u'Pale Lager'),
        (u'Patersbier', u'Patersbier'),
        (u'Perry', u'Perry'),
        (u'Pilsner', u'Pilsner'),
        (u'Porter', u'Porter'),
        (u'Pumpkin / Yam Beer', u'Pumpkin / Yam Beer'),
        (u'Pyment', u'Pyment'),
        (u'Radler', u'Radler'),
        (u'Rauchbier', u'Rauchbier'),
        (u'Roggenbier', u'Roggenbier'),
        (u'Root Beer', u'Root Beer'),
        (u'Russian Imperial Stout', u'Russian Imperial Stout'),
        (u'Rye Beer', u'Rye Beer'),
        (u'Sahti', u'Sahti'),
        (u'Saison / Farmhouse Ale', u'Saison / Farmhouse Ale'),
        (u'Schwarzbier', u'Schwarzbier'),
        (u'Scotch Ale / Wee Heavy', u'Scotch Ale / Wee Heavy'),
        (u'Scottish Ale', u'Scottish Ale'),
        (u'Scottish Export Ale', u'Scottish Export Ale'),
        (u'Session IPA', u'Session IPA'),
        (u'Smoked Beer', u'Smoked Beer'),
        (u'Sour Ale', u'Sour Ale'),
        (u'Specialty Grain', u'Specialty Grain'),
        (u'Stout', u'Stout'),
        (u'Triple IPA', u'Triple IPA'),
        (u'Vienna Lager', u'Vienna Lager'),
        (u'Weizenbock', u'Weizenbock'),
        (u'Wheat Wine', u'Wheat Wine'),
        (u'White IPA', u'White IPA'),
        (u'Winter Ale', u'Winter Ale'),
        (u'Winter Lager', u'Winter Lager'),
        (u'Winter Warmer', u'Winter Warmer'),
        (u'Witbier', u'Witbier'),
    )

    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    beer_name = models.CharField(max_length=255)
    style = models.CharField(max_length=255, choices=STYLES)
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=500, default=None, blank=True, null=True)
    website = models.URLField(max_length=255, default=None, blank=True, null=True)
    untappd_url = models.URLField(max_length=255, default=None, blank=True, null=True)
    beer_advocate_url = models.URLField(max_length=255, default=None, blank=True, null=True)
    rate_beer_url = models.URLField(max_length=255, default=None, blank=True, null=True)
    added_by = models.ForeignKey(User, related_name='+')
    added_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='+')
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Beer"
        verbose_name_plural = "Beers"
        ordering = ['beer_name']
        unique_together = ('brewery', 'beer_name')

    def pre_save(self, request):
        if not self.id:
            self.added_by = request.user
        self.updated_by = request.user

    def __str__(self):
        return self.beer_name


class Event(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    added_by = models.ForeignKey(User, related_name='+')
    added_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='+')
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        unique_together = ('event_name', 'date')

    def get_event_list(self):
        event_list = Event.objects.all()
        return event_list

    def pre_save(self, request):
        if not self.id:
            self.added_by = request.user
        self.updated_by = request.user

    def __str__(self):
        return u"%s %s" % (self.date.strftime('%Y'), self.event_name)


class Event_Brewery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    area = models.CharField(max_length=50, default=None, blank=True, null=True)
    booth = models.CharField(max_length=50, default=None, blank=True, null=True)
    added_by = models.ForeignKey(User, related_name='+')
    added_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='+')
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event_Brewery"
        verbose_name_plural = "Event_Breweries"
        unique_together = ('event', 'brewery')

    def pre_save(self, request):
        if not self.id:
            self.added_by = request.user
        self.updated_by = request.user

    def get_brewery_list_by_event(self, event):
        brewery_list = Event_Brewery.objects.select_related().filter(event_id=event)
        return brewery_list

    def __str__(self):
        e = Event.objects.get(id=self.event_id)
        b = Brewery.objects.get(id=self.brewery_id)
        #return e.date.strftime('%Y ') + e.event_name + ', ' + b.brewery_name
        return u"%s" % (b.brewery_name)


class Event_Beer(models.Model):
    event_brewery = models.ForeignKey(Event_Brewery, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    brewmaster = models.BooleanField(default=False)
    bottle_row = models.BooleanField(default=False)
    vip = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, related_name='+')
    added_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='+')
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event_Beer"
        verbose_name_plural = "Event_Beers"
        unique_together = ('event_brewery', 'beer')

    def pre_save(self, request):
        if not self.id:
            self.added_by = self.request.user
        self.updated_by = self.request.user

    def __str__(self):
        eb = Event_Brewery.objects.get(id=self.event_brewery_id)
        e = Event.objects.get(id=eb.event_id)
        b = Brewery.objects.get(id=eb.brewery_id)
        br = Beer.objects.get(id=self.beer_id)

        return e.date.strftime('%Y ') + e.event_name + ', ' + b.brewery_name + ', ' + br.beer_name
