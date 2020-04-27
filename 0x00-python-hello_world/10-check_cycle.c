#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - frees a listint_t list
  * @list: pointer for checking if the list has a cycle
  * Return: 1 if list has a cycle or 0 if not
  */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	while (turtle != NULL)
	{
		turtle = turtle->next;
		hare = hare->next;
		if (hare == NULL || hare->next == NULL)
			break;
		hare = hare->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
