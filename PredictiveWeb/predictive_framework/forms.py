from django import forms


class PredictForm(forms.Form):
    claims = forms.CharField(label='Number of Claims',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Claims'}))

    appeal_category = forms.CharField(label='Appeal Category',
                                      widget=forms.TextInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Appeal Category'}))

    medicare_part = forms.CharField(label='Medicare Part',
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Medicare Part'}))

    requestor_type = forms.CharField(label='Requestor Type',
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Requestor Type'}))

    state = forms.CharField(label='State',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))

    psc_zpic = forms.CharField(label='PSC/ZPIC',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PSC/ZPIC'}))

    rac = forms.CharField(label='RAC',
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RAC'}))

    procedure_code = forms.CharField(label='Procedure Code',
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Procedure Code'}))




