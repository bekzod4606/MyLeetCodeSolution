def maxDistance(position, m):
        def min_dist(min_dist):
            prev_pos = position[0]
            count = 1
            for cur in position[1:]:
                if cur-prev_pos>=min_dist:
                    prev_pos = cur
                    count+=1
            return count>=m
        position.sort()
        left, right = 1, position[-1]-position[0]
        while left<right:
            mid = (left+right+1)//2
            if min_dist(mid):
                left = mid
            else:
                right = mid - 1
        return left