# -*- coding: utf-8 -*-
"""03-01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-HhCE_5lvSQP54F9IuQ2B1YB-N2Gwrzj
"""

import numpy as np

perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0,
       21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7,
       23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5,
       27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0,
       39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5,
       44.0])
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

import matplotlib.pyplot as plt
plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)

test_array = np.array([1,2,3,4])
print(test_array.shape)
test_array = test_array.reshape(2,2)
print(test_array.shape)

train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1,1)
print(train_input.shape, test_input.shape)

from sklearn.neighbors import KNeighborsRegressor
knr = KNeighborsRegressor()

# k - 최근접 이웃 회귀 모델을 훈련합니다
knr.fit(train_input, train_target)

print(knr.score(test_input, test_target)) # 결정계수

# score() 메서드의 출력값은 높을수록 좋은 것임.

from sklearn.metrics import mean_absolute_error

# 테스트 세트에 대한 예측을 만듦
test_prediction = knr.predict(test_input)

# 테스트 세트에 대한 평균 절댓값 오차를 계산
mae = mean_absolute_error(test_target, test_prediction)
print(mae) # 예측이 평균적으로 19g 정도 타깃값과 다름을 알 수 있음.

print(knr.score(train_input, train_target))

# 과소적합인 상태를 해결할 방법은 모델을 좀 더 복잡하게 만드는 것이다
# 모델을 더 복잡하게 만드는 방법은 이웃의 개수 k를 줄이는 것.  이웃의 개수를 줄이면 훈련세트의 국지적인 패턴에 민감해지고,
# 이웃의 개수를 늘리면 데이터 전반에 있는 일반적 패턴을 따르게 될 것임.

# 이웃의 개수를 3으로 설정
knr.n_neighbors = 1

# 모델 다시 훈련
knr.fit(train_input, train_target)
print(knr.score(train_input, train_target))

print(knr.score(test_input, test_target))

# k-최근접 이웃 회귀 객체를 만듦
knr = KNeighborsRegressor()
# 5 ~ 45 x 좌표 만들기
x = np.arange(5,45).reshape(-1,1)

# n = 1, 5, 10 일 때 예측 결과를 그래프로 그립니다
for n in [1,5,10]:
  # 모델 훈련
  knr.n_neighbors = n
  knr.fit(train_input, train_target)

  # 지정한 범위 x 에 대한 예측을 구합니다.
  prediction = knr.predict(x)

  # 훈련 세트와 예측 결과를 그래프로 그림
  plt.scatter(train_input, train_target)
  plt.plot(x, prediction)
  plt.title('n_neighbors = {}'.format(n))
  plt.xlabel('length')
  plt.ylabel('weight')
  plt.show()

