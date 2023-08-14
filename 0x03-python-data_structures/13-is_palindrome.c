#include "lists.h"

listint_t *_reverselistint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * _reverselistint - Helps reverse a singly-linked listint_t list.
 * @head: pointer to the starting node of the list.
 *
 * Return: pointer to the head of the reversed list.
 */
listint_t *_reverselistint(listint_t **head)
{
	listint_t *curr = *head, *next, *prev = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr, *rev, *mid;
	size_t list_size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	curr = *head;
	while (curr)
	{
		list_size++;
		curr = curr->next;
	}

	curr = *head;
	for (i = 0; i < (list_size / 2) - 1; i++)
		curr = curr->next;

	if ((list_size % 2) == 0 && curr->n != curr->next->n)
		return (0);

	curr = curr->next->next;
	rev = _reverselistint(&curr);
	mid = rev;

	curr = *head;
	while (rev)
	{
		if (curr->n != rev->n)
			return (0);
		curr = curr->next;
		rev = rev->next;
	}
	_reverselistint(&mid);

	return (1);
}
