'''
전제 
신경망에서는 적용 가능한 가중치와 편향이 있고, 이 가중치와 편향을 훈련 데이터에 적응하도록 조정하는 과정을 '학습'이라한다.
신경망 학습은 다음과 같이 4단계로 수행한다.

1단계 - 미니배치
훈련 데이터 중 일부를 무작위로 가져온다. 이렇게 선별한 데이터를 미니배치라 하며, 
그 미니배치와 손심할수 값을 줄이는 것이 목표이다 

2단계 - 기울기 산출
미니배치의 손실 함수 값을 줄이기 위해 가중치 매개변수의 기울기를 구한다.
기울기는 손실 함수의 값을 가장 작게 하는 방향을 제시한다.

3단계 - 매개변수 갱신
가중치 매개변수를 기울기 방향으로 아주 조금 갱신한다.

4단계 - 반복 
1~3단계를 반복한다

데이터를 무작위로 선정하기 때문에 확률적 경사 하강법 stochastic gradient descent 라고 부른다
'''

import sys 
import os 
import numpy as np
from numpy.core.numeric import cross 
from utils.functions import  *
from utils.gradient import * 

class TwoLayerNet:
  '''
  params: 신경망의 매개변수를 보관하는 딕셔너리 변수 
  params['W1']은 1번째 층의 가중치 , params['b1']은 1번쨰 층의 편향 
  params['W2']은 2번째 층의 가중치, params['b2']은 2번째 층의 편향 
  grad: 기울기를 보관하는 딕셔너리 변수 
  grads['W1']은 1번쨰 층의 가중치의 기울기 , grads['b1']은 1번째 층의 편향의 기울기
  grads['W2']은 2번째 층의 가중치의 기울기, grads['b2']은 2번째 층의 편향의 기울기

  '''
  def __init__(self,input_size, hidden_size, output_size, weight_init_std=0.01) -> None:
    self.params={}
    self.params['W1']=weight_init_std*np.random.randn(input_size,hidden_size)
    self.params['b1']=np.zeros(hidden_size)
    self.params['W2']=weight_init_std*np.random.randn(hidden_size,output_size)
    self.params['b2']=np.zeros(output_size)
  
  def predict(self, x):
    W1,W2=self.params['W1'],self.params['W2']
    b1,b2=self.params['b1'],self.params['b2']

    a1=np.dot(x,W1)+b1
    z1=sigmoid(a1)
    a2=np.dot(z1,W2)+b2
    y=softmax(a2)

    return y

  def loss(self, x,t):
    y=self.predict(x)
    return cross_entropy_error(y,t)

  def accuracy(self, x,t):
    y=self.predict(x)
    y=np.argmax(y,axis=1)
    y=np.argmax(y,axis=1)

    accuracy=np.sum(y==t)/float(x.shape[0])
    return accuracy

  def numerical_gradient(self, x,t):
    loss_w=lambda W: self.loss(x,t)

    grads={}
    grads['W1']=numerical_gradient(loss_w,self.params['W1'])
    grads['W2']=numerical_gradient(loss_w, self.params['W2'])
    grads['b1']=numerical_gradient(loss_w,self.params['b1'])
    grads['b2']=numerical_gradient(loss_w,self.params['b2'])

    return grads

if __name__=='__main__':
  net=TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
  print(net.params['W1'].shape)
  print(net.params['b1'].shape)
  print(net.params['W2'].shape)
  print(net.params['b2'].shape)

  x=np.random.rand(100,784) # 더미 입력 데이터 100장
  t=np.random.rand(100,10) # 더미 정답 레이블 100장 
  grads=net.numerical_gradient(x,t)
  print(grads['W1'].shape)
  print(grads['b1'].shape)
  print(grads['W2'].shape)
  print(grads['b2'].shape)