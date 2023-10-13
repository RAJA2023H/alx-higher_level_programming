#include <lists.h>
size_t print_dlistint(const dlistint_t *h)
	struct dlistint_s* head = NULL;
	struct dlistint_s* tail = NULL;
	struct  dlistint_s* current = head;
	int i = 0;

	while (current != NULL)
	{
		printf("%d -> ", current->n);
		current = current->next;
		i++;
	}
	return(i);
