# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode(0,None)
        if l1 != None and l2 != None:
            value = l1.val + l2.val
            if value >= 10:
                value = value - 10
                if l1.next == None:
                    l1.next = ListNode(0,None)
                l1.next.val += 1
            ans.val = value
            ans.next = Solution.addTwoNumbers(self,l1.next,l2.next)
        elif l1 == None and l2 != None:
            if l2.val >= 10:
                ans.val = l2.val - 10
                ans.next = Solution.addTwoNumbers(self,ListNode(1,None),l2.next)
            else:
                ans.val = l2.val
                ans.next = Solution.addTwoNumbers(self,None,l2.next)
        elif l1 != None and l2 == None:
            if l1.val >= 10:
                ans.val = l1.val - 10
                ans.next = Solution.addTwoNumbers(self,l1.next,ListNode(1,None))
            else:
                ans.val = l1.val
                ans.next = Solution.addTwoNumbers(self,l1.next,None)
        else:
            return None    
        
        return ans

"""
Accept with one attempt
https://leetcode.com/problems/add-two-numbers/
"""
