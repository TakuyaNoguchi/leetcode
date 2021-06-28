import unittest
from answer import Solution
from answer import ListNode

class SolutionTest(unittest.TestCase):
  def test_addTwoNumbers(self):
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    listnode = Solution().addTwoNumbers(l1, l2)
    for n in [7, 0, 8]:
      self.assertEqual(n, listnode.val)
      listnode = listnode.next
    self.assertIsNone(listnode)

    l1 = ListNode(0)
    l2 = ListNode(0)
    listnode = Solution().addTwoNumbers(l1, l2)
    for n in [0]:
      self.assertEqual(n, listnode.val)
      listnode = listnode.next
    self.assertIsNone(listnode)

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    listnode = Solution().addTwoNumbers(l1, l2)
    for n in [8, 9, 9, 9, 0, 0, 0, 1]:
      self.assertEqual(n, listnode.val)
      listnode = listnode.next
    self.assertIsNone(listnode)

    l1 = ListNode(2, ListNode(4, ListNode(9)))
    l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
    listnode = Solution().addTwoNumbers(l1, l2)
    for n in [7, 0, 4, 0, 1]:
      self.assertEqual(n, listnode.val)
      listnode = listnode.next
    self.assertIsNone(listnode)

if __name__ == "__main__":
  unittest.main()