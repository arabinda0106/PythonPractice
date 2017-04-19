import math
import string
import re
import random


from math import sin, cos, radians
import sys
    

def make_dot_strings(x):
    return ' '*int(10*cos(radians(x)) + 10) + 'o'

assert make_dot_strings(90) == '          o'
assert make_dot_strings(180) == 'o'
    
def segmentsIntersection(left, right):

    answer = 0
    events = []
    opened = 0

    for i in range(len(left)):
        events.append([left[i], 1])
        events.append([right[i], -1])

    events.sort()

    for i in range(len(events)):
        if opened == len(left):
            opened += events[i][0] - events[i - 1][0]
        opened += events[i][1]

    return answer


def bijectiveBase10(a):
    result = []
    strResult = []
    while a > 0:
        result.append(a % 10)
        a //= 10
    for i in range(len(result)):
        if i + 1 < len(result) and result[i] <= 0:
            result[i] += 10
            result[i + 1] -= 1
    for i in range(len(result)):
        if result[i] == 10:
            strResult.append('A')
        elif result[i] != 0 or i != len(result) - 1:
            strResult.append(chr(ord('0') + result[i]))
    return ''.join(reversed(strResult))

def levenshteinDistance(string1, string2):

    len1 = len(string1)
    len2 = len(string2)
    dp = []
    for i in range(len1 + 1):
        dp.append([0] * (len2 + 1))
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                continue
            dp[i][j] = 1 + min(dp[i - 1][j - 1],
                    min(dp[i][j - 1], dp[i - 1][j]))

    return 4

def uberPool(A, B, C, X, Y):

    def distance(P, Q):
        return abs(P[0] - Q[0]) + abs(P[1] - Q[1])

    initialDist = distance(A, B)
    travelledDist = distance(A, C)
    D = [X, Y]
    remainingDist = [0, 0]
    for i in range(2):
        remainingDist[i] = distance(C, D[i]) + distance(D[i], B)

    best = 1
    if remainingDist[0] > remainingDist[1]:
        best = 2

    if  (remainingDist[0] + travelledDist) > initialDist * 2 and (remainingDist[1] + travelledDist) > initialDist * 2 :
        best = -1

    return best

def palindromeRearranging(inputString):

  count = [0] * 26
  for i in range(len(inputString)):
    count[ord(inputString[i]) - ord('a')] += 1

  odds = 0
  for i in range(26):
    if count[i] % 2 == 1:
      odds += 1

  return odds % 2 == len(inputString) % 2
 

def get_median(list):
    if len(list) % 2 == 0:
        return sum([list[:len(list)/2][0], list[len(list)/2:][1]])/2.0
    else:
        return len(list)/2.0
    
def priceSuggestion(contractData):
    if contractData:
        contractData = sorted(contractData)
        first_group = contractData[:len(contractData)/2]
        second_group = contractData[len(contractData)/2:]
        if len(first_group) % 2 == 0:
            first_median = first_group[int(get_median(first_group)-1)]
        else:
            first_median = first_group[int(get_median(first_group))]
        second_median = second_group[int(get_median(second_group))]
        return [first_median, second_median]
    return []

def main():
    #priceSuggestion([1, 5, 6, 3, 2, 4, 7, 8])
    palindromeRearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc")
    #uberPool([1, 1], [8, 1], [6, 1], [6, 5], [6, -5])
    uberPool([17, 49], [90, -72], [64, 24], [-64, 64], [-9, -87])
    #uberPool([0, 0], [3, 3], [3, 1], [5, 0], [2, 2])
    levenshteinDistance("fight", "friend")
    b1 = segmentsIntersection([1,2,3], [5,4,11])
        #s = make_dot_strings(100)
        #print(s)
        #a = 10
        #t = bijectiveBase10(a)
        #print(s)

    #for i in range(1000):
    #    s = make_dot_strings(i)
    #    print(s)

if __name__ == "__main__":
    sys.exit(int(main() or 0))

