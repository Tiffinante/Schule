import random
import math

len_of_tuple = 20
temp = []

for i in range(len_of_tuple):
    temp.append(random.randint(0, 100))

# print tuple data
my_tuple = tuple(temp)
print(my_tuple)
print(type(my_tuple))

# sort tuple
my_tuple_sort = tuple(sorted(my_tuple))
print(my_tuple_sort)

# stats
print("\nMittelwert:")
mittelwert = sum(my_tuple_sort) / len_of_tuple
print(mittelwert)

print("\nMedian:")
if len_of_tuple % 2 == 0:
    m1 = my_tuple_sort[len_of_tuple // 2]
    m2 = my_tuple_sort[len_of_tuple // 2 - 1]
    median = (m1 + m2)/2
else:
    median = my_tuple_sort[len_of_tuple // 2]
print(median)

print("\nStandardabweichung:")
v = 0
for n in my_tuple_sort:
    v += (n - mittelwert)**2
stdv = math.sqrt(v / (len_of_tuple - 1))
# stdv = math.sqrt(sum([(x - mittelwert)**2 for x in my_tuple_sort]) / (len_of_tuple-1))
print(stdv)
mxdzn = 0
print("\nMaximale Distanz zwischen Nachbarwerten:")
for i in range(len_of_tuple - 1):
    diff = my_tuple_sort[i + 1] - my_tuple_sort[i]
    if diff > mxdzn:
        mxdzn = diff
print(mxdzn)

print("\nMinimale Distanz zwischen Nachbarwerten:")
mndzn = 2**128
for i in range(len_of_tuple - 1):
    diff = my_tuple_sort[i + 1] - my_tuple_sort[i]
    if diff < mxdzn:
        mndzn = diff
print(mndzn)

print("\n\nMxDzN -> Maximale Distanz zwischen Nachbarwerten")
print("MnDzN -> Minimale Distanz zwischen Nachbarwerten\n")

header = "{:<8}  {:<12}  {:<8}  {:<20}  {:<7}  {:<7}".format("", "Mittelwert", "Median", "Standardabweichung", "MxDzN",
                                                             "MnDzN", )
text_my_tuple = "{:<8}  {:<12}  {:<8}  {:<20}  {:<7}  {:<7}".format("my_tuple", mittelwert, median, stdv, mxdzn,
                                                                    mndzn, )
print(header)
print(text_my_tuple)
