#include "lists.h"

/**
 * checking - palindrome validation function
 * @head: ptr to list's head.
 * @last_val: ptr to the end of the list
 * Return: 1 if palindrome, 0 if not.
 */
int checking(listint_t **head, listint_t *last_val)
{
	if (last_val == NULL)
		return (1);
	if (checking(head, last_val->next) && (*head)->n == last_val->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}


/**
 * is_palindrome - checks if a list is pallindrome.
 * @head: ptr to list's head.
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (checking(head, *head));
}
