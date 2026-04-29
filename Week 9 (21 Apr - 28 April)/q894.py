
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        
        def solve(n):
            if n in memo:
                return memo[n]
            
            res = []
           
            if n == 1:
                return [TreeNode(0)]
            
            # only odd
            if n % 2 == 0:
                return []
            
            for left_nodes in range(1, n, 2):
                right_nodes = n - 1 - left_nodes
                
                left_trees = solve(left_nodes)
                right_trees = solve(right_nodes)
                
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
            
            memo[n] = res
            return res
        
        return solve(n)