"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
"""
import heapq

class Solution:
    # Heap solution
    # Time Complexity: O(N * lgN)
    # Space Complexity: O(N)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_points = []
        distances = [(val[0] ** 2 + val[1] ** 2, i) for i, val in enumerate(points)]
        heapq.heapify(distances) # O(nlgn) to create heap
        for i in range(k):
            point = heapq.heappop(distances)    # O(lgn) to pop and maintain heap property
            k_points.append(points[point[1]])
        
        return k_points
    
    
    # Quick Select solution
    # Time Complexity: O(N), Worst Case: O(N^2)
    # Space Complexity: O(1)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_points = []
        distances = [(val[0] ** 2 + val[1] ** 2, i) for i, val in enumerate(points)]
        distances = self.quick_select(distances, 0, len(distances) - 1, k)
        for val in distances:
            k_points.append(points[val[1]])
        return k_points
     
    def quick_select(self, lst, l, r, k):
        pivotIndex = len(lst)

        while pivotIndex != k-1:
            pivotIndex = self.partition(lst, l, r)
            if pivotIndex < k:
                l = pivotIndex + 1
            else:
                r = pivotIndex - 1

        return lst[:k]

    def partition(self, lst, l, r):
        """
        Lomuto Parition with random pivot to avoid sorted list O(N^2)
        """
        # Choose random pivot
        rand_int = random.randint(l, r)
        lst[r], lst[rand_int] = lst[rand_int], lst[r]
        
        pivot = lst[r][0]
        i = l
        for j in range(l, r):
            if lst[j][0] < pivot:
                if i != j:
                    lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[i], lst[r] =  lst[r], lst[i] 
        return i

    