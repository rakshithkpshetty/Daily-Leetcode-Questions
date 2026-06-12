<<<<<<< HEAD
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
                res=[];
                nums.sort();
                for i in range(len(nums)):
                    j=i+1;
                    k=len(nums)-1;
                    if(i>0  and nums[i]==nums[i-1]):
                        continue;
                    while(j<k):
                        total=nums[i]+nums[j]+nums[k];
                        if(total>0):
                            k-=1;
                        elif(total<0):
                            j+=1;
                        else:
                            res.append([nums[i],nums[j],nums[k]])
                            j+=1;
                            while(nums[j]==nums[j-1] and j<k):
                                j+=1
                return res
    #--------------------------------------------------------
    '''
    
    🔎 Approach in Your Code
Sorting

First, the array is sorted. This makes it easier to avoid duplicates and to use the two-pointer technique effectively.

Fixing one element (i)

You iterate through the array with index i. For each nums[i], you try to find two other numbers (nums[j] and nums[k]) such that their sum equals -nums[i].

Skipping duplicates for i

If the current number is the same as the previous one (nums[i] == nums[i-1]), you skip it to avoid duplicate triplets.

Two-pointer search (j and k)

You set j = i+1 and k = nums.length-1.

Then, while j < k, you calculate the sum:

total=nums[i]+nums[j]+nums[k]
If total > 0, you move k-- (to reduce the sum).

If total < 0, you move j++ (to increase the sum).

If total == 0, you found a valid triplet.

Handling duplicates for j

After finding a valid triplet, you increment j and skip over duplicates (while nums[j] == nums[j-1]).

Collecting results

Each valid triplet is added to the result list.

⚠️ Limitations in Your Current Code
You only skip duplicates for j, but not for k. This can lead to duplicate triplets.

After finding a triplet, you only move j++ but not k--. Both should move inward to continue searching.

The loop for i should ideally run until nums.length - 2 (since you need at least three numbers).
    
    '''
    
    '''
    class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            
            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];

                if (total > 0) {
                    k--;
                } else if (total < 0) {
                    j++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;

                    while (nums[j] == nums[j-1] && j < k) {
                        j++;
                    }
                }
            }
        }
        return res;        
    }
}
    '''
=======
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
    res=[];
            nums.sort();
            for i in range(len(nums)):
                j=i+1;
                k=len(nums)-1;
                if(i>0  and nums[i]==nums[i-1]):
                    continue;
                while(j<k):
                    total=nums[i]+nums[j]+nums[k];
                    if(total>0):
                        k-=1;
                    elif(total<0):
                        j+=1;
                    else:
                        res.append([nums[i],nums[j],nums[k]])
                        j+=1;
                        while(nums[j]==nums[j-1] and j<k):
                            j+=1
            return res
    #--------------------------------------------------------
    '''
    class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            
            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];

                if (total > 0) {
                    k--;
                } else if (total < 0) {
                    j++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;

                    while (nums[j] == nums[j-1] && j < k) {
                        j++;
                    }
                }
            }
        }
        return res;        
    }
}
    '''
>>>>>>> 667cd5e94ae53b87a98b51e96766cb3435d7fb9f
    