def search(lst,ele):
  l=0
  h=len(lst)-1
  while(l<h):
    mid = (l+h)//2
    if lst[mid] == ele:
      return mid
    elif lst[mid]<ele:
      l = mid+1
    else:
      h = mid-1
  return -1

lst = [2,5,9,4,8,6]
lst.sort()  
ele_to_search = 5
ans = search(lst,ele_to_search)
print(ans)
