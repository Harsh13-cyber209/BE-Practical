
import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Generate Huffman Codes
def generate_codes(root, code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = code or "0"
        return

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)


# Huffman Encoding
def huffman_encoding(data):

    if not data:
        return {}

    # Calculate frequency
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1

    # Create Min Heap
    heap = []

    for char, frequency in freq.items():
        heapq.heappush(heap, Node(char, frequency))

    # Build Huffman Tree
    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)

        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # Generate Huffman Codes
    codes = {}
    generate_codes(heap[0], "", codes)

    return codes


# Main Program
data = input("Enter a string: ")

codes = huffman_encoding(data)

print("\nHuffman Codes:")
for char, code in codes.items():
    print(char, ":", code)

encoded = "".join(codes[char] for char in data)
print("\nEncoded String:", encoded)
