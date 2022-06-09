import pandas as pd
import numpy as np
import tensorflow as tf
import pymysql

connect = pymysql.connect(host='localhost', user='beom', password="1234", db='sejong', charset='utf8')

sql = "SELECT * FROM spec"
data = pd.read_sql(sql, connect)

corr_df = data.corr()
corr_df = corr_df.apply(lambda x: round(x ,2))


a1 = corr_df.iloc[0]['gpa']
a2 = corr_df.iloc[0]['english']
a3 = corr_df.iloc[0]['outside']
a4 = corr_df.iloc[0]['volunteer']
a5 = corr_df.iloc[0]['intern']

# 합격여부와 각 파라미터별 피어슨 상관계수
# 가중치구하는코드

ydata = data['result'].values

xdata1 = (data['gpa'].values)/4.5
xdata2 = (data['english'].values)/4
xdata3 = (data['outside'].values)/5
xdata4 = (data['volunteer'].values)/3
xdata5 = (data['intern'].values)/2
# 각 파라미터를 변수에 할당 후 최댓값으로 나누어 0~1 사이의 값으로 치환

xdata1 = xdata1*a1
xdata1 = pd.DataFrame(xdata1)
xdata1.columns = ["gpa"]
# 학점 가중치 적용


xdata2 = xdata2*a2
xdata2 = pd.DataFrame(xdata2)
xdata2.columns = ["english"]
# 영어 가중치 적용


xdata3 = xdata3*a3
xdata3 = pd.DataFrame(xdata3)
xdata3.columns = ["outside"]
# 대외활동 가중치 적용


xdata4 = xdata4*a4
xdata4 = pd.DataFrame(xdata4)
xdata4.columns = ["volunteer"]
# 봉사 가중치 적용


xdata5 = xdata5*a5
xdata5 = pd.DataFrame(xdata5)
xdata5.columns = ["intern"]
# 인턴 가중치 적용

xdataR =pd.concat([xdata1,xdata2,xdata3,xdata4,xdata5], axis=1)
# 각 파라미터별 데이터 재통합

xdata=[]
for i,rows in xdataR.iterrows():
    xdata.append([ rows['gpa'], rows['english'], rows['outside'], rows['volunteer'], rows['intern']])
print(xdata)




model = tf.keras.models.Sequential([
     tf.keras.layers.Dense(64,  activation='tanh'),
     tf.keras.layers.Dense(128, activation='tanh'),
     tf.keras.layers.Dense(1, activation='sigmoid') #sigmoid 0~1 사이의 숫자로 나옴 (확률)
])


model.compile(optimizer='adam', loss= 'binary_crossentropy', metrics= ['accuracy'])


model.fit(np.array(xdata), np.array(ydata), epochs=100)   #학습데이터, 결과값, epochs=100(백번 학습)


def predictSomething(stduent):
    tmp = [stduent]

    tmp[0][0] = tmp[0][0] / 4.5 * a1
    tmp[0][1] = tmp[0][1] / 4 * a2
    tmp[0][2] = tmp[0][2] / 5 * a3
    tmp[0][3] = tmp[0][3] / 3 * a4
    tmp[0][4] = tmp[0][4] / 2 * a5
    # 입력 파라미터 0~1로 바꾼후 가중치 적용

    if tmp[0][1] == 0.0:
        return 0
    else:
        prediction = model.predict(tmp)
        if prediction == 0:
            return 0;
        else:
            i = 100*prediction
            m = round(i[0][0], 2)
            return m

connect.close()
