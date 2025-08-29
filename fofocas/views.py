# fofocas/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from .models import Fofoca, Comentario
from .forms import FofocaForm, ComentarioForm

def lista_fofocas(request):
    fofocas = Fofoca.objects.all().order_by('-data_publicacao')
    filtro = request.GET.get('filtro')
    if filtro:
        fofocas = fofocas.filter(tags=filtro)
    return render(request, 'fofocas/lista_fofocas.html', {'fofocas': fofocas, 'filtro': filtro})

def detalhes_fofoca(request, pk):
    fofoca = get_object_or_404(Fofoca, pk=pk)
    top_level_comentarios = fofoca.comentarios.filter(parent_comment__isnull=True).order_by('data_comentario')
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.fofoca = fofoca
            parent_id = request.POST.get('parent_comment_id')
            if parent_id:
                comentario.parent_comment = Comentario.objects.get(id=parent_id)
            comentario.save()
            return redirect('detalhes_fofoca', pk=fofoca.pk)
    else:
        form = ComentarioForm()
    return render(request, 'fofocas/detalhes_fofoca.html', {'fofoca': fofoca, 'comentarios': top_level_comentarios, 'form': form})

def nova_fofoca(request):
    if request.method == 'POST':
        form = FofocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fofocas')
    else:
        form = FofocaForm()
    return render(request, 'fofocas/nova_fofoca.html', {'form': form})

@require_POST
def reagir_fofoca(request):
    try:
        data = json.loads(request.body)
        fofoca_id = data.get('fofoca_id')
        reacao_tipo = data.get('reacao_tipo')
        
        fofoca = get_object_or_404(Fofoca, id=fofoca_id)

        # Mapeia o tipo de reação para o nome do campo no modelo
        campo_reacao = {
            'feliz': 'reacao_feliz',
            'triste': 'reacao_triste',
            'bravo': 'reacao_bravo',
            'surpreso': 'reacao_surpreso',
        }.get(reacao_tipo)

        if campo_reacao:
            # Incrementa o contador do campo correto de forma dinâmica
            setattr(fofoca, campo_reacao, getattr(fofoca, campo_reacao) + 1)
            fofoca.save()

        # Retorna os novos contadores em formato JSON
        return JsonResponse({
            'reacao_feliz': fofoca.reacao_feliz,
            'reacao_triste': fofoca.reacao_triste,
            'reacao_bravo': fofoca.reacao_bravo,
            'reacao_surpreso': fofoca.reacao_surpreso,
        })
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Requisição inválida.'}, status=400)
    except Fofoca.DoesNotExist:
        return JsonResponse({'error': 'Fofoca não encontrada.'}, status=404)