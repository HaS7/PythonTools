# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # see you again
        # 深复制
        # 展示一个杂技
        copy = pHead
        while copy:
            temp = RandomListNode(copy.label)
            temp.next = copy.next
            copy.next = temp
            copy = temp.next

        copy = pHead

        ret = RandomListNode(0)
        ret_copy = ret
        while copy and copy.next:
            copy.next.random = copy.random.next if copy.random else None
            copy = copy.next.next
        copy = pHead

        while copy and copy.next:
            ret_copy.next = copy.next
            ret_copy = ret_copy.next
            copy.next = copy.next.next
            copy = copy.next

        return ret.next



s1 = RandomListNode(1)

s2 = RandomListNode(2)

s3 = RandomListNode(3)

s4 = RandomListNode(4)

s5 = RandomListNode(5)

s1.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s1.random = s3
s2.random = s5
s4.random = s2

su = Solution()

ret = su.Clone(s1)

temp = ret

while temp:
    print(temp, temp.label, temp.random.label if temp.random else "None")
    temp = temp.next




