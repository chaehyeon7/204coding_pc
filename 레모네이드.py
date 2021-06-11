###########################
# 라이브러리 사용
import pandas as pd
import tensorflow as tf

###########################
# 파일로부터 데이터 읽어오기
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
레모네이드 = pd.read_csv(파일경로)

###########################
# 데이터의 모양확인
print(레모네이드.shape)

###########################
# 데이터 칼럼이름 확인
print(레모네이드.columns)

###########################
# 독립변수와 종속변수 분리
독립 = 레모네이드[['온도']]
종속 = 레모네이드[['판매량']]
print(독립.shape, 종속.shape)

###########################
# 각각의 데이터 확인해보기
print(레모네이드.head())

###########################
# 모델을 만듭니다.
X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

###########################
# 모델을 학습시킵니다.
model.fit(독립, 종속, epochs=100)

###########################
# 모델을 이용합니다.
print(model.predict(독립))
print(model.predict([[15]]))

print(독립)
print(종속)
#tensorflow 다운 완료