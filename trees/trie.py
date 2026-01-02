# Trie (Prefix Tree) — Explained Like a Pro
# 🔑 What is a Trie?
# A tree-based data structure used to store a set of strings (usually words) in a way that allows:
# Super-fast prefix-based search
# Efficient word dictionary representation
# Used in autocomplete, spell-check, IP routing, AI search trees

# 📌 Real-Life Example:
# Let’s say you insert these words:
# cat
# car
# cart
# can
# They’ll share common prefixes like "ca" and branch only when they differ — saving space + boosting search.

# 🧠 Why Use a Trie Instead of List/Set?
# Task	List/Set	Trie
# Search whole word	O(n) per word	O(k), where k = length of word
# Search by prefix	❌ slow (scan all)	✅ very fast
# Memory efficient for lots of similar words	❌ repeated prefixes waste space	✅ prefixes shared
# Supports autocomplete?	❌ no	✅ yes

# 🧠 Summary:
# Concept	Key
# Trie = Tree for strings	✅ Efficient prefix search
# Fast insert/search by character	✅ O(k)
# Best for autocomplete & dictionary-like data	✅ Absolutely

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end_of_word = False
#         self.prefix_count = 0  # To count how many words pass through this node

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         current = self.root
#         for ch in word:
#             if ch not in current.children:
#                 current.children[ch] = TrieNode()
#             current = current.children[ch]
#             current.prefix_count += 1  # update prefix count at each node
#         current.end_of_word = True

#     def search(self, word):
#         current = self.root
#         for ch in word:
#             if ch not in current.children:
#                 return False
#             current = current.children[ch]
#         return current.end_of_word

#     def startsWith(self, prefix):
#         current = self.root
#         for ch in prefix:
#             if ch not in current.children:
#                 return False
#             current = current.children[ch]
#         return True

#     def count_words_with_prefix(self, prefix):
#         current = self.root
#         for ch in prefix:
#             if ch not in current.children:
#                 return 0
#             current = current.children[ch]
#         return current.prefix_count

#     def suggest_words(self, prefix):
#         def dfs(node, path, results):
#             if node.end_of_word:
#                 results.append(''.join(path))
#             for ch, child in node.children.items():
#                 path.append(ch)
#                 dfs(child, path, results)
#                 path.pop()

#         current = self.root
#         for ch in prefix:
#             if ch not in current.children:
#                 return []  # No suggestions
#             current = current.children[ch]

#         results = []
#         dfs(current, list(prefix), results)
#         return results

# trie = Trie()
# words = ["car", "care", "cat", "cart", "cater", "dog", "dove", "doom"]
# for word in words:
#     trie.insert(word)

# print("Search 'car':", trie.search("car"))  # ✅ True
# print("Search 'card':", trie.search("card"))  # ❌ False

# print("Starts with 'ca':", trie.startsWith("ca"))  # ✅ True
# print("Starts with 'doz':", trie.startsWith("doz"))  # ❌ False

# print("Word suggestions for 'car':", trie.suggest_words("car"))  
# # ['car', 'care', 'cart']

# print("Word suggestions for 'do':", trie.suggest_words("do"))  
# # ['dog', 'dove', 'doom']

# print("Count words with prefix 'ca':", trie.count_words_with_prefix("ca"))  # 5
# print("Count words with prefix 'do':", trie.count_words_with_prefix("do"))  # 3




class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True
        
    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.is_end
    
    def starts_with(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True
    
    def suggest_words(self, prefix):
        def dfs(node, path, results):
            if node.is_end:
                results.append(''.join(path))
            for ch, child in node.children.items():
                path.append(ch)
                dfs(child, path, results)
                path.pop()

        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return []  # No suggestions
            current = current.children[ch]

        results = []
        dfs(current, list(prefix), results)
        return results

trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")
print(trie.search("apple"))   
print(trie.search("app"))        
print(trie.search("appl"))      
print(trie.starts_with("appl"))  
print(trie.starts_with("banana"))
print("Word suggestions for 'ap':", trie.suggest_words("ap"))  
