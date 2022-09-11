/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dridolfo <dridolfo@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/09/11 21:49:11 by dridolfo          #+#    #+#             */
/*   Updated: 2022/09/11 22:38:45 by dridolfo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

int	rush(int x, int y);

static int	ft_strncmp(const char *s1, const char *s2, unsigned int n)
{
	unsigned int	i;

	i = 0;
	if (n == 0)
		return (0);
	else
	{
		while (s1[i] == s2[i] && i < n - 1)
		{
			if (s1[i] == '\0' || s2[i] == '\0')
				break ;
			i++;
		}
	}
	return ((unsigned char)(s1[i]) - (unsigned char)(s2[i]));
}

static int	ft_atoi(const char *str)
{
	int		i;
	int		r;
	int		s;

	i = 0;
	r = 0;
	s = 1;
	if (ft_strncmp("-2147483648", str, 12) == 0)
		return (-2147483648);
	while (str[i] != '\0' && ((str[i] > 8 && 14 > str[i]) || str[i] == 32))
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			s *= -1;
		i++;
	}
	while (str[i] != '\0' && (str[i] > 47 && str[i] < 58))
	{
		r *= 10;
		r += (str[i] - 48);
		i++;
	}
	return (r * s);
}

int	main(int argc, char **argv)
{
	if (argc != 3)
		write(1, "Error: Wrong number of arguments\n", 34);
	rush(ft_atoi(argv[1]), ft_atoi(argv[2]));
	return (0);
}
