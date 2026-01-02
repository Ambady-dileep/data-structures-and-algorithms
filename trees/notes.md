✅ What Are Linear and Non-Linear Data Structures?
   Term	                                  Meaning
Linear DS	    Data elements are arranged in a sequence (one after the other).
Non-Linear DS	Data elements are connected in a hierarchical or graph structure.

What is an AVL Tree?
An AVL Tree is a special kind of Binary Search Tree (BST) that keeps itself balanced all the time.
🔥 Why AVL Tree?
👉 In a regular BST, if you insert sorted data (like 1,2,3,4), it becomes a linked list, not a tree.
That’s bad. Searching becomes O(n) instead of O(log n). AVL Tree fixes that by balancing the tree after every insert/delete so it stays efficient.
⚙️ Core Concepts: ✅ Balance Factor
For every node : Balance Factor = height(left subtree) - height(right subtree)
Allowed values: -1, 0, or +1
If it's more than that, the tree is unbalanced and needs rotation.
It tells you if the node is "leaning" more to the left or right.
🔁 Rotations
When the tree is unbalanced, we rotate the nodes to restore balance.
Case	          Rotation Type
Left-Left (LL)	  Right Rotation
Right-Right (RR)  Left Rotation
Left-Right (LR)	  Left + Right Rotation
Right-Left (RL)	  Right + Left Rotation
🚀 Summary — Remember This:
AVL = Self-Balancing BST
Ensures height difference (balance factor) is always -1, 0, or +1
Rotations fix imbalance
Keeps operations O(log n)
🧠 Core AVL Tree Summary
Topic	              Explanation
✅ It’s a BST	    With added balancing on each insertion/deletion
✅ Balance Factor	Must always be -1, 0, or +1
✅ Rotations	        LL, RR, LR, RL fix imbalances
✅ Operations	    Insert, Delete, Search = O(log n)
✅ Use case	        When you want a guaranteed balanced BST (better than regular BSTs when data is skewed)
"AVL Trees are better than normal BSTs because they maintain strict balance. In a regular BST, if we insert sorted data, the tree can become highly unbalanced, behaving like a linked list with O(n) time for search. But AVL Trees automatically perform rotations to ensure the tree stays balanced, keeping all operations at O(log n) time."

🔍 Breakdown (in your own words style):
✅ BST doesn’t fix itself — so sorted inserts like 10, 20, 30, 40 → make it a straight line → worst case
✅ AVL checks the balance factor after every insert
✅ If any node becomes too tall (imbalance > 1), AVL auto-rotates to fix it
✅ So it stays fast and reliable even if data is not random























