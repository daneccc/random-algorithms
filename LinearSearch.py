def search(lst,ele)
  n=len(lst)
  for i in range(n):
    if ele == lst[i]:
      return i
  return -1
    
lst = [2,5,9,4,8,6]
ele_to_search = 5
ans = search(lst,ele_to_search)
print(ans)
