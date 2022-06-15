"""
Meeting Rooms
tags : Intervals

Input: [[0,30],[5,10],[15,20]]
Output: false

Input: [[7,10],[2,4]]
Output: true

給出一些會議時間, 看能不能全部參加, 如不能則false

重疊(overlap) : a, b, a的起點介於b的起點和終點之間, ab互換在比較一次

1.倆倆互相比較
    Time Complex : O(N x 1/2 x N) >> O(N^2)
    Space Complex : O(0)
2.先依照起點排序
    Time Complex : O(NlogN)(排序NlogN + N遍歷)
    Space Complex : O(0)


"""


def solve1(intervals):
    for i in range(len(intervals) - 1):
        for j in range(i + 1, len(intervals)):
            if intervals[j][0] >= intervals[i][0] and intervals[j][0] <= intervals[i][1]:
                return False
            if intervals[i][0] >= intervals[j][0] and intervals[i][0] <= intervals[j][1]:
                return False
    return True


def solve2(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] >= intervals[i-1][0] and intervals[i][0] <= intervals[i-1][1]:
            return False
    return True


if __name__ == '__main__':
    print('Solve1 : two loop')
    print(solve1([[0, 30], [5, 10], [15, 20]]))  # False
    print(solve1([[9, 15], [5, 10]]))  # False
    print(solve1([[7, 10], [2, 4]]))  # True

    print('Solve2 : Sort and one loop')
    print(solve2([[0, 30], [5, 10], [15, 20]]))  # False
    print(solve2([[9, 15], [5, 10]]))  # False
    print(solve2([[7, 10], [2, 4]]))  # True
