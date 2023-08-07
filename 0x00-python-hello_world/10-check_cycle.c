#include "lists.h"

/**
 * check_cycle - checks if thers a cycle in list
 * @list: pointer to the list
 * Return: 0 if there is no cycle and
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	while (list && slow_ptr && slow_ptr->next)
	{
		list = list->next;
		slow_ptr = slow_ptr->next->next;

		if (list == slow_ptr)
		{
			list = fast_ptr;
			fast_ptr =  slow_ptr;
			while (1)
			{
				slow_ptr = fast_ptr;
				while (slow_ptr->next != list && slow_ptr->next != fast_ptr)
				{
					slow_ptr = slow_ptr->next;
				}
				if (slow_ptr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
