#infosys infytq question
#input:accept a string of stars(*) and bars(|). then take start index and end index.
#output:number of stars enclosed in between any two bars within the start index and end index
def countstar(strg,start_index,stop_index):
    n=len(start_index)
    result=[]
    for i in range(n):
        substr=strg[start_index[i]:stop_index[i]+1]
        start=0
        stop=len(substr)-1
        print(substr)
        while 1:
            print(start)
            print(stop)
            if start>=stop:
                result.append(0)
                break
            if substr[start]=='|' and substr[stop]=='|':
                substr=substr[start:stop]
                result.append(substr.count('*'))
                break
            if substr[start]!='|':
                start=start+1
            if substr[stop]!='|':
                stop=stop-1
    return result
if __name__=='__main__':
    start_index=[]
    stop_index=[]
    strg=input("enter string ")
    n=int(input("enter no of substrings "))
    print("enter start and stop indices")
    for i in range(n):
        start_index.append(int(input()))
        stop_index.append(int(input()))
    print(start_index)
    print(stop_index)
    result=countstar(strg,start_index,stop_index)
    for i in range(n):
        print(f'{strg[start_index[i]:stop_index[i]+1]}->{result[i]}')
