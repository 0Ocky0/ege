def dist(p1, p2):
    return max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))


def centr(cluster):
    minim = 10 ** 40
    funal_centroid = []
    for centroid in cluster:
        sum_dist = 0
        for point in cluster:
            sum_dist += dist(centroid, point)
        if sum_dist < minim:
            minim = sum_dist
            final_centroid = centroid
    return final_centroid

f = open('27A.txt')
k1, k2, k3 = [], [], []
for line in f:
    x, y = map(float, line.split(';'))
    if y < 5:
        k1.append([x, y])
    elif y < 6:
        k2.append([x, y])
    elif y > 6:
        k3.append([x, y])
centroids = [centr(cluster) for cluster in [k1, k2, k3]]
px = int(sum(x for x, y in centroids) / len(centroids) * 10000)
py = int(sum(y for x, y in centroids) / len(centroids) * 10000)
print(px, py)


# def dist(p1, p2):
#     return max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))
#
#
# def centr(cluster):
#     minim = 10 ** 40
#     funal_centroid = []
#     for centroid in cluster:
#         sum_dist = 0
#         for point in cluster:
#             sum_dist += dist(centroid, point)
#         if sum_dist < minim:
#             minim = sum_dist
#             final_centroid = centroid
#     return final_centroid
#
# f = open('27B.txt')
# k1, k2, k3, k4, k5 = [], [], [], [], []
# for line in f:
#     x, y = map(float, line.split(';'))
#     if x > 2.5 and y < 0.5:
#         k1.append([x, y])
#         if y > 0.5 and y < 4.5:
#             k2.append([x, y])
#         if y > 4.5:
#             k3.append([x, y])
#     elif x < 2.5 and y < 2:
#         k4.append([x, y])
#     elif x < 2.5 and y > 2:
#         k5.append([x, y])
# centroids = [centr(cluster) for cluster in [k1, k2, k3, k4, k5]]
# px = int(sum(x for x, y in centroids) / len(centroids) * 10000)
# py = int(sum(y for x, y in centroids) / len(centroids) * 10000)
# print(px, py)