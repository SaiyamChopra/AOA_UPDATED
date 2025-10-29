import random

# Sample data points
points = [[20, 500], [40, 1000], [30, 800], [18, 300], [28, 1200], [35, 1400], [45, 1800]]

k = 2  # number of clusters
centroids = random.sample(points, k)  # randomly select k centroids

for _ in range(10):  # repeat to converge
    clusters = [[] for _ in range(k)]
    
    # Assign each point to the nearest centroid
    for p in points:
        distances = [((p[0]-c[0])**2 + (p[1]-c[1])**2)**0.5 for c in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(p)
    
    # Update centroids (mean of assigned points)
    new_centroids = []
    for cluster in clusters:
        if cluster:
            x_mean = sum(p[0] for p in cluster) / len(cluster) 
            y_mean = sum(p[1] for p in cluster) / len(cluster)
            new_centroids.append([x_mean, y_mean])
        else:
            new_centroids.append(random.choice(points))
    
    centroids = new_centroids

# Output final clusters and centroids
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")
print("Final centroids:", centroids)
