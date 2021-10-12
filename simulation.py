import app.data_visualization as dv
import numpy as np
import pandas as pd
import app.data_processing as dp
from matplotlib import pyplot as plt
from database_models import *
import matplotlib
import matplotlib.pyplot as plt
import threading
import time

def generate_risk_matrix():
    import seaborn as sns
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    data = [[6,7,8,9,10],[5,6,7,8,9],[4,5,6,7,8],[3,4,5,6,7]]
    data =  np.array(data)
    #sns.heatmap(data=data,cmap='RdYlGn_r', vmin=3, vmax=10, annot=True, fmt='.0f')
    #plt.show()

    data = {
        '<10E-4 (1)': [6,5,4,3,2],
        '<10E-4/10E-3 (2)': [7,6,5,4,3],
        '<10E-3/10E-2 (3)': [8,7,6,5,4],
        '<10E-2/10E-1 (4)': [9,8,7,6,5],
        '<10E-1/1 (5)': [10,9,8,7,6]
    }
    y_tick_labels = ['More than ten fatalities (5)','More than one fatality (4)', 'One fatality (3)', 'One major injury (2)', 'One minor injury (1)']
    x_tick_labels = ['<10E-4 (1)','<10E-4/10E-3 (2)','<10E-3/10E-2 (3)','<10E-2/10E-1 (4)','<10E-1/1 (5)']
    df = pd.DataFrame(data)
    print(df)
    _plot = sns.heatmap(data=df,cmap='RdYlGn_r',yticklabels=y_tick_labels, annot=True, fmt='.0f')
    _plot.set_xticklabels(labels=x_tick_labels, rotation=45)
    plt.ylabel('Magnitude (fatalities)', fontsize = 10) # x-axis label with fontsize 15
    plt.xlabel('Frequencies (events/year)', fontsize = 10) # y-axis label with fontsize 15
    plt.suptitle('Risk Matrix')
    plt.show()

def response_summary(X, Y, Z,accuracy,two_d=False,filename=None):
    if two_d:
        df = pd.read_csv(filename)
        X = df[X]
        Y = df[Y]
        df.drop(['Unnamed: 0'], axis=1, inplace=True)
        df.to_html(r'templates\response.html')
        df.plot()
        plt.savefig(r'static\img\Figure_2.png')
    else:
        df = pd.read_csv(filename)
        X = df[X]
        Y = df[Y]
        Z = df[Z]
        df.drop(['Unnamed: 0'], axis=1, inplace=True)
        df.to_html(r'templates\response.html')
        df.plot()
        plt.savefig(r'static\img\Figure_2.png')
        plt.scatter(X,Y,Z)
    response_file = open(r'templates\response.html', 'r')
    response_file_content = response_file.read()
    response_file.close()
    lopa_file = open('Lopa.html', 'r')
    lopa_file_content = lopa_file.read()
    lopa_file.close()
    output_file = open('output.txt', 'w')
    output_file.write("{% extends 'base.html' %}\n")
    output_file.write("{% block title %}Response Page{% endblock %}\n")
    output_file.write("{% block content %}\n")
    output_file.write("<h2><strong>2D Plot</strong></h2>\n")
    output_file.write("<img src='{{ url_for('static', filename='img/Figure_2.png') }}' alt='graph' width=600 height=400>\n")
    output_file.write("<hr/>\n")
    output_file.write("<h2><strong>Regression Results</strong></h2>\n")
    output_file.write("<img src='{{ url_for('static', filename='img/Figure_3.png') }}' alt='graph' width=600 height=400>\n")
    output_file.write("<hr/>\n")
    output_file.write("<h2><strong>3D Plot</strong></h2>\n")
    output_file.write("<img src='{{ url_for('static', filename='img/Figure_4.png') }}' alt='graph' width=600 height=400>\n")
    output_file.write("<hr/>\n")
    output_file.write("<h2><strong>Box Plot</strong></h2>\n")
    output_file.write("<img src='{{ url_for('static', filename='img/Figure_5.png') }}' alt='graph' width=600 height=400>\n")
    output_file.write("<hr/>\n")
    output_file.write("<strong>Table 1</strong>\n")
    output_file.write("{}".format(response_file_content))
    output_file.write("<hr/>\n")
    output_file.write(' THE ACCURACY OF THE MODEL IS: {}'.format(accuracy))
    output_file.write("<hr/>\n")
    output_file.write("<h2><strong>Layer Of Protection Analysis</strong></h2>\n")
    output_file.write("{}".format(lopa_file_content))
    output_file.write("<hr/>\n")
    output_file.write("<h2><strong>Risk Assesment</strong></h2>\n")
    output_file.write("<img src='{{ url_for('static', filename='img/Risk_matrix.png') }}' alt='graph' width=600 height=400>\n")
    output_file.write("<hr/>\n")    
    output_file.write("{% endblock %}\n")
    output_file.close()   

    output_text_file = open('output.txt', 'r')
    output_text_file_content = output_text_file.read()
    output_text_file.close()

    output_file = open(r'templates\data_analysis.html', 'w')
    output_file.write(f'{output_text_file_content}')
    output_file.close()
    #plt.show()



