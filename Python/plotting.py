#imports
import matplotlib.pyplot as plt
import numpy as np

#arrays of data
countries = ['Japan', 'Switzerland', 'Australia', 'Singapore', 'Spain', 'France', 'Sweden', 'Italy', 'Canada', 'Norway']
col = ['red', 'orange', 'yellow',  'green', 'violet', 'indigo', 'blue', 'gray', 'black', 'purple']
life_exp = np.array([83.7, 83.4, 82.8, 82.7, 82.7, 82.5, 82.4, 82.3, 82.3, 82.1])                   
gdp = np.array([5.15, 703.08, 1.52, 372.06, 1.39, 2.78, 547.86, 1.99, 1.74, 434.75])
pop = np.array([125.96, 8.54, 25.5, 5.7, 46.94, 67.02, 10.23, 60.36, 37.59, 5.42])

#plot                                
plt.scatter(gdp, life_exp, s = pop*5, c = col)

#customization
plt.title('Relationship Of Life Expectancy and GDP er Capita'
plt.ylabel('Life Expectancy (Yrs)')
plt.xlabel('GDP per Capita (B)')     
plt.yscale('log')      
plt.yticks([80, 80.5, 81, 81.5, 82, 82.5, 83, 83.5, 84])                    
plt.xscale('log')
plt.show()