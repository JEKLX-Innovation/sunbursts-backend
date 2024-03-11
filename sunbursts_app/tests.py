from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CookieStand


class CookieStandModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a test user for ForeignKey
        test_user = get_user_model().objects.create_user(username='testuser', password='12345')
        test_user.save()

        # Create a CookieStand object for testing
        CookieStand.objects.create(
            location='Test Location',
            owner=test_user,
            description='Test Description',
            hourly_sales=[10, 20, 30],
            minimum_customers_per_hour=5,
            maximum_customers_per_hour=50,
            average_cookie_per_sale=2.5
        )

    def test_location_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_owner_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'owner')

    def test_description_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_hourly_sales_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('hourly_sales').verbose_name
        self.assertEquals(field_label, 'hourly sales')

    def test_minimum_customers_per_hour_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('minimum_customers_per_hour').verbose_name
        self.assertEquals(field_label, 'minimum customers per hour')

    def test_maximum_customers_per_hour_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('maximum_customers_per_hour').verbose_name
        self.assertEquals(field_label, 'maximum customers per hour')

    def test_average_cookie_per_sale_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('average_cookie_per_sale').verbose_name
        self.assertEquals(field_label, 'average cookie per sale')

    def test_get_absolute_url(self):
        cookie_stand = CookieStand.objects.get(id=1)
        expected_url = reverse('cookiestand_detail', args=[str(cookie_stand.id)])
        self.assertEquals(cookie_stand.get_absolute_url(), expected_url)
