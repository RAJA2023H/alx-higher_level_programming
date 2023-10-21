#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev = NULL, *mid = NULL;
    int is_palindrome = 1;

    if (!*head || !(*head)->next)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast)
    {
        mid = slow;
        slow = slow->next;
    }

    listint_t *second_half = reverse_list(&slow);
    listint_t *first_half = *head;

    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    if (mid)
    {
        prev->next = mid;
        mid->next = reverse_list(&slow);
    }
    else
    {
        prev->next = reverse_list(&slow);
    }

    return is_palindrome;
}

listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return prev;
}
