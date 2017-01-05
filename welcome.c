/*
 * welcome.c
 * 
 * Copyright 2016 Chandra <chandra@SriMaa>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */
// This is test file updated locally... version 1 /5th Jan time: 15.52

#include <stdio.h>
#include <assert.h>

int main(int argc, char **argv)
{
	int abc [] = {0,1,4};
	int *copy = abc;
	
	copy[0] = 3;
	
	assert(abc[0]==3);
	printf("Assert pass\n");
	printf("%d ",copy[2]);
	
}

	


