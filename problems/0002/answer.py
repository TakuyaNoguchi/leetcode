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