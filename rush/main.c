/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gcucino <gcucino@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/09/11 21:49:11 by dridolfo          #+#    #+#             */
/*   Updated: 2022/11/20 18:01:53 by gcucino          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

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

int	ft_check_int(const char *str, int i, int s)
{
	int	j;

	j = 0;
	while (str[i + j] != '\0' && (str[i + j] > 47 && str[i + j] < 58))
		j++;
	printf("%d\n", j);
	if (j > 10)
		return (-1);
	else if (j < 10)
		return (1);
	else
	{
		if (s == 1)
			return (ft_strncmp(&str[i], "2147483647", 10) <= 0);
		else
			return (ft_strncmp(&str[i], "2147483648", 10) <= 0);
	}
}

static int	ft_atoi(const char *str)
{
	int		i;
	int		r;
	int		s;

	i = 0;
	r = 0;
	s = 1;
	while (str[i] != '\0' && ((str[i] > 8 && 14 > str[i]) || str[i] == 32))
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			s *= -1;
		i++;
	}
	if (ft_check_int(str, i, s) == 0)
		return (-1);
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
	int	x;
	int	y;
	
	if (argc != 3)
		return(write(1, "Error: Wrong number of arguments\n", 34));
	x = ft_atoi(argv[1]);
	y = ft_atoi(argv[2]);
	printf("%d, %d\n", x, y);
	if (x < 0 || y < 0)
	{
		write(1, "Invalid arguments passed.\n", 27);
		return(-1);
	}
	// rush(x, y);
	return (0);
}
