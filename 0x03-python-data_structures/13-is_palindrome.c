#include "lists.h"
listint_t* reverseList(listint_t* head)
{
    listint_t* prev = NULL;
    listint_t* current = head;
    listint_t* next;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}
bool compareLists(listint_t* list1, listint_t* list2)
{
	while (list1 != NULL && list2 != NULL) {
        if (list1->n != list2->n) {
            return false;
        }
        list1 = list1->next;
        list2 = list2->next;
    }
    return true;
}

int is_palindrome(listint_t **head) {
    listint_t* current = *head;

    if (current == NULL || current->next == NULL) {
        return 1;
    }

    listint_t* slow = current;
    listint_t* fast = current;
    listint_t* prev_slow = current;

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    listint_t* second_half = slow;
    if (fast != NULL)
    {
        second_half = slow->next;
    }

    prev_slow->next = NULL;

    second_half = reverseList(second_half);

    int is_palindrome = compareLists(current, second_half);

    second_half = reverseList(second_half);
    prev_slow->next = second_half;

    return is_palindrome;
}
