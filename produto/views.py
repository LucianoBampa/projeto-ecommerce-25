from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Lista de Produtos")


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Detalhe do Produto")


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Adicionar ao Carrinho")


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Remover do Carrinho")


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Carrinho de Compras")


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Finalizar Compra")
