#include<stdio.h>
int c=0;
void tower(int n,char from,char to,char aux){
	if(n==1){
		printf("\nMove disk 1 from %c to %c ",from,to);
		c++;
		return;
	}
	tower(n-1,from,aux,to);
	printf("\nMove disk %d from %c to %c ",n,from,to);
	c++;
	tower(n-1,aux,to,from);
}
int main(){
	int n=3;
	tower(n,'A','C','B');
	printf("\n%d",c);
}


// #include<stdio.h>
// #include<stdlib.h>
// #include<stdlib.h>
// int a[100],size,choice,x,top=-1;
// void push();
// void dis();
// void pop();
// int main(){
// 	printf("The stack operation:\n");
// 	printf("1.Push 2.Pop 3.Display 4.Exit\n\n");
// 	printf("Enter the size of the array: ");
// 	scanf("%d",&size);
// 	do{
// 		printf("\nEnter Your choice ");
// 		scanf("%d", &choice);
// 		switch(choice){
// 			case 1:
// 				push();
// 				break;
// 			case 2:
// 				pop();
// 				break;
// 			case 3:
// 				dis();
// 				break;
// 			case 4:
// 				exit(0);
// 				break;
// 			default:
// 				printf("\nPlease enter the correct choice");
// 				break;
// 		}
// 	}
// 	while(choice!=4);
// 	return 0;
// }
// void push(){
// 	if(top==size-1)
// 		printf("\nThe stack is overflow");
// 	else{
// 		printf("\nEnter the value ");
// 		scanf("%d",&x);
// 		top++;
// 		a[top]=x;
// 	}
// }
// void pop(){
// 	if(top<0)
// 		printf("\nThe stack in underflow");
// 	else{
// 		printf("\nThe deleted element is %d",a[top]);
// 		top--;
// 	}
// }
// void dis(){
// 	int i=0;
// 	if(top<0)
// 		printf("\nThe stack is empty");
// 	else{
// 		for( i = 0; i <= top; i++)
// 			printf("%d ",a[i]);		
// 	}
// }

// #include<stdio.h>
// #include<stdlib.h>
// #include<limits.h>
// struct StackNode
// {
// 	int data;
// 	struct StackNode* next;
// };
// struct StackNode* newNode(int data){
// 	struct StackNode* stackNode=(struct StackNode*)malloc(sizeof(struct StackNode));
// 	stackNode->data=data;
// 	stackNode->next=NULL;
// 	return stackNode;
// };
// int isEmpty(struct StackNode *root){
// 	return !root;
// }
// void push(struct StackNode** root, int data){
// 	struct StackNode* stackNode=newNode(data);
// 	stackNode->next=(*root);
// 	*root=stackNode;
// }
// void pop(struct StackNode** root){
// 	if(isEmpty(root))
// 		return INT_MIN;
// 	struct StackNode* temp=*root;
// 	*root=(*root)->next;
// 	int popped=temp->data;
// 	free(temp);
// }
