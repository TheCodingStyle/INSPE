/*
** EPITECH PROJECT, 2023
** my_strlen()
** File description:
** Length of the string
*/

int my_strlen(char const *str)
{
    int i;

    for (i = 0; str[i] != '\0'; i++);
    return i;
}
