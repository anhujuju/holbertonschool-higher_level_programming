#include "lists.h"

/**
 * check_cycle - Checks if the single linkedlist contains a loop.
 *
 * @list: Pointer to the head of the list.
 *
 * Return: 0 if there is no loop. Otherwise 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}