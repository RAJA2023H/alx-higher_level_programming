#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *second_half;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        // List has an odd number of nodes, skip the middle node
        slow = slow->next;
    }

    // Reverse the second half of the list
    prev->next = NULL;
    second_half = reverse_list(&slow);

    // Compare the first half and the reversed second half
    is_palindrome = compare_lists(*head, second_half);

    // Restore the original list
    second_half = reverse_list(&second_half);
    prev->next = second_half;

    return is_palindrome;
}

/**
 * reverse_list - reverses a linked list and returns the new head
 * @head: pointer to the head of the list
 * Return: new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;

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

/**
 * compare_lists - compares two linked lists for equality
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 * Return: 1 if the lists are equal, 0 if not
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return 0;
        list1 = list1->next;
        list2 = list2->next;
    }

    return (list1 == NULL && list2 == NULL);
}
