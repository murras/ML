## lec 01 기본적인 Machine Learning의 용어와 개념 설명

### Supervised learning

- 유형
    - regression (회귀분석)
    - binary classification
    - multi-label classification
- 학습할 수 있는 데이터가 필요하다.
- training을 하고 학습을 기반으로 x에 대한 y값을 얻는다.

---
## lec 02 Linear Regression의 Hypothesis와 cost 설명

### Linear Regrssion
- training data로 training을 한다.
- model을 만든다.
- model을 기반으로 x일때 y값을 얻어낸다.

### Cost function, Loss Function
- 실제 데이터와 가설이 나타낸 데이터의 선과의 거리가 적은게 더 좋다.
- (H(x)-y)^2
    - 항상 양수, 차이가 클 떄 더 큰 값.

 ![Image](https://i.imgur.com/mSxKIyy.png)
---
## lec 03 Linear Regression의 cost 최소화 알고리즘의 원리 설명

### Gradient descent algorithm(경사를 따라 내려가는 알고리즘)

- W-Cost의 그래프에서 경사도가(W)가 완만한 곳으로 옮겨간다.

### Convex function
![Image](https://i.imgur.com/S5QSqPq.png)
