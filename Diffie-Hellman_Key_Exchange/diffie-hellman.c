#include<stdio.h>

// Algorithm is used to calculate the key
long int key(int a,int b,int mod)
 {
  long int t;
  if(b==1)
  return a;
  t=key(a,b/2,mod);
  if(b%2==0)
   return (t*t)%mod;
  else
   return (((t*t)%mod)*a)%mod;
 }

 int main()
 {
 	
  int n,g,x,y,alice,bob;
  
  // Alice and Bob will both agree on the values of variables n and g
  printf("Enter the value of public variable n: ");
  scanf("%d",&n);
  printf("Enter the value of public variable g: ");
  scanf("%d",&g);
  
  // Alice inputs value for private variable x
  printf("Enter the value of private variable x for Alice: ");
  scanf("%d",&x);  alice=key(g,x,n);
  // Bob inputs value for private variable y
  printf("Enter the value of private variable y for Bob: ");
  scanf("%d",&y);  bob=key(g,y,n);
  
  // If this was successful, two matching numbers will be displayed
  printf("Key for Alice is : %ld\n",key(bob,x,n));
  printf("Key for Bob is : %ld\n",key(alice,y,n));
 }
