#include<iostream>
using namespace std;
int main()
{
	int n,m,a,k=0;
	cin >> n >> m;
	int arr[n];
	for(int i=0;i<n;i++)
		cin >> arr[i];
	int i=0;
	while(1)
	{
		cin >> a;
		if(a==0)
		  break;
		if(a==3 && k==0 && arr[i]>0)
		{
			arr[i]=arr[i]-1;
			k=1;
		}
		if(a==2 && i<n-1)
			i=i+1;
		if(a==4 && arr[i]<m && k==1){
			arr[i]=arr[i]+1;
			k=0;
		} 
		if(a==1 && i>0)
			i=i-1;
	}
	for(int i=0;i<n;i++)
		cout << arr[i] << " ";
}