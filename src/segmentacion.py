import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 42


def main() -> None:
    df = pd.read_csv("data/zonas_argentina_base.csv")

    features = [
        "pobreza_infantil_pct",
        "abandono_secundaria_pct",
        "sobreedad_secundaria_pct",
        "hogares_nbi_pct",
        "barrios_renabap",
    ]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    model = KMeans(n_clusters=3, random_state=RANDOM_STATE, n_init=10)
    df["cluster"] = model.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, df["cluster"])
    print(f"Silhouette Score (k=3): {score:.3f}\n")

    resumen = df.groupby("cluster")[features].mean().round(2)
    print("Promedio por cluster:")
    print(resumen, "\n")

    print("Zonas por cluster:")
    print(df[["zona", "provincia", "cluster", "pobreza_infantil_pct", "abandono_secundaria_pct"]])


if __name__ == "__main__":
    main()
