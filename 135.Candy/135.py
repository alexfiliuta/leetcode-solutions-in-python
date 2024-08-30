class Solution(object):
    def candy(self, ratings):
        candies = [1] * len(ratings)
        
        counter = 1
        while counter <= len(ratings) - 1:
            if ratings[counter] > ratings[counter-1]:
                candies[counter] = candies[counter-1] + 1
            counter += 1

        counter = len(ratings) - 2
        while counter >= 0:
            if ratings[counter] > ratings[counter+1] and not candies[counter] > candies[counter+1]:
                candies[counter] = candies[counter+1] + 1
            counter -= 1

        return 1 if len(ratings) == 1 else sum(candies)
        """
        :type ratings: List[int]
        :rtype: int
        """