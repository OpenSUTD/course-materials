from drawtree3 import draw_level_order
import math

"""
Note: It helps to have arrtree3.py and drawtree3.py along with your test code in the 
same working directory to ensure that the imports go smoothly.

Brief overview regarding the simple tree class:
    2 attributes:
        arr: the array
        
        n: the size of the heap
        
    6 Methods:
        swap: swaps two elements of the heap
        
        swapv: Does whatever swap does, but also shows a visualisation of the tree
         
        vistree: visualises a heap using an array as an argument
        
        vistree2: visualises a heap using a simple tree object as an argument
        
        decreasecount: decreases the heapsize (VERY IMPORTANT FUNCTION!)
        
        printtail: prints out the elements of the array NOT inside the heap
        
    Note that heap != array, hence the need for the
    heapsize attribute. Heap-based functions will have
    to rely on the heapsize to work properly. 
"""

class treesimple():
  def __init__(self,unsorted):
    self.arr = unsorted  #list of integers as input
    self.n = len(self.arr)

  def decreasecount(self):
    self.n-=1

  def printtail(self):
    for i in range(len(self.arr)-self.n):
      print ('tail at i=',self.arr[self.n+i])

  def swap(self,i,k):
    if  ( i < self.n ) and ( k < self.n ):
      z=self.arr[i]
      self.arr[i]=self.arr[k]
      self.arr[k]=z
    else:
      if i >= self.n:
        print ('ERROR: i >= self.n', i ,self.n)
      if k >= self.n:
        print ('ERROR: k >= self.n', k ,self.n)

  def swapv(self,i,k):
    self.swap(i,k)
    vistree2(self)


def vistree2(treesimple):
  n = treesimple.n
  if(n<1):
      print("There is no heap")
      return 
  printstr='{'

  for i in range(n-1):
    if(int(treesimple.arr[i])>=0):
      printstr+=str(treesimple.arr[i])+','
    else:
      printstr+='#'+','
  if(int(treesimple.arr[n-1])>=0):
    printstr+=str(treesimple.arr[n-1])
  else:
    printstr+='#'
  printstr+='}'


  draw_level_order(printstr)


def vistree(heaparray):

  n=len(heaparray)
  printstr='{'

  for i in range(n-1):
    if(int(heaparray[i])>=0):
      printstr+=str(heaparray[i])+','
    else:
      printstr+='#'+','
  if(int(heaparray[n-1])>=0):
    printstr+=str(heaparray[n-1])
  else:
    printstr+='#'
  printstr+='}'


  draw_level_order(printstr)


def swap(heaparray,i,k):
  if  ( i < len(heaparray) ) and ( k < len(heaparray) ):
    z=heaparray[i]
    heaparray[i]=heaparray[k]
    heaparray[k]=z
  else:
    if i >= len(heaparray):
      print ('ERROR: i >= len(heaparray)', i ,len(heaparray))
    if k >= len(heaparray):
      print ('ERROR: k >= len(heaparray)', k ,len(heaparray))

  return heaparray

def swapv(heaparray,i,k):
  swap(heaparray,i,k)
  vistree(heaparray)
  
"""
Try to take advantage of the simpletree class.
Note which functions use simpletree objects as an argument.
Please implement all these functions below.
"""

#Task 2 methods
def max_heapify(simpleTree,i):
  #Think abou how tree nodes are arranged in an array and how child nodes are referenced.
  #You can visualise it as a trickle down effect
  vistree2(simpleTree)

  """
  Hints for build max heap: 
  From what node index to start? try ceil log_2(n)
  Any class member x must be accessed by the self-preﬁx self.x.
  x=1 sets a local variable, not a class member, 
  hence max heapify should run for nodes 0 to self.n ,not for the whole array.
  """
  heapSize = simpleTree.n

  # Indexes of the left and right children.
  l = 2*i+1
  r = 2*i+2

  A = simpleTree.arr

  largest = i

  #check left
  if (l < heapSize and A[l] > A[i]):
    largest = l

  if (r < heapSize and A[r] > A[largest]):
    largest = r

  if (largest != i):
    swapv(A,i,largest)
    max_heapify(simpleTree, largest)



def build_max_heap(unsorted_tree):
  
  unsorted_tree.n = len(unsorted_tree.arr)
  heapSize = unsorted_tree.n
  for i in range(int(heapSize/2)-1,-1,-1):
    max_heapify(unsorted_tree,i)
  vistree2(unsorted_tree)


  

#Task 4 methods
def extract_max(tree,i):
  #You shoul make sure that the heap is converted into a max heap the first time you use this method.
  #Note that if you call build_max_heap here, you'll end up 
  #converting the entire array into a heap, so you'll be back to square one
  max_val = 0
  #Make sure to decrease the heap size
  #What happens if the heapsize is 0?
  vistree(tree)
  return max_val

def heapsort(unsorted_tree):
  #Make sure you decrement the heap-size at the appropriate moments
  pass
  #implement it yourself



