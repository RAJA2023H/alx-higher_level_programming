#include "lists.h"

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: A pointer to a pointer to the head of the linked list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head, *palindrome = *head;
    int length = 0, i = 0, j = 0;

    if (!*head)
        return (1);

    // Calculate the length of the linked list
    while (current)
    {
        current = current->next;
        length++;
    }

    current = *head;
    for (i = 1; i <= length; i++)
    {
        for (j = i; j <= length - i; j++)
            palindrome = palindrome->next;

        if (current->n != palindrome->n)
            return (0);

        current = current->next;
        palindrome = current;
    }

    return (1);
}
