def minDays(bloomDay, m, k):
        if len(bloomDay)<m*k:
            return -1
        def can_make_bouqet(day: int) -> bool:
            bouqets = 0
            flowers_in_row = 0
            for bloom in bloomDay:
                if bloom<=day:
                    flowers_in_row+=1
                    if flowers_in_row==k:
                        bouqets+=1
                        flowers_in_row=0
                else:
                    flowers_in_row=0
            return bouqets>=m

        left, right = min(bloomDay), max(bloomDay)
        while left<right:
            mid = (left+right)//2
            if can_make_bouqet(mid):
                right = mid
            else:
                left = mid+1
        return left