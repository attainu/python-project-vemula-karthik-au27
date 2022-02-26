#Core CSE:
from doctest import Example


Q1. List out different OOPS principles and explain?
Ans:  There are four types of  major principles that take an object 
      they are Encapsulation, Data Abstraction, Polymorphism and Inheritance

      Encapsulation:
            Encapsulation is the mechanism of hiding of data implementation by restricting access to
        public methods. Instance variables are kept private and accessor methods are made publi
        -c to achieve this
       FOR EX:For example, we are hiding the name and dob attributes of person class in the below co
       -de snippet.

       Data Abstraction:
            Abstract means a concept or an Idea which is not associated with any particular instance.
        Using abstract class/Interface we express the intent of the class rather than the actual imp
        -lementation. In a way, one class should not know the inner details of another in order to use
         it, just knowing the interfaces should be good enough.

        Inheritance:
             Inheritances expresses “is-a” and/or “has-a” relationship between two objects. Using Inh
        -eritance, In derived classes we can reuse the code of existing super classes. In Java, concept
         of “is-a” is based on class inheritance (using extends) or interface implementation (using imple
         -ments).

        Polymorphism:
              It means one name many forms. It is further of two types — static and dynamic. Static
         polymorphism is achieved using method overloading and dynamic polymorphism using method ov
         -erriding. It is closely related to inheritance. We can write a code that works on the sup
         -erclass, and it will work with any subclass type as well.
                
        
Q2. List out Layers of TCP/IP Model and explain?
Ans: TCP/IP MODEL:
   * TCP refers to Transmission Control Protocol.
   * TCP/IP has 4 layers.
   * TCP/IP is more reliable
   * TCP/IP does not have very strict boundaries.
   * TCP/IP follow a horizontal approach.
   * TCP/IP uses both session and presentation layer in the application layer itself.
   * TCP/IP developed protocols then model.
   * Transport layer in TCP/IP does not provide assurance delivery of packets.
   * TCP/IP model network layer only provides connection less services.
   * Protocols cannot be replaced easily in TCP/IP model.

Q3. Construct a binary tree by using postorder and inorder sequences given below.
Inorder: N, M, P, O, Q
Postorder: N, P, Q, O, M.
Ans: A binary tree is a data structure in which every node or vertex has atmost two children. In Pyt
-hon, a binary tree can be represented in different ways with different data structures(dictionary,
 list) and class representation for a node. However, binarytree library helps to directly implement 
 a binary tree. It also supports heap and binary search tree(BST). This module does not come pre-ins
 -talled with Python’s standard utility module. To install it type the below command in the terminal.

  Inorder:
      1. Traverse the left subtree, i.e., call Inorder(left-subtree)
      2. Visit the root.
      3. Traverse the right subtree, i.e., call Inorder(right-subtree)

  Postorder:
      1. Visit the root.
      2. Traverse the left subtree, i.e., call Preorder(left-subtree)
      3. Traverse the right subtree, i.e., call Preorder(right-subtree)

Q4. Explain LRU cache and its implementation by taking some examples and explaining all steps.
Ans: We are given total possible page numbers that can be referred. We are also given cache (or mem
    -ory) size (Number of page frames that cache can hold at a time). The LRU caching scheme is to r
    -emove the least recently used frame when the cache is full and a new page is referenced which 
    is not there in cache. 

    We use two data structures to implement an LRU Cache. 
    
    1.Queue which is implemented using a doubly linked list. The maximum size of the queue will be e
    -qual to the total number of frames available (cache size). The most recently used pages will be
     near front end and least recently pages will be near the rear end.

    2.A Hash with page number as key and address of the corresponding queue node as value.
     
     Example:
        – Consider the following reference string :  
           1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

Q5. Explain virtual memory.
Ans:   Virtual memory is a feature of an operating system that enables a computer to be able to comp
 -ensate shortages of physical memory by transferring pages of data from random access memory to di
 -sk storage. ... This process allows for RAM to be freed up so that a computer can complete the ta
 -sk.
Q6. Explain Deadlock and its characteristics.
Ans:  A deadlock is a situation in which two processes sharing the same set of resources are effecti
 -vely preventing each other from accessing the resource, resulting in both programs ceasing to func
 -tion. ... Thus, in deadlock, processes never finish executing and system resources are tied up, pr
 -eventing other jobs from starting.

Q8. Explain NAT and ARP protocol?
Ans: In the case of such pool addresses, the outside gateway interface and the access router's insid
-e interface share the same broadcast domain, ARP is used, and the NAT gateway is required to reply 
on behalf of the static address pool. ... Most of the time, the firewall/NAT software takes care of 
this by itself, though.