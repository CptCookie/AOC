import requests
import numpy as np
token = "53616c7465645f5f714a6cdb587039fed75269df026ce7ed488de790cdf65fd96d06ec495e5b02c1551c3f2b487d59d5"

r = requests.get("https://adventofcode.com/2019/day/8/input", cookies={"session": token})
pixellist = list(r.content.decode().strip())
# pixellist = [int(x) for x in pixellist]

zeros = 0
result = 0

chunks = [pixellist[i:i + 25] for i in range(0, len(pixellist), 25)]
pics = []

for n in range(0, len(chunks), 6):
    pics.append(chunks[n:n+6])

for n in pics:
    unique, unique_count = np.unique(np.array(n), return_counts=True)
    if unique_count[0] > zeros:
        zeros = unique_count[0]
        result = unique_count[1] * unique_count[2]


print(result)


