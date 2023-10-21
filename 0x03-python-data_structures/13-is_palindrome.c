#include "lists.h"

/**
 * is_palindrome - check if is palindrom
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *prem = *head, *deux = *head,
		  *prev = NULL, *current, *next, *first, *second;

	if (*head == NULL)
		return (1);
	for (; deux != NULL && deux->next != NULL;
			prem = prem->next, deux = deux->next->next);
	current = prem;
	for (; current != NULL;
			next = current->next, current->next = prev, prev = current, current = next);

	first = *head;
	second = prev;

	for (; first != NULL && second != NULL;
			first = first->next, second = second->next)
	{
		if (first->n != second->n)
			return (0);
	}
	return (1);
}
