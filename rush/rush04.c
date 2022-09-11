/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush04.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dridolfo <dridolfo@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/09/11 23:00:25 by dridolfo          #+#    #+#             */
/*   Updated: 2022/09/11 23:02:21 by dridolfo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

void	rush_(int *coord, char *el);
void	writer(int i, int j, int *coord, char *el);

int	rush(int x, int y)
{
	char	*el;
	int		*coord;

	if (x < 0 || y < 0)
		return (write(1, "Invalid arguments passed.\n", 27));
	el = malloc(6);
	coord = malloc(sizeof(int) * 2);
	el = malloc(6);
	coord = malloc(sizeof(int) * 2);
	el[0] = 'A';
	el[1] = 'C';
	el[2] = 'A';
	el[3] = 'C';
	el[4] = 'B';
	el[5] = 'B';
	coord[0] = x;
	coord[1] = y;
	rush_(coord, el);
	free(el);
	free(coord);
	return (0);
}
