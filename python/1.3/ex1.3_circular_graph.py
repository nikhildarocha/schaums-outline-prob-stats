import matplotlib.pyplot as plt

# Data to plot
labels = 'Philadelphia', 'Suburbs', 'PA', 'NJ', 'Elsewhere'
sizes = [225, 100, 60, 75, 40]

fig = plt.figure(figsize =(10, 7)) 
plt.pie(sizes, labels = labels, autopct='%1.0f%%') 
  
# show plot 
plt.show() 