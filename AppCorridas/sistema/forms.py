from django import forms
class Corrida(forms.Form):
    #uber 4 paradas e destino
    #99pop e indriver 2 paradas e destino
    origem = forms.CharField(
        label="Origem",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Insira o local de embarque"
            }
        )
    )
    # parada1 = forms.CharField(
    #     label="Parada 1",
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Insira o local da parada"
    #         }
    #     )
    # )
    # parada2 = forms.CharField(
    #     label="Parada 1",
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Insira o local da parada"
    #         }
    #     )
    # )
    # parada3 = forms.CharField(
    #     label="Parada 1",
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Insira o local da parada"
    #         }
    #     )
    # )
    # parada4 = forms.CharField(
    #     label="Parada 1",
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Insira o local da parada"
    #         }
    #     )
    # )
    destino = forms.CharField(
        label="Destino",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Insira o destino final"
            }
        )
    )