dog_cal = 120
bun_cal = 40
ketchup_cal = 37
mustard_cal = 20
onion_cal = 22
print("\tСосиска \tБулочка \tКетчуп \tГорчица \tЛук \tКалории")
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    total_cal = (dog_cal * dog) + (bun_cal * bun) + (ketchup_cal * ketchup) \
                    + (mustard_cal * mustard) + (onion_cal * onion)
                    print("#", count, "\t", end=" ")
                    print(dog, "\t", bun, "\t", ketchup, "\t", end=" ")
                    print(mustard, "\t", onion, end=" ")
                    print("\t", total_cal)
                    count = count + 1
