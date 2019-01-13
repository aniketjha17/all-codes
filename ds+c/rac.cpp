// #include<iostream> 
// using namespace std; 
  
// // Returns count of all squares  
// // in a rectangle of size m x n 
// int countSquares(int m, int n) 
// { 
// // If n is smaller, swap m and n 
// if (n < m) 
//     swap(m, n); 
  
// // Now n is greater dimension,  
// // apply formula 
// return m * (m + 1) * (2 * m + 1) /  
//      6 + (n - m) * m *(m + 1) / 2; 
// } 
  
// // Driver Code 
// int main() 
// { 
// int m = 4, n = 3; 
// cout << "Count of squares is "
//      << countSquares(m, n); 
// } 

#include<bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	while(t--){
		string s;
		cin>>s;
		int hold = 1;
		string ans = "safe";
		vector<int> busy;
		//cout<<s.length();
		for(int i=0;i<s.length();++i){
			if(isdigit(s[i])){
				int low = (i) - (s[i] - '0');
				int high = (i) + (s[i] - '0');

				if(low<0) 
					low = 0;

				if(high>=s.length())
					high = s.length()-1;

				//cout<<low<<" "<<high<<endl;


				
				for(int j= i;j<=high;++j){
					busy.push_back(j);
				}

				for(int j= i+1;j<=high;++j){
					if(isdigit(s[j])){
						// cout<<s[j];
						ans = "unsafe";
						hold = 0;
						break;
					}
				}

				for(int j = i-1;j>=low;--j){
					if(find(busy.begin(), busy.end(),j)!=busy.end()){
						//cout<<j;
						ans = "unsafe";
						hold = 0;
						break;

					}
				}


				
			}

			if(hold==0)
				break;
				
		}
		// for(int i=0;i<busy.size();++i){
		// 	cout<<busy[i]<<" ";
		// }
		cout<<ans<<endl;
	}
}