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


f = open('demo_2025_27_Б.txt')
k1, k2, k3 = [], [], []
for line in f:
    x, y = map(float, line.split())
    if x > 5:
        k1.append([x, y])
    elif x < 5 and y > 6:
        k2.append([x, y])
    elif x < 5 and y < 6:
        k3.append([x, y])
centroids = [centr(cluster) for cluster in [k1, k2]]
px = int(sum(x for x, y in centroids) / len(centroids) * 10000)
py = int(sum(y for x, y in centroids) / len(centroids) * 10000)
print(px, py)
