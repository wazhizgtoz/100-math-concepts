from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Modulo, Conceito


def index(request):
    """Página inicial com todos os conceitos agrupados por módulo"""
    modulos = Modulo.objects.prefetch_related("conceitos").all()
    total = Conceito.objects.count()
    concluidos = Conceito.objects.filter(concluido=True).count()

    context = {
        "modulos": modulos,
        "total": total,
        "concluidos": concluidos,
        "progresso": int((concluidos / total) * 100) if total > 0 else 0,
    }
    return render(request, "concepts/index.html", context)


def detalhe(request, slug):
    """Página de detalhes de um conceito específico"""
    conceito = get_object_or_404(Conceito, slug=slug)
    context = {
        "conceito": conceito,
        "modulo": conceito.modulo,
    }
    return render(request, "concepts/detalhe.html", context)


def toggle_concluido(request, conceito_id):
    """API para marcar/desmarcar conceito como concluído"""
    if request.method == "POST":
        conceito = get_object_or_404(Conceito, id=conceito_id)
        conceito.concluido = not conceito.concluido
        conceito.save()
        return JsonResponse(
            {
                "success": True,
                "concluido": conceito.concluido,
                "conceito_id": conceito.id,
            }
        )
    return JsonResponse({"success": False}, status=400)
