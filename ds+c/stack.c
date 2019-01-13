#include<stdio.h>
#include<stdlib.h>
int choice,top,i,size,stc[100],x;
void push();
void pop();
void dis();
int main(){
	printf("Stack Data-Structure\n");
	printf("1.Push  2.Pop  3.Display  4.Exit\n\n");
	printf("Enter the size of the stack ");
	scanf("%d",&size);
	top=-1;
	do{
		printf("Enter ur response ");
		scanf("%d",&choice);
		switch(choice){
			case 1:
				push();
				break;
			case 2:
				pop();
				break;
			case 3:
				dis();
				break;
			case 4:
				exit(0);
				break;
			default:
				printf("Please enter a valid input");
		}
	}
	while(choice!=4);
	return 0;
}
void push(){
	if(top==size-1)
		printf("The stack is  OVERFOLW\n");
	else{
		printf("Enter the value to be pushed ");
		scanf("%d",&x);	
		top++;
		stc[top]=x;
	}
}
void pop(){
	if(top<=-1)
		printf("Stack is underflow\n");
	else{
		printf("The poped element is %d\n",stc[top]);
		top--;	
	}
}
void dis(){
	int i;
	for(i=top;i>=0;i--)
		printf("%d\n",stc[i]);
}






/* que*/
#include <stdio.h>
#include<stdlib.h>
void insert();
void del();
void dis();
int que[100],choice,x,i,front=-1,rear=-1,size;
int main(){
	printf("que Data-Structure\n");
	printf("1.Insert  2.Delete  3.Display  4.Exit\n");
	printf("Enter the size of the que ");
	scanf("%d",&size);
	do{
		printf("\nEnter ur response ");
		scanf("%d",&choice);
		switch(choice){
			case 1:
				insert();
				break;
			case 2:
				del();
				break;
			case 3:
				dis();
				break;
			case 4:
				exit(0);
				break;
			default:
				printf("Please enter a valid input\n");
		}
	}
	while(choice!=4);
	return 0;
}
void insert(){
	if(rear==size-1)
		printf("No space\n");
	else{
		printf("Enter the element to be inserted ");
		scanf("%d",&x);
		rear++;
		que[rear]=x;
	}
}
void del(){
	if(front==rear)
		printf("Que is empty\n");
	else{
		front++;
		printf("The deleted element is %d\n",que[front]);
	}
}
void dis(){
	for(i=rear;i>front;i--)
		printf("%d ",que[i]);
}







/*cque*/
#include <stdio.h>
#include <stdlib.h>
#define SIZE 5
void enQueue(int);
void deQueue();
void display();
int cQueue[SIZE], front = -1, rear = -1;
void main(){
	int choice, value;
	printf("\n****** MENU ******\n");
	printf("1. Insert\n2. Delete\n3. Display\n4. Exit\n");
	while (1){
		printf("Enter your choice: ");
		scanf("%d", &choice);
		switch (choice){
		case 1:
			printf("\nEnter the value to be insert:  ");
			scanf("%d", &value);
			enQueue(value);
			break;
		case 2:
			deQueue();
			break;
		case 3:
			display();
			break;
		case 4:
			exit(0);
		default:
			printf("\nPlease select the correct choice!!!\n");
		}
	}
}
void enQueue(int value){
	if ((front == 0 && rear == SIZE - 1) || (front == rear + 1))
		printf("\nCircular Queue is Full! Insertion not possible!!!\n");
	else{
		if (rear == SIZE - 1 && front != 0)
			rear = -1;
		cQueue[++rear] = value;
		printf("\nInsertion Success!!!\n");
		
	}
}
void deQueue(){
	if (front == -1 && rear == -1)
		printf("\nCircular Queue is Empty! Deletion is not possible!!!\n");
	else{
		printf("\nDeleted element : %d\n", cQueue[front++]);
		if(front==rear)
			front=rear=-1;
		else if(front==SIZE-1)
			front=0;
	}
}
void display(){
	if (front == -1)
		printf("\nCircular Queue is Empty!!!\n");
	else{
		int i = front;
		printf("\nCircular Queue Elements are : \n");
		if (front <= rear)
			while (i <= rear)
				printf("%d\t", cQueue[i++]);
		else{
			while (i <= SIZE - 1)
				printf("%d\t", cQueue[i++]);
			i = 0;
			while (i <= rear)
				printf("%d\t", cQueue[i++]);
		}
	}
}