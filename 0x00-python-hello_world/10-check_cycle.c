#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Check if there is a cycle in a linked list.
 * @list: Pointer to the head of the linked list.
 * Return: 1 if a cycle is detected, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
    listint_t *slow_ptr;
    listint_t *fast_ptr;

    slow_ptr = list;
    fast_ptr = list;

    if (list == NULL || list->next == NULL) {
        return (0);
    }

    while (fast_ptr != NULL && fast_ptr->next != NULL) {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;

        if (slow_ptr == fast_ptr) {
            return (1);
        }
    }

    return (0);
}
