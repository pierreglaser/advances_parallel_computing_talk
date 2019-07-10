Parallel(n_jobs=2, backend="loky")(
    delayed(greet)(friend) for friend in ("Alice", "Bob"))
