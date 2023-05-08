from ting_file_management.abstract_queue import AbstractQueue
from collections import deque

# ref:
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/library/collections.html#collections.deque


# Para que as operações insert_first e remove_last
# tenham complexidade de tempo O(1), é possível usar
# Listas duplamente encadeadas (Doubly Linked Lists)
# ou Deques.


class Queue(AbstractQueue):
    def __init__(self):
        self._list = deque()

    def __len__(self):
        return len(self._list)

    def enqueue(self, value):
        self._list.append(value)

    def dequeue(self):
        # deque.popleft() lança IndexError se lista está vazia
        removed_element = self._list.popleft()
        return removed_element

    def search(self, index):
        if not (isinstance(index, int) and (0 <= index < len(self))):
            raise IndexError("Índice Inválido ou Inexistente")
        # Deque: _list[0] e _list[-1] -> O(1) ; _list[n] -> O(n)
        return self._list[index]
