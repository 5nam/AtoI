# -*- coding: utf-8 -*-
"""2-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m-fDGAgtfICYEWvqsXq6DmmLSArdjK4W
"""

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = [[l,w] for l, w in zip(fish_length, fish_weight)]
fish_target = [1] * 35 + [0] * 14

# 처음 35개를 훈련 세트로, 나머지 14개를 테스트 세트로 사용할 것.

# KNeighborsClassifier 객체 생성
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# 훈련 세트로 입력값 중 0부터 34번째 인덱스까지 사용
train_input = fish_data[:35]
# 훈련 세트로 타깃값 중 0부터 34번째 인덱스까지 사용
train_target = fish_target[:35]
# 테스트 세트로 입력값 중 35번째부터 마지막 인덱스까지 사용
test_input = fish_data[35:]
# 테스트 세트로 타깃값 중 35번째부터 마지막 인덱스까지 사용
test_target = fish_target[35:]

# 슬라이싱 연산으로 인덱스 0~34까지 : 훈련 세트, 인덱스 35~48까지 : 테스트 세트로 선택

# 훈련세트로 fit(), 테스트 세트로 score() 호출 및 평가
kn = kn.fit(train_input, train_target)
kn.score(test_input, test_target)

# 정확도가 0.0 이 나오는 것은 샘플링인 골고루 섞여 있지 않고, 한쪽으로 치우친 샘플링 편향 상태이므로

import numpy as np

# 생선 데이터를 2차원 넘파이 배열로 변환
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

# print(input_arr)
print(input_arr.shape) # 이 명령을 사용하면 (샘플 수, 특성 수)를 출력합니다.

# 넘파이 arange() 함수를 사용하여 0 ~ 48까지 1씩 증가하는 인덱스를 간단히 만들 수 있음.
np.random.seed(42)
index = np.arange(49) # arange() 함수에 정수 n 을 전달하면 0~n-1까지 1씩 증가하는 배열을 만듦.
np.random.shuffle(index) # 주어진 배열을 무작위로 섞음.

print(index)

# 처음 35개 input_arr와 target_arr 에 전달하여 훈련 세트로
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

# index 의 첫 번째 값은 13이므로 tarin_input 의 첫 번째 원소는 input_arr의 14번째 원소가 들어 있을 것.
# print(input_arr[13], train_input[0])

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

import matplotlib.pyplot as plt
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(test_input[:,0], test_input[:,1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# k-최근접 이웃 모델을 훈련시켜보기
kn = kn.fit(train_input, train_target)

# test_input, test_target 으로 이 모델을 테스트
kn.score(test_input, test_target)

# predict() 메서드로 테스트 세트의 예측 결과와 실제 타깃을 확인
kn.predict(test_input) # test_target 과 일치