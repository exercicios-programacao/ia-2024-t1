"""Implementa steps para teste do A*."""

from behave import given, then, when

import busca


@when('eu procuro o menor caminho com o algoritmo A*')
def _when_astar_algorithm_is_used(context):
    try:
        result = busca.a_star(
            context.graph, context.start, context.goal
        )
    except Exception as ex:
        context.exception = ex
        context.vertex_count = None
        context.length = None
        context.path = None
        raise ex from None
    else:
        assert result != None
        context.exception = None
        count, length, path = result
        context.vertex_count = count
        context.length = length
        context.path = path

