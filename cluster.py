from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
# '22년도' 컬럼은 범주형 데이터로, 군집화에 포함하지 않으므로 이를 제외합니다.
data = pd.read_excel('/data.xlsx')
data = pd.DataFrame(data)
data_for_clustering = data.drop(columns=['22년도'])

# 결측치 처리 (필요한 경우)
data_for_clustering = data_for_clustering.fillna(data_for_clustering.mean())

# 데이터 정규화
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_for_clustering)

# 최적의 k 값을 찾기 위한 엘보우 기법 적용
inertia = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# 엘보우 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(k_range, inertia, marker='o')
plt.xlabel('Number of clusters, k')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.show()

# 최적의 k 값으로 군집화 수행 (이전에 찾은 최적의 k=3로 가정)
k_optimal = 3
kmeans = KMeans(n_clusters=k_optimal, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# 원본 데이터에 군집 라벨 추가
data['Cluster'] = clusters
data.to_excel('/mnt/data/clustered_data.xlsx', index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Clustered Data", dataframe=data)
