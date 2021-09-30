import collections, heapq


def topKFrequent(self, nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []

    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])