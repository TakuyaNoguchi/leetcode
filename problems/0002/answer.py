from typing import List

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    sum = int(''.join(reversed(self.__listNodeToList(l1)))) + int(''.join(reversed(self.__listNodeToList(l2))))

    return self.__listToListNode(list(map(int, reversed(list(str(sum))))))

  def __listNodeToList(self, listNode: ListNode) -> List:
    l = []
    while True:
      l.append(str(listNode.val))

      if listNode.next is None:
        break

      listNode = listNode.next

    return l

  def __listToListNode(self, l: List) -> ListNode:
    firstnode = ListNode(l[0])
    prevnode = firstnode

    for n in l[1:len(l)]:
      listnode = ListNode(n)

      prevnode.next = listnode
      prevnode = listnode

    return firstnode

# 以降は動作確認用
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
listnode = Solution().addTwoNumbers(l1, l2)

while True:
  print(listnode.val, end = '')
  listnode = listnode.next

  if listnode is None:
    break
print()

l1 = ListNode(0)
l2 = ListNode(0)
listnode = Solution().addTwoNumbers(l1, l2)

while True:
  print(listnode.val, end = '')
  listnode = listnode.next

  if listnode is None:
    break
print()

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
listnode = Solution().addTwoNumbers(l1, l2)

while True:
  print(listnode.val, end = '')
  listnode = listnode.next

  if listnode is None:
    break
print()

l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
listnode = Solution().addTwoNumbers(l1, l2)

while True:
  print(listnode.val, end = '')
  listnode = listnode.next

  if listnode is None:
    break
print()