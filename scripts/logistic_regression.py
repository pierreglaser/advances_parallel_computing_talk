clf = RandomForestClassifier(n_estimators=100, n_jobs=4)
X, y = get_data()
clf.fit(X, y)  # runs on 4 cores!
