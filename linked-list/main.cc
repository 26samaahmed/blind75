class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* current = head;
        ListNode* previous = nullptr;
        ListNode* next_node;

        while (current != nullptr) {
            next_node = current->next;
            current->next = previous;
            previous = current;
            current = next_node;
        }
        head = previous;
        return head;
    }
    
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummyNode(0);
        ListNode* list3 = &dummyNode;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                list3->next = list1;
                list1 = list1->next;
            } else {
                list3->next = list2;
                list2 = list2->next;
            }

            list3 = list3->next; // update new list's tail
        }

        // if there's still more to one of the lists then just append it
        if (list2 != nullptr) {
            list3->next = list2;
        }

        if (list1 != nullptr) {
            list3->next = list1;
        }

        return dummyNode.next; // to skip dummy node and return new list
    }
};
