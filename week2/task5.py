def merge_the_tools(string, k):
    # your code goes here
  for i in range(0, len(string), k): #code to prit substrings 
        substring = string[i:i+k]
        line = set()#helps in removing the duplicateg 
        result = ''
        for char in substring:#loop for each char in substring
            if char not in line:
                line.add(char)#adds char to the seen line set 
                result =result + char #result added to the new unique char 
        print(result)

    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)