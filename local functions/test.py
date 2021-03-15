# # def heapify(arr, n, i):
# #     largest = i  # Initialize largest as root
# #     l = 2 * i + 1  # left = 2*i + 1
# #     r = 2 * i + 2  # right = 2*i + 2
# #
# #     # See if left child of root exists and is
# #     # greater than root
# #     if l < n and arr[largest] < arr[l]:
# #         largest = l
# #
# #     # See if right child of root exists and is
# #     # greater than root
# #     if r < n and arr[largest] < arr[r]:
# #         largest = r
# #
# #     # Change root, if needed
# #     if largest != i:
# #         arr[i], arr[largest] = arr[largest], arr[i]  # swap
# #         print(arr)
# #         # Heapify the root.
# #         heapify(arr, n, largest)
# #
# #
# # # The main function to sort an array of given size
# #
# #
# # def heapSort(arr):
# #     n = len(arr)
# #
# #     # Build a maxheap.
# #     for i in range(n // 2 - 1, -1, -1):
# #         heapify(arr, n, i)
# #
# #     # One by one extract elements
# #     for i in range(n - 1, 0, -1):
# #         arr[i], arr[0] = arr[0], arr[i]  # swap
# #         heapify(arr, i, 0)
# #
# #
# # # Driver code
# # arr = [1,3,6,7,9]
# # heapSort(arr)
# # n = len(arr)
# # print("Sorted array is")
# # for i in range(n):
# #     print("%d" % arr[i]),
# # # This code is contributed by Mohit Kumra
#
# # ython
# # program
# # for
#
#
# # implementation of Horner Method
# # for Polynomial Evaluation
#
# # returns value of poly[0]x(n-1)
# # + poly[1]x(n-2) + .. + poly[n-1]
# def horner(poly, n, x):
#     # Initialize result
#     result = poly[0]
#
#     # Evaluate value of polynomial
#     # using Horner's method
#     for i in range(1, n):
#         result = result * x + poly[i]
#         print(result)
#     return result
#
#
# # Driver program to
# # test above function.
#
# # Let us evaluate value of
# # 2x3 - 6x2 + 2x - 1 for x = 3
# poly = [5, -2, 3, -4,8]
# x = 2
# n = len(poly)
#
# print("Value of polynomial is ", horner(poly, n, x))
#
# # This code is contributed
# # by Anant Agarwal.
