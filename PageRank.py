links = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['A']
}

d = 0.85  # Damping factor
pages = list(links.keys())
N = len(pages)
ranks = {p: 1 / N for p in pages}

for _ in range(100):  # iterate to converge
    new_ranks = {}
    for page in pages:
        new_ranks[page] = (1 - d) / N
        for other in pages:
            if page in links[other]:
                new_ranks[page] += d * ranks[other] / len(links[other])
    ranks = new_ranks

for p, r in ranks.items():
    print(f"{p}: {r:.4f}")
