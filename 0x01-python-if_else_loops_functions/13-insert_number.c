#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts number in a sorted linked list
 * @head: Pointer to pointer to the  head of listint_t
 * @number: Integer to be input
 * Return: Pointer to the head of listint
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *prev = *head;
	listint_t *next_node;

	next_node = (listint_t*)malloc(sizeof(listint_t));

	if (next_node == NULL)
		return (NULL);
	next_node->n = number;
	next_node->next = NULL;

	if (*head == NULL)
	{
		*head = next_node;
		(*head)->next = NULL;
		return (next_node);
	}
	while (curr->next != NULL)
	{
		if (curr->n > number)
		{
			if (prev == *head)
			{
				*head = next_node;
				next_node->next = curr;
				return (next_node);
			}
			prev->next = next_node;
			next_node->next = curr;
			return (next_node);
		}
		prev = curr;
		curr = curr->next;
	}
	if (curr->next == NULL){
		curr->next = next_node;
		next_node->next = NULL;
	}
	return (NULL);
}
