from django import forms
from .models import Order, Car

class OrderForm(forms.ModelForm):
    cars = forms.ModelMultipleChoiceField(
        queryset=Car.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for car selection
        required=True  # Ensure the field is required
    )

    class Meta:
        model = Order
        fields = '__all__'


