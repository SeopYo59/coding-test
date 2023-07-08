#include <stdio.h>

void Moo(int n, int k, int mooLength)
{
	int centerLength = k + 3;
	int firstSideLength = (mooLength - centerLength) / 2;
	int	secondSideLength = (mooLength - centerLength) / 2;

	if(n <= firstSideLength) //첫번째 사이드에 있습니까?
	{ 
		Moo(n, k-1, mooLength - (centerLength + secondSideLength));
		return;
	} 
	
	else if(n <= (firstSideLength + centerLength)) //센터에 있습니까? 
	{
		if(n == firstSideLength + 1) //첫글자가 m입니까? 
		{
			printf("m");
			return;
		}
		else
		{
			printf("o");
			return;
		}
	}
	
	else if(n <= mooLength) //두번째 사이드에 있습니까?
	{ 
		Moo(n - (firstSideLength + centerLength), k-1, mooLength - (firstSideLength + centerLength));
		return;
	}
		
	return;
}


int main(void)
{
	int n = 0;
	scanf("%d", &n);
	
	int mooLength = 3;  //S(k) = "moo"
	int k = 0; 
	while(mooLength < n) //n번째 글자를 구하기 위한 최소 수열 길이를 구한다. 
	{
		k++; 
		mooLength = (mooLength*2) + (k+3);
	}
	
	Moo(n, k, mooLength);
	
	return 0;
}