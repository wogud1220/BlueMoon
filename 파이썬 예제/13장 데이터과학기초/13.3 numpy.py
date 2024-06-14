# 배열 연산하기
import numpy as np
asset = np.array([1000, 2000, 1500, 900]) 
debt = np.array([300, 1200, 0, 1500])
print("asset", asset)
print("debt ", debt)
asset = asset - 500
print("500 deducted each")
print("asset", asset)
print("balance after debt deduction")
balance = asset - debt
print("balance", balance)
print("asset", asset)
print("balances over 1000")
print(balance > 500)
asset = balance
debt = debt - debt
print("asset", asset[0], asset[1], asset[2], asset[3])
print("debt ", debt)
