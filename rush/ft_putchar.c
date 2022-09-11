/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dridolfo <dridolfo@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/09/11 17:14:07 by dridolfo          #+#    #+#             */
/*   Updated: 2022/09/11 22:38:25 by dridolfo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

int	ft_putchar(int c)
{
	return (write(1, &c, 1));
}

void	writer(int i, int j, int *coord, char *el)
{
	if (i == 0 && j == 0)
		write(1, &el[0], 1);
	else if (i == 0 && j == (coord[0] - 1))
		write(1, &el[1], 1);
	else if (i == (coord[1] - 1) && j == 0)
		write(1, &el[2], 1);
	else if (i == (coord[1] - 1) && j == (coord[0] - 1))
		write(1, &el[3], 1);
	else if (i == 0 || i == (coord[1] - 1))
		write(1, &el[4], 1);
	else if (j == 0 || j == (coord[0] - 1))
		ft_putchar(el[5]);
	else
		write(1, " ", 1);
}

void	rush_(int *coord, char *el)
{
	int	i;
	int	j;
	int	x;
	int	y;

	i = 0;
	x = coord[0];
	y = coord[1];
	while (i < y)
	{
		j = 0;
		while (j < x)
			writer(i, j++, coord, el);
		write(1, "\n", 1);
		i++;
	}
}
