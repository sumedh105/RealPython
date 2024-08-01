no_of_cats = 100

cat_dict = {}
for i in range(1, 101):
    if i == 1:
        for j in range(1, 101):
            cat_dict[j] = 1

    else:
        for j in range(1, 101):
            mod = j%i
            if mod == 0:
                if cat_dict[j] == 1:
                    cat_dict[j] = 0
                else:
                    cat_dict[j] = 1
    #print(cat_dict)

for i in range(1, 101):
    if cat_dict[i] == 1:
        print(f"i = {i} and cat_dict[i] = {cat_dict[i]}")

