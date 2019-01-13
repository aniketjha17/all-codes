// bubble short:-
// #include <stdio.h>
// int main()
// {
//   int array[100], n, c, d, swap;
//   printf("Enter number of elements\n");
//   scanf("%d", &n);
//   printf("Enter %d integers\n", n);
//   for (c = 0; c < n; c++)
//     scanf("%d", &array[c]);
//   for (c = 0 ; c < n - 1; c++)
//   {
//     for (d = 0 ; d < n - c - 1; d++)
//     {
//       if (array[d] > array[d+1]) 
//       {
//         swap       = array[d];
//         array[d]   = array[d+1];
//         array[d+1] = swap;
//       }
//     }
//   }
//   printf("Sorted list in ascending order:\n");
//   for (c = 0; c < n; c++)
//      printf("%d\n", array[c]);
//   return 0;
// }





// selcetion sort:-
// #include <stdio.h> 
// int main()
// {
//   int array[100], n, c, d, position, swap;
//   printf("Enter number of elements\n");
//   scanf("%d", &n);
//   printf("Enter %d integers\n", n);
//   for (c = 0; c < n; c++)
//     scanf("%d", &array[c]);
//   for (c = 0; c < (n - 1); c++)
//   {
//     position = c;
//     for (d = c + 1; d < n; d++)
//     {
//       if (array[position] > array[d])
//         position = d;
//     }
//     if (position != c)
//     {
//       swap = array[c];
//       array[c] = array[position];
//       array[position] = swap;
//     }
//   }
//   printf("Sorted list in ascending order:\n");
//   for (c = 0; c < n; c++)
//     printf("%d\n", array[c]);
//   return 0;
// }




// insertion sort:-
// #include <stdio.h>
// int main()
// {
//   int n, array[1000], c, d, t;
//   printf("Enter number of elements\n");
//   scanf("%d", &n);
//   printf("Enter %d integers\n", n);
//   for (c = 0; c < n; c++)
//     scanf("%d", &array[c]);
//   for (c = 1 ; c < n; c++) {
//     d = c;
//     while ( d > 0 && array[d-1] > array[d]) {
//       t          = array[d];
//       array[d]   = array[d-1];
//       array[d-1] = t;
//       d--;
//     }
//   }
//   printf("Sorted list in ascending order:\n");
//   for (c = 0; c <= n - 1; c++) {
//     printf("%d\n", array[c]);
//   } 
//   return 0;
// }




// quick sort:-
// #include<stdio.h>
// void quicksort(int number[25],int first,int last){
//    int i, j, pivot, temp;
//    if(first<last){
//       pivot=first;
//       i=first;
//       j=last;
//       while(i<j){
//          while(number[i]<=number[pivot]&&i<last)
//             i++;
//          while(number[j]>number[pivot])
//             j--;
//          if(i<j){
//             temp=number[i];
//             number[i]=number[j];
//             number[j]=temp;
//          }
//       }
//       temp=number[pivot];
//       number[pivot]=number[j];
//       number[j]=temp;
//       quicksort(number,first,j-1);
//       quicksort(number,j+1,last);
//    }
// }
// int main(){
//    int i, count, number[25];
//    printf("How many elements are u going to enter?: ");
//    scanf("%d",&count);
//    printf("Enter %d elements: ", count);
//    for(i=0;i<count;i++)
//       scanf("%d",&number[i]);
//    quicksort(number,0,count-1);
//    printf("Order of Sorted elements: ");
//    for(i=0;i<count;i++)
//       printf(" %d",number[i]);
//    return 0;
// }





// merge sort:-
// #include <stdio.h>
// #define max 10
// int a[11] = { 10, 14, 19, 26, 27, 31, 33, 35, 42, 44, 0 };
// int b[10];
// void merging(int low, int mid, int high) {
//    int l1, l2, i;
//    for(l1 = low, l2 = mid + 1, i = low; l1 <= mid && l2 <= high; i++) {
//       if(a[l1] <= a[l2])
//          b[i] = a[l1++];
//       else
//          b[i] = a[l2++];
//    }
//    while(l1 <= mid)    
//       b[i++] = a[l1++];
//    while(l2 <= high)   
//       b[i++] = a[l2++];
//    for(i = low; i <= high; i++)
//       a[i] = b[i];
// }
// void sort(int low, int high) {
//    int mid;
//    if(low < high) {
//       mid = (low + high) / 2;
//       sort(low, mid);
//       sort(mid+1, high);
//       merging(low, mid, high);
//    } else { 
//       return;
//    }   
// }
// int main() { 
//    int i;
//    printf("List before sorting\n");
//    for(i = 0; i <= max; i++)
//       printf("%d ", a[i]);
//    sort(0, max);
//    printf("\nList after sorting\n");
//    for(i = 0; i <= max; i++)
//       printf("%d ", a[i]);
// }






// //binary search:-
// #include<stdio.h>
// int main()
// {
//    int c, first, last, middle, n, search, array[100];
//    printf("Enter number of elements\n");
//    scanf("%d",&n);
//    printf("Enter %d integers\n", n);
//    for (c = 0; c < n; c++)
//       scanf("%d",&array[c]);
//    printf("Enter value to find\n");
//    scanf("%d", &search);
//    first = 0;
//    last = n - 1;
//    middle = (first+last)/2;
//    while (first <= last) {
//       if (array[middle] < search)
//          first = middle + 1;    
//       else if (array[middle] == search) {
//          printf("%d found at location %d.\n", search, middle+1);
//          break;
//       }
//       else
//          last = middle - 1;
//       middle = (first + last)/2;
//    }
//    if (first > last)
//       printf("Not found! %d isn't present in the list.\n", search);
//    return 0;  
// }
