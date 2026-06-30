'''In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i  in range(numRows):
            row=[1]
            for j in range(1,i):
                row.append(result[i-1][j-1]+result[i-1][j])
            if(i>0):
                row.append(1)
            result.append(row)
        return result;



        '''
        class Solution {
   public List<List<Integer>> generate(int numRows) {
        
        List<List<Integer>> result=new ArrayList<>();
        for(int i=0;i<numRows;i++){
            List<Integer>  row=new ArrayList<>();
            row.add(1);
            for(int j=1;j<i;j++){
                row.add(result.get(i-1).get(j-1)+result.get(i-1).get(j));
            }
            if(i>0){
                row.add(1);
            }
            result.add(row);
        }
        return result;



    }
}'''
        