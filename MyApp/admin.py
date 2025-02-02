from django.contrib import admin
from .models import Car, Order, Contact, Driver, Task
import logging
from django import forms
logger = logging.getLogger(__name__)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'price', 'car_desc', 'image_tag')  # Include 'image_tag' in list_display
    search_fields = ('car_name',)
    list_filter = ('price',)

    # Optional: Show image thumbnail in the admin
    def image_tag(self, obj):
        return f'<img src="{obj.image.url}" width="50" />' if obj.image else ''

    image_tag.allow_tags = True


class OrderAdminForm(forms.ModelForm):  # Corrected this line
    cars = forms.ModelMultipleChoiceField(
        queryset=Car.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for car selection
        required=True  # Ensure the field is required
    )

    class Meta:
        model = Order
        fields = '__all__'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm  # Use the custom form
    list_display = ('name', 'email', 'phone', 'days_for_rent', 'date', 'loc_from', 'loc_to', 'driver_name', 'cars_list')
    search_fields = ('name', 'email')
    list_filter = ('date', 'loc_from', 'loc_to')

    # Custom method to display the driver's name
    def driver_name(self, obj):
        return obj.driver.name if obj.driver else 'No Driver Assigned'

    driver_name.short_description = 'Driver'

    # Custom method to display the list of cars
    def cars_list(self, obj):
        return ", ".join([car.car_name for car in obj.cars.all()])

    cars_list.short_description = 'Cars'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'email', 'phone', 'status', 'availability', 'vehicle_assigned')
    search_fields = ('name', 'license_number', 'email')
    list_filter = ('status', 'availability')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'driver', 'status', 'created_at')
    search_fields = ('name', 'driver__name')
    list_filter = ('status', 'created_at')
