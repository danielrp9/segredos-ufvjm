# fofocas/forms.py

from django import forms
from .models import Fofoca, Comentario

class FofocaForm(forms.ModelForm):
    class Meta:
        model = Fofoca
        fields = ['titulo', 'corpo', 'tags']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-input block w-full rounded-xl border-none bg-[var(--primary-100)] px-4 py-3 text-base text-[#1c1c0d] placeholder:text-[#9e9d47] focus:outline-none focus:ring-2 focus:ring-[var(--primary-700)]',
                'placeholder': 'Dê um título quente para sua fofoca'
            }),
            'corpo': forms.Textarea(attrs={
                'class': 'form-textarea block w-full resize-none rounded-xl border-none bg-[var(--primary-100)] px-4 py-3 text-base text-[#1c1c0d] placeholder:text-[#9e9d47] focus:outline-none focus:ring-2 focus:ring-[var(--primary-700)]',
                'placeholder': 'Conte-nos todos os detalhes...',
                'rows': '8'
            }),
            'tags': forms.RadioSelect(),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['corpo']
        widgets = {
            'corpo': forms.Textarea(attrs={'placeholder': 'Adicionar comentário anônimo'}),
        }