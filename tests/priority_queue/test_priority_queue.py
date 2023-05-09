from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    high_priority_file_1 = {
        "nome_do_arquivo": "arquivo_teste_priority_1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["Teste", "Teste", "Teste"],
    }

    high_priority_file_2 = {
        "nome_do_arquivo": "arquivo_teste_priority_2.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ["Teste", "Teste"],
    }

    regular_priority_file_1 = {
        "nome_do_arquivo": "arquivo_teste_regular_1.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "Teste",
            "Teste",
            "Teste",
            "Teste",
            "Teste",
            "Teste",
        ],
    }

    regular_priority_file_2 = {
        "nome_do_arquivo": "arquivo_teste_regular_2.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": ["Teste", "Teste" "Teste", "Teste", "Teste"],
    }

    queue = PriorityQueue()
    queue.enqueue(regular_priority_file_1)
    queue.enqueue(high_priority_file_1)
    queue.enqueue(regular_priority_file_2)
    queue.enqueue(high_priority_file_2)

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(7)

    # Ordem de prioridade:
    # [
    #   high_priority_file_1,
    #   high_priority_file_2,
    #   regular_priority_file_1,
    #   regular_priority_file_2
    # ]

    assert len(queue.high_priority) == 2
    assert len(queue.regular_priority) == 2
    assert len(queue) == 4
    assert queue.search(1) == high_priority_file_2
    assert queue.search(2) == regular_priority_file_1
    assert queue.dequeue() == high_priority_file_1
    assert queue.dequeue() == high_priority_file_2
    assert queue.dequeue() == regular_priority_file_1
    assert queue.dequeue() == regular_priority_file_2
