import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime
import pyowm

def plot_bars(days,min_t,max_t):  
        print(days)      
        days=dates.date2num(days)
        print(days) 
        min_temp_bar=plt.bar(days-0.2, min_t, width=0.3, color='yellow')
        max_temp_bar=plt.bar(days+0.2, max_t, width=0.3, color='green')
        plt.xticks(days)
        x_y_axis=plt.gca()
        xaxis_format=dates.DateFormatter('%d/%m')
        
        x_y_axis.xaxis.set_major_formatter(xaxis_format)
        plt.xlabel('Dates(dd/mm)')
        plt.ylabel('Temperature') 
        plt.title('5-Day Forecast')
        
        for bar_chart in [min_temp_bar,max_temp_bar]:
            for index,bar in enumerate(bar_chart):
                height=bar.get_height()
                xpos=bar.get_x()+bar.get_width()/2.0
                ypos=height 
                label_text=str(int(height))
                plt.text(xpos, ypos,label_text,
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        color='Red')
        
        
        plt.savefig('bar.png')
        plt.clf()
    
