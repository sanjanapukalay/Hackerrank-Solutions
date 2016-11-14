# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

input_param = raw_input().split(" ")
degree = int(input_param[0])
train_rows = int(input_param[1])

train_features = []
test_features = []
train_value = []

for i in range(0,train_rows):
    row = raw_input().split(" ")
    row = [float(i) for i in row]
    train_features.append(row[0:2])
    train_value.append(row[-1])
    
test_rows = int(raw_input())

for i in range(0,test_rows):
    row = raw_input().split(" ")
    row = [float(i) for i in row]
    test_features.append(row[0:2])
   
    
poly_feature = PolynomialFeatures(degree=3)
train_features = poly_feature.fit_transform(train_features)

model = LinearRegression().fit(train_features,train_value)
test_features = poly_feature.fit_transform(test_features)


prediction=model.predict(test_features)
for i in prediction:
    print round(i,2)
    





    

    

    
    
