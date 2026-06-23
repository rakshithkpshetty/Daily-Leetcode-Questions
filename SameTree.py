'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 
'''# Definition for a binary tree node.
# class TreeNode:
#     defhttps://assets.leetcode.com/uploads/2020/12/20/ex3.jpg$0 __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p is None and q is None):
            return True
        if(p is None or q is None):
            return False
        if(p.val!=q.val):
            return False;
        return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)

        #-----------------------------------------------------------------------------------
        '''
        /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if((p ==  null) && (q == null)){
            return true;
        }
        if(p ==  null || q == null){
            return false;
        }
        if(p.val!= q.val){

            return false;
        }{
        return (isSameTree(p.left, q.left)) && ( isSameTree(p.right, q.right));}
        
    }
}
      /**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    
     if((p ===  null) && (q === null)){
            return true;
        }
        if(p ===  null || q === null){
            return false;
        }
        if(p.val!= q.val){

            return false;
        }{
        return (isSameTree(p.left, q.left)) && ( isSameTree(p.right, q.right));}
    
};  
        
    /**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {


     if((p ===  null) && (q === null)){
            return true;
        }
        if(p ===  null || q === null){
            return false;
        }
        if(p.val!= q.val){

            return false;
        }{
        return (isSameTree(p.left, q.left)) && ( isSameTree(p.right, q.right));}
    
};
        |
        /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public bool IsSameTree(TreeNode p, TreeNode q) {
         if((p ==  null) && (q == null)){
            return true;
        }
        if(p ==  null || q == null){
            return false;
        }
        if(p.val!= q.val){

            return false;
        }{
        return (IsSameTree(p.left, q.left)) && ( IsSameTree(p.right, q.right));}
        
    }
}'''