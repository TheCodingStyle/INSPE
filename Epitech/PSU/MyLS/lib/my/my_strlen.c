/*
** EPITECH PROJECT, 2023
** do-op()
** File description:
** Makes Operation
*/

int my_strlen(char const *str)
{
    int i;

    for (i = 0; str[i] != '\0'; i++);
    return i;
}
