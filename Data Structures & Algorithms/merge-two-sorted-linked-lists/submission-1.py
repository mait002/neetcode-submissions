# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # we have to check if either list is empty
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        # dummy node
        res = ListNode()

        # shorter notation
        l1 = list1
        l2 = list2

        #initial res to the smallest starting node
        if l1.val <= l2.val:
            res = l1
            l1 = l1.next
        else:
            res = l2
            l2 = l2.next
        
        # initial head
        head = res
        

        while res != None:
            
            # check if either list node points to null
            # if so, then no point traversing any further
            if l1 == None:
                res.next = l2
                break
            elif l2 == None:
                res.next = l1
                break

            # if l1.val <= l2.val, res.next will point to l1.val
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            
            else:
                res.next = l2
                l2 = l2.next

            # update to move res 
            res = res.next

        return head


            



                

