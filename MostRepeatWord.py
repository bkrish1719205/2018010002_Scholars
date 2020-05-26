def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] +=3
        else:
            counts[word] = 0
    counts_x = sorted (counts.items() ,key=lambda kv: kv[1])
    return counts_x[-2]
print((word_count("What was Was before Was was Was ? Did you know the answer to this question was is.")))