from typing import Optional


class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check if list empty then no point merge, return another list
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # smallest number be head
        if list1.val < list2.val:
            head = ListNode(list1.val)
            tail = head
            list1 = list1.next  # replace previous node
        else:
            head = ListNode(list2.val)
            tail = head
            list2 = list2.next

        # tail construction start here
        # Loop until any of the list becomes empty
        while list1 is not None and list2 is not None:
            # connect small number first
            if list1.val < list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            tail = tail.next  # current tail set to new tail

        # connect all the nodes, if remaining left in list
        while list1 is not None:
            tail.next = ListNode(list1.val)
            list1 = list1.next
            tail = tail.next

        while list2 is not None:
            tail.next = ListNode(list2.val)
            list2 = list2.next
            tail = tail.next

        # return the listNode
        return head

# function to convert list of number into listnode


def listToListNode(list):
    if not list:
        return None

    head = ListNode(list[0])
    nextElement = head
    i = 1
    while i < len(list):
        nextElement.next = ListNode(list[i])
        nextElement = nextElement.next
        i += 1
    return head

# function to convert listnode to list


def listNodetoList(listNode: ListNode):
    currentNode = listNode
    list = []
    while True:
        list.append(currentNode.val)
        if(currentNode.next is None):
            break
        currentNode = currentNode.next
    return list


list1 = [1, 2, 4]
listNode1 = listToListNode(list1)
list2 = [1, 3, 4, 5, 6]
listNode2 = listToListNode(list2)
listNodeResult = Solution().mergeTwoLists(listNode1, listNode2)
result = listNodetoList(listNodeResult)
print(result)
