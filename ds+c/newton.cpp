#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node *next;
};
void printList();
int main(){
	struct Node* head;
	struct Node* second;
	struct Node* third;
	
	head=(struct Node*)malloc(sizeof(struct Node));
	second=(struct Node*)malloc(sizeof(struct Node));
	third=(struct Node*)malloc(sizeof(struct Node));
	
	head->data=14;
	head->next=second;
	second->data=45;
	second->next=third;
	third->data=78;
	third->next=NULL;
	
	printList(head);
}
void printList(struct Node n){
	while(n!=NULL){
		printf("%d",n->data);
		n=n->next
	}
}
