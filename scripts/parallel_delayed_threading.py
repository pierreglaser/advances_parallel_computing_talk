Parallel(n_jobs=2, backend="threading")(
    delayed(greet)(friend) for friend in ("Alice", "Bob"))
