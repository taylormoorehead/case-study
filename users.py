import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2018, 2030)
users_no_tax = np.array([347, 653, 1039, 1407, 1720, 1922, 2050, 2136, 2198, 2249, 2299, 2354])

def predict_users_with_tax(years, users_no_tax, initial_loss_rate, start_year):
    users_with_tax = np.copy(users_no_tax)
    
    start_index = np.where(years == start_year)[0][0]
    users_with_tax[start_index] = users_no_tax[start_index] * (1 - initial_loss_rate)
    
    for i in range(start_index + 1, len(users_with_tax)):
        users_with_tax[i] = users_with_tax[i-1] * (1 - 0.05 / np.log(i - start_index + 2))
    
    return users_with_tax

initial_loss_rate = 0.07
start_year = 2024

users_with_tax = predict_users_with_tax(years, users_no_tax, initial_loss_rate, start_year)

plt.figure(figsize=(14, 7))

plt.plot(years, users_no_tax, label='Users without carbon-based tax', marker='o', color='b')
plt.plot(years, users_with_tax, label='Users with carbon-based tax', marker='o', linestyle='--', color='r')

bar_width = 0.35
plt.bar(years - bar_width / 2, users_no_tax, bar_width, label='Users without carbon-based tax', color='b', alpha=0.5)
plt.bar(years + bar_width / 2, users_with_tax, bar_width, label='Users with carbon-based tax', color='r', alpha=0.5)

plt.xlabel('Year')
plt.ylabel('Number of Users (millions)')
plt.title('Prediction of TikTok Users with and without Carbon-Based Tax')
plt.legend()
plt.grid(True)
plt.show()
