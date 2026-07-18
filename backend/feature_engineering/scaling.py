from sklearn.preprocessing import StandardScaler
def scale_features(data, columns):


    print("\n========== SCALING FEATURES ==========\n")

    scaler = StandardScaler()

    data[columns] = scaler.fit_transform(data[columns])

    print(data[columns].head())

    print("\n Scaling Complete!\n")

    return data, scaler