def isBalanced(s):
    OPENS = ["(", "[", "{"]
    CO_DICT = {")": "(", "]": "[", "}": "{"}

    st = []
    for c in s:
        if c in OPENS:
            st.append(c)
        else:
            if not st:
                return "NO"
            else:
                p = st.pop()
                if CO_DICT[c] != p:
                    return "NO"
    # Return
    if st:
        return "NO"
    return "YES"


# print(isBalanced("{(([])[])[][(])]}"))
# print(isBalanced("][[{)())))}[)}}}}[{){}()]([][]){{{{{[)}]]{([{)()][({}[){]({{"))
# print(isBalanced("{{}("))
# exit()

outputs = []
with open("/home/shane/Desktop/output04_balanced-brackets.txt") as f:
    for l in f:
        outputs.append(l.rstrip())

with open("/home/shane/Desktop/input04_balanced-brackets.txt") as f:

    for i, l in enumerate(f):
        if i == 0:
            continue
        l = l.rstrip()

        if isBalanced(l) != outputs[i - 1]:
            print(i)
