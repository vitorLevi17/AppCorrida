from django import forms

#Formulario para receber do usuario os endereços de origem e destino
#Para o formulario ser validado, ambos os campos devem ser preenchidos
class Corrida(forms.Form):
    origem = forms.CharField(
        label="Origem",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Insira o local de embarque"
            }
        )
    )
    destino = forms.CharField(
        label="Destino",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Insira o destino final"
            }
        )
    )