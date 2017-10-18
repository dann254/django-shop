from django import forms


class PurchaseForm(forms.Form):
    name     = forms.CharField()
    price    = forms.IntegerField()
    quantity = forms.IntegerField()

    def clean_price(self):
        price = self.cleaned_data.get("price")
        try:
            int(price)
        except:
            raise forms.ValidationError("please enter quantity as an integer")

        return price
