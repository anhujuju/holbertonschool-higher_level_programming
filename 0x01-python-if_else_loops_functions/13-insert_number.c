#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert new node to a list
 * @head: pointer to list head
 * @number: to be inserted
 * Return: address of the new node, or NULl if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (head == NULL)
		return (NULL);

	if (*head == NULL || current->n > number)
	{
		new->n = number;
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->next != NULL)
	{
		if (current->next->n > number)
		{
			temp = current->next;
			current->next = new;
			new->n = number;
			new->next = temp;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	new->n = number;
	new->next = NULL;
	return (new);
}
