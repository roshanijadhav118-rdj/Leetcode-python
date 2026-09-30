class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second
