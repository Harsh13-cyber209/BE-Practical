import heapq

def huffman(chars, freq):

    heap = []

    for i in range(len(chars)):
        heapq.heappush(heap, (freq[i], chars[i]))

    while len(heap) > 1:

        f1, left = heapq.heappop(heap)
        f2, right = heapq.heappop(heap)

        new_node = (left, right)

        heapq.heappush(heap, (f1 + f2, new_node))

    def print_codes(node, code=""):

        if isinstance(node, str):
            print(node, ":", code)
            return

        left, right = node

        print_codes(left, code + "0")
        print_codes(right, code + "1")

    print("Huffman Codes:")
    print_codes(heap[0][1])


# Main Program
chars = ['A', 'B', 'C', 'D']
freq = [5, 9, 12, 13]

huffman(chars, freq)
