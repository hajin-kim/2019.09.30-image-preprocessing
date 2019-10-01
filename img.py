import numpy as np
import cv2
import matplotlib.pyplot as plt

target = str(input("Target image dir: "))

cap = cv2.imread(target, cv2.IMREAD_COLOR)

#
# print(type(cap))
# print(cap)
# print(type(cap[0][0]))
# print(type(cap[0][0][0]))
#
# a = input('Checkpoint . . .')

print("Getting img . . .")
sigma = 0
count = 0
for y in cap:
    for x in y:
        count += 1
        for RGB in x:
            sigma += RGB

print("Processing img . . .")
sigma //= count
new_cap = cap
for y in range(len(cap)):
    for x in range(len(cap[y])):
        RGB = int(cap[y][x][0]) + int(cap[y][x][1]) + int(cap[y][x][2])
        if RGB > sigma:
            new_cap[y][x][0] = np.uint8(255)
            new_cap[y][x][1] = np.uint8(255)
            new_cap[y][x][2] = np.uint8(255)
        else:
            new_cap[y][x][0] = np.uint8(0)
            new_cap[y][x][1] = np.uint8(0)
            new_cap[y][x][2] = np.uint8(0)
    if y % 20 == 19:
        print("  Line", y + 1, "processing complete.")


cv2.imwrite("result." + target.split('.')[-1], new_cap)

print("Done.")

plt.imshow(new_cap)
plt.show()

# plt.imshow(cap)
# plt.xticks([]) # hide x axis
# plt.yticks([]) # hide y axis
# plt.show()
