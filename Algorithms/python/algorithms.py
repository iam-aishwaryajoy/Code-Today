import logging as log

class SearchAlgorithm:
    def linear_search(self, data, query):
        #T(C) = O(N) and S(C) = O(1)
        pos = 0

        while(pos < len(data)):
            if data[pos] == query:
                return pos
            else:
                pos = pos + 1

            if pos == len(data):
                return -1
        return -1


    def binary_search(self, data, query):
        low = 0
        high = len(data) - 1
        #data.sort(reverse=True)

        log.debug(" ")
        if len(data) < 20:
            log.debug("Data{},queryi{}".format(data, query))
        while(low <= high):
            mid = (low+high)//2
            mid_card = data[mid]
            if len(data) < 20:
                log.debug("LMH:{},{},{}".format(low, mid, high))

            if mid_card == query:
                if mid-1 >=0 and data[mid-1] == query:
                    high = mid -1
                else:
                    return mid
            elif mid_card < query:
                high = mid - 1
            elif mid_card > query:
                low = mid + 1

        return -1


