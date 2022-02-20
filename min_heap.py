# Course: CS261 - Data Structures
# Assignment: 5
# Student: Remington Wimberly
# Description:


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def parent_node(self, i):
        """ returns index of parent node"""
        return (i - 1) // 2

    def right_child(self, i):
        """ returns index of right child node"""
        return i * 2 + 2

    def left_child(self, i):
        """ returns index of left child node"""
        return i * 2 + 1

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the min heap maintaining the heap property
        """
        self.heap.append(node)

        i = self.heap.length() - 1

        while i > 0:
            if self.heap.get_at_index(i) < self.heap.get_at_index(self.parent_node(i)):
                self.heap.swap(i, self.parent_node(i))
            i = self.parent_node(i)

    def get_min(self) -> object:
        """
        returns an object with a minimum key without removing it from the heap
        """
        if self.is_empty():
            raise MinHeapException()
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        returns an object with a minimum key and removes it from the heap
        """
        min_value = self.get_min()
        end_value = self.heap.pop()

        # if self.is_empty():
        #     raise MinHeapException()
        if self.heap.length() == 0:
            # return the element at index 0 of length is zero
            return min_value
        else:
            # put the value at the end and have it bubble through the heap
            self.heap.set_at_index(0, end_value)

            i = 0

            while i < self.heap.length():

                lesser_child = None
                current_value = self.heap.get_at_index(i)

                if self.left_child(i) < self.heap.length() and current_value > self.heap.get_at_index(self.left_child(i)):
                    lesser_child = self.left_child(i)
                    current_value = self.heap.get_at_index(self.left_child(i))

                if self.right_child(i) < self.heap.length() and current_value > self.heap.get_at_index(self.right_child(i)):
                    lesser_child = self.right_child(i)
                    current_value = self.heap.get_at_index(self.right_child(i))


                if lesser_child is not None:
                    self.heap.swap(i, lesser_child)
                    i = lesser_child
                else:
                    break

        return min_value


    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        self.heap = DynamicArray()

        for i in range(da.length()):
            self.heap.append(da.get_at_index(i))

            # self.add(i)

# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)
