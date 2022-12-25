def main(s):
    """
    A str of several words is given. All letters are lowercase. Make sure that the first letter of each word is capitalized.
    Args:
        s: str
    Returns:
        str: answer
    """
    y=0
    l=0
    while len(s)>l:
        if s[l].isdigit():
            y+=1
        l+=1
        

    
    return y
print(main("python 2022"))
