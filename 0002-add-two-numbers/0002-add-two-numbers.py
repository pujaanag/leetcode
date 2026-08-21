# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = None
        temp = None

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry
            digit = total % 10
            carry = total // 10

            new = ListNode(digit)

            if head is None:
                head = new
                temp = new
            else:
                temp.next = new
                temp = temp.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return head