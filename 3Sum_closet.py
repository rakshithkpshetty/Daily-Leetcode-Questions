'''
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

'''
class Solution:#--------------------------------------
    def threeSumClosest(self, nums: List[int], target: int) -> int: 
        #-4, -1 1,2
        #close--->(-4 ....)--->-4
        close=float("inf");
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    cur_sum=nums[i]+nums[j]+nums[k];
                    if(abs(cur_sum-target)<abs(close)-target):
                        close=cur_sum;
        return close;
#-------------------------------------------------------------
'''
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int close=Integer.MAX_VALUE/2;
        for(int i=0;i<nums.length-2;i++){
            for(int  j=i+1;j<nums.length-1;j++){
                for(int k=j+1;k<nums.length;k++){
                    int cur_sum=nums[i]+nums[j]+nums[k];
                    if(Math.abs(cur_sum-target)<Math.abs(close-target)){
                        close=cur_sum;
                    }
                }
            }
        }
        return close;
    }
}
'''
        

    


        