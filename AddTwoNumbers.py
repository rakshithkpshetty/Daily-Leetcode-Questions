'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Step 1: Convert linked lists to Python lists
        a = []
        b = []
        
        while l1:
            a.append(l1.val)
            l1 = l1.next
        # Example output: a = [2, 4, 3]
        
        while l2:
            b.append(l2.val)
            l2 = l2.next
        # Example output: b = [5, 6, 4]
        
        
        # Step 2: Reverse lists and convert to numbers
        num1 = int("".join(map(str, a[::-1])))
        # a[::-1] = [3, 4, 2]
        # num1 = 342
        
        num2 = int("".join(map(str, b[::-1])))
        # b[::-1] = [4, 6, 5]
        # num2 = 465
        
        
        # Step 3: Add the two numbers
        total = num1 + num2
        # total = 342 + 465 = 807
        
        
        # Step 4: Convert sum to reversed digit list
        digits = list(map(int, str(total)))[::-1]
        # str(total) = "807"
        # digits = [7, 0, 8]
        
        
        # Step 5: Convert list to linked list
        dummy = ListNode(0)
        curr = dummy
        
        for d in digits:
            curr.next = ListNode(d)
            curr = curr.next
        # Linked list formed: 7 → 0 → 8
        
        
        return dummy.next