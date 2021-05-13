
from django import forms
from .models import Deposit
from .script import  Deposit_calc


class DepositForm(forms.ModelForm):
    deposit = forms.DecimalField(label='deposit', widget=forms.NumberInput(attrs={"placeholder": "Your deposit"}))
    term = forms.DecimalField(label='term', widget=forms.NumberInput(attrs={"placeholder": "Your term"}))
    rate = forms.DecimalField(label='rate', widget=forms.NumberInput(attrs={"placeholder": "Your rate"}))

    class Meta:
        model = Deposit
        fields = [
            'deposit',
            'term',
            'rate',
            
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        # your calculate
        deposit = Deposit_calc(deposit = instance.deposit, term=instance.term, rate=instance.rate )
        a = deposit.interest()
        instance.interest = a
        
        if commit:
            instance.save()
        return instance