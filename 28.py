def strStr(haystack, needle):

    for i in range(len(haystack)):
        string=""
        for j in range(i,len(haystack)):
            string+=haystack[j]
            if string==needle:
                return i
    return -1