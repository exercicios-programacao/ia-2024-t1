"""Passos comuns aos testes."""

import os
from behave import given, then

import graph


@given('a descrição de um grafo a partir do arquivo "{filename}"')
def _given_a_map_from_file(context, filename):
    context.graph = graph.read_graph(os.path.join("mapas", filename))


@given('vértice inicial é {start:d}')
def _given_start_node(context, start):
    context.start = start


@given('vértice final é {goal:d}')
def _given_start_node(context, goal):
    context.goal = goal


@then('o número de vértices analisados é {expected}')
def _then_number_of_checked_vertices(context, expected):
    expected = list(map(int, expected.split(",")))
    assert context.exception is None, f"Exception: {str(context.exception)}"
    assert context.vertex_count in expected, (
        f"Número de vértices: {expected} != {context.vertex_count}"
    )


@then('o caminho encontrado é {expected}')
def step_impl(context, expected):
    assert context.exception is None, f"Exception: {str(context.exception)}"
    expected = [
        list(map(int, l.strip(" []").split(",")))
        for l in expected.split(";")
    ]
    assert context.path in expected, (
        f"Caminho:\n{expected}\n{context.path}"
    )

