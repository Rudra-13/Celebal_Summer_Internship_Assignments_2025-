
def count_num(s):
    if not s:
        return ""

    count = 1
    result = ""

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += f"({count}, {s[i - 1]}) "
            count = 1

    result += f"({count}, {s[-1]})"
    return result
#function count_num is called here 
if __name__ == "__main__":
    s = input()
    output = count_num(s)
    print(output)
