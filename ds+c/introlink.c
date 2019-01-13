
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
	
	head->data=1;
	head->next=second;
	second->data=2;
	second->next=third;
	third->data=3;
	third->next=NULL;
	
	printList(head);
}
void printList(struct Node *n){
	while(n!=NULL){
		printf("%d ",n->data);
		n=n->next;
	}
}






//inserting a node in the front:-
#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node *next;
};
void printList();
void push();
int main(){
	struct Node* head;
	struct Node* second;
	struct Node* third;
	struct Node* forth;
	
	head=(struct Node*)malloc(sizeof(struct Node));
	second=(struct Node*)malloc(sizeof(struct Node));
	third=(struct Node*)malloc(sizeof(struct Node));
	
	head->data=45;
	head->next=second;
	second->data=85;
	second->next=third;
	third->data=65;
	third->next=NULL;
	printf("The orginal list is :");
	printList(head);
	printf("\n");
	push(&head,78);
	push(&head,100);
	printf("The list after push has been operated :");
	printList(head);
}
void push(struct Node** head_ref, int new_data)
{
   /* 1. allocate node */
   struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
   /* 2. put in the data  */
   new_node->data  = new_data;
   /* 3. Make next of new node as head */
   new_node->next = (*head_ref);
   /* 4. move the head to point to the new node */
   (*head_ref)  = new_node;
}
void printList(struct Node *n){
	while(n!=NULL){
		printf("%d ",n->data);
		n=n->next;
	}
}






/*inserting a node at the end*/
#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node *next;
};
void push();
void print();
int main(){
	struct Node* head;
	struct Node* second;
	head=(struct Node*)malloc(sizeof(struct Node));
	second=(struct Node*)malloc(sizeof(struct Node));
	head->data=78;
	head->next=second;
	second->data=100;
	second->next=NULL;
	print(head);
	printf("\n");
	push(&head,125);
	print(head);
}
void print(struct Node *n){
	while(n!=NULL){
		printf("%d ",n->data);
		n=n->next;
	}
}
void push(struct Node** head_ref, int new_data)
{
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    struct Node *last = *head_ref; 
    new_node->data  = new_data;
    new_node->next = NULL;
    if (*head_ref == NULL)
    {
       *head_ref = new_node;
       return;
    }
    while (last->next != NULL)
        last = last->next;
    last->next = new_node;
    return;
}





//insert after:-
#include<stdio.h>
#include<stdlib.h>
//insert node at particular posotion:-
struct Node{
	int data;
	struct Node *next;
};
void insertAfter();
void print();
int main(){
	struct Node* head=(struct Node*)malloc(sizeof(struct Node));
	struct Node* second=(struct Node*)malloc(sizeof(struct Node));
	struct Node* third=(struct Node*)malloc(sizeof(struct Node));
	head->data=745;
	head->next=second;
	second->data=547;
	second->next=third;
	third->data=985;
	third->next=NULL;
	print(head);
	printf("\n");
	insertAfter(head->next,254);
	print(head);
}
void insertAfter(struct Node* prev_ref,int value){
	struct Node* new_node=(struct Node*)malloc(sizeof(struct Node));
	new_node->data=value;
	new_node->next=prev_ref->next;
	prev_ref->next=new_node;
}
void print(struct Node *n){
	while(n!=NULL){
		printf("%d ",n->data);
		n=n->next;
	}
}






//delete node after:-
#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node *next;
};
void deleteNode();
void print();
int main(){
	struct Node* head=(struct Node*)malloc(sizeof(struct Node));
	struct Node* second=(struct Node*)malloc(sizeof(struct Node));
	struct Node* third=(struct Node*)malloc(sizeof(struct Node));
	struct Node* forth=(struct Node*)malloc(sizeof(struct Node));
	head->data=784;
	head->next=second;
	second->data=412;
	second->next=third;
	third->data=241;
	third->next=forth;
	forth->data=120;
	forth->next=NULL;
	printf("The original linked list\n");
	print(head);
	deleteNode(&head, 241);
	printf("\n");
	print(head);
}
void print(struct Node *n){
	while(n!=NULL){
		printf("%d ",n->data);
		n=n->next;
	}
}
void deleteNode(struct Node **head_ref, int key)
{
    struct Node* temp = *head_ref, *prev;
    if (temp != NULL && temp->data == key)
    {
        *head_ref = temp->next;  
        free(temp);              
        return;
    }
    while (temp != NULL && temp->data != key)
    {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) 
		return;
    prev->next = temp->next;
    free(temp); 
}



