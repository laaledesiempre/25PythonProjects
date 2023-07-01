def binarySearch(element, list):
    start=0
    end=int(len(list)/2)
    i=0
    while True:
        i+=1
        if i>15:
            break
        print(start,end)
        print(list[start:end])
        if element==list[end]:
            print(f"index is {end}")
            break
        elif list[start:end+1][-1]<element:
            print("bigger")
            start=end
            end=int((end*2-1)-int(((end*2-1)-start)/2))+1
        else:
            end=int(end/2)+1


binarySearch(5,[0,1,2,3,4,5,6,7])