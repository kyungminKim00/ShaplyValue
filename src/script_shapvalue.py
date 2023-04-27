import itertools
import numpy as np


# 특성 개수와 부분집합의 크기를 입력으로 받아 샤플리 가중치를 계산하는 함수
def shapley_weight(num_features, subset_size):
    num = np.math.factorial(num_features)
    den = np.math.factorial(subset_size) * np.math.factorial(
        num_features - subset_size - 1
    )
    weight = num / den
    return weight


# 임의로 정의한 모델 함수 f
def model_function(subset):
    # 실제 모델 함수를 정의해야 함
    # 예시: f(S) = sum(S)와 같은 간단한 함수를 사용할 수 있음
    return sum(subset)


# 특성 개수와 샤플리 값 계산을 위한 부분집합 생성
num_features = 5
features = list(range(num_features))
shap_values = np.zeros(num_features)

# 각 부분집합에 대한 샤플리 가중치 계산
for i in range(num_features):
    for subset_size in range(num_features):
        subsets = itertools.combinations(features, subset_size)
        for subset in subsets:
            if i not in subset:
                S = set(subset)
                weight = shapley_weight(num_features, subset_size)
                shap_values[i] += weight * (model_function(S | {i}) - model_function(S))

print(f"Shapley Values: {shap_values}")
