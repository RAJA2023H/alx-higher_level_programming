#include "lists.h"

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: A pointer to a pointer to the head of the linked list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *mid = NULL;
    int is_palindrome = 1;

    if (!head || !*head || !((*head)->next))
        return (1);

    // Find the middle of the linked list
    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast)
    {
        // List has an odd number of elements, so skip the middle one
        mid = slow;
        slow = slow->next;
    }

    // Reverse the second half of the linked list
    listint_t *second_half = NULL;
    while (slow)
    {
        listint_t *next = slow->next;
        slow->next = second_half;
        second_half = slow;
        slow = next;
    }

    // Compare the first half and reversed second half
    listint_t *first_half = *head;
    while (second_half)
    {
        if (first_half->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the original linked list
    while (prev)
    {
        listint_t *next = prev->next;
        prev->next = mid;
        mid = prev;
        prev = next;
    }

    return is_palindrome;
}
