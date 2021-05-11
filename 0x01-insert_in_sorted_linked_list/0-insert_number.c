#include "lists.h"
/**
 * add_nodeint - adds a new node at the beginning of a listint_t list.
 * @n: nodes
 * @head: first node
 * Return: New node.
 */
listint_t *insert_node(listint_t **head, int number);
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	if (new)
	{
		new->number = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	free(new);
	return (NULL);
}
