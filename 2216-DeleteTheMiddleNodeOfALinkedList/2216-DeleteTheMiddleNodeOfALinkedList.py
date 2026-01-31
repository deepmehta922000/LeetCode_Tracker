# Last updated: 1/31/2026, 2:18:45 PM
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # current = head
        # count = 1

        # # Count the number of nodes in the linked list
        # while current.next:
        #     count += 1
        #     current = current.next

        # # Calculate the index of the middle node

        # mid = count // 2

        # current = head
        # prev = None

        # # Traverse the linked list again to find the middle node
        # for i in range(mid):
        #     prev = current
        #     current = current.next

        # # Connect the previous node to the next node, effectively removing the middle node
        # if prev:
        #     prev.next = current.next
        # else:
        #     # If the head is the middle node, update the head
        #     head = current.next

        # return head

        if not head or not head.next:
        # If the list is empty or has only one node, there is no middle to delete
            return None

        slow_pointer = head
        fast_pointer = head
        prev_node = None

        while fast_pointer and fast_pointer.next:
            prev_node = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        # At this point, slow_pointer is at the middle node
        # Delete the middle node by updating the next pointer of the previous node
        prev_node.next = slow_pointer.next

        return head

