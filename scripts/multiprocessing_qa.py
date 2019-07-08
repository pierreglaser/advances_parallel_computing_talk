
# A: worker pools
pool = mp.Pool(2)
results = pool.map(greet, ["Alice", "Bob"])
