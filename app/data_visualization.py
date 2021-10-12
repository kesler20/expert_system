import pandas as pd
import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt
from matplotlib import cm


class DataVisulaization(object):

    def __init__(self, Column1,Column2,Column3, filename, w=[0,0,0]):
        
        Column1 : str
        Column2 : str
        Column3 : str
        filename: str
        w : list
        
        self.filename = filename
        self.Column1 = Column1
        self.Column2 = Column2
        self.Column3 = Column3
        self.w = w

        data = pd.read_csv(filename)
        try:
            self.data2 = data.sample(n=300,axis='rows')
        except ValueError:
            self.data2 = data.sample(n=round(len(data)/1.5),axis='rows')            

    def thred_SCATTER_PLOT(self):

        X = self.data2[self.Column1]
        Y = self.data2[self.Column3]
        Z = self.data2[self.Column2]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(X,Y,Z,'r')
        plt.savefig(r'static\img\Figure_4.png')


    def REGRESSION_GRAPH(self, _alpha):
        #initialize the response space 
        f = lambda x, y: _alpha + self.w[0]*x + self.w[1]*y + self.w[2]
        x0 = np.linspace(0, len(self.data2[self.Column1]))
        y0 = np.linspace(0, len(self.data2[self.Column3]))
        X1, Y1 = np.meshgrid(x0,y0)
        F = f(X1,Y1)
        Z1 = np.array(self.data2[self.Column1]/2)
        z2 = np.array(self.data2[self.Column3]/2)
        z3 = np.array(self.data2[self.Column2]/2)

        y1 = []
        x1 = [y1.append(i) for i in range(12)]
        x1 = np.array(y1)
        y1 = x1

        fig = plt.figure(figsize = [12,8])
        ax = fig.add_subplot(111, projection='3d')
        #ax.plot_surface(X1, Y1, G/2)
        ax.plot_surface(X1, Y1, F/2, cmap=cm.coolwarm)
        plt.scatter(Z1,z3,z2,c='black', marker='o', alpha=_alpha)
        ax.set_xlabel(self.Column1)
        ax.set_ylabel(self.Column3)
        ax.set_zlabel(self.Column2)
        plt.savefig(r'static\img\Figure_3.png')
        #plt.show()

    def BOX_PLOT(self):
        import matplotlib.pyplot as plt
        import numpy as np
        
        fig = plt.figure(figsize =(10, 7))
        
        # Creating axes instance
        ax = fig.add_axes([0, 0, 1, 1])
        ax.boxplot(self.data2[self.Column2])
        plt.axhline(self.data2[self.Column2].mean(), color='black')
        plt.savefig(r'static\img\Figure_5.png')

    def MODEL_ACCURACY(self):
        model = sm.OLS(self.data2[self.Column2], self.data2[[self.Column1,self.Column3, self.Column2]])
        results = model.fit()
        score = results.rsquared
        print(score)
        print(results.params)
        
        x = np.linspace(self.data2[self.Column1].min(),0.005*(self.data2[self.Column1].max()))
        y = np.linspace(self.data2[self.Column3].min(),0.005*(self.data2[self.Column3].max()))
        z = np.linspace(self.data2[self.Column2].min(), 0.005*(self.data2[self.Column2].max()))
        self.w = results.params
        Fx = 1.667 + self.w[0]*x + self.w[1]*y + self.w[2]*z
        operating_range = []
        for i in range(len(Fx)):
            response = Fx[i]
            if response > 1.6 and response < 1.7:
                operating_range.append([x[i], y[i], z[i]])
            else:
                pass
        print(operating_range)
        return results.params, score

def data_driven_optimization():
    x = []
    none = [x.append(v) for v in range(200)]
    y = []
    none = [y.append(v) for v in range(200)]
    z = []
    none = [z.append(v) for v in range(200)]
    data2 = pd.DataFrame(x)
    data2['Risk'] = pd.DataFrame(x)
    data2['Cost'] = pd.DataFrame(y)
    data2['PFD'] = pd.DataFrame(z)
    Column1 = 'Risk'
    Column2 = 'Cost'
    Column3 = 'PFD'
    f = lambda x, y: 1.5 + x**2 + 0.99*y**2
    x0 = np.linspace(0, len(data2[Column1]))
    y0 = np.linspace(0, len(data2[Column3]))
    X1, Y1 = np.meshgrid(x0,y0)
    F = f(X1,Y1)
    data = data2 
    Z1 = np.array(data2[Column1]/2)
    z2 = np.array(data[Column3])
    z3 = np.array(data2[Column2]/2)

    y1 = []
    x1 = [y1.append(i) for i in range(12)]
    x1 = np.array(y1)
    y1 = x1

    fig = plt.figure(figsize = [12,8])
    ax = fig.add_subplot(111, projection='3d')
    #ax.plot_surface(X1, Y1, G/2)
    ax.plot_surface(X1, Y1, F/2, cmap=cm.coolwarm)
    plt.scatter(Z1,z3,z2,c='black', marker='o')
    ax.set_xlabel(Column1)
    ax.set_ylabel(Column3)
    ax.set_zlabel(Column2)
    plt.show()

def generate_random_dataset():
    import pandas as pd
    import numpy as np
    from random import choice

    datapoints = 200
    data_x = []
    data_y = []
    data_z = []
    for i in range(datapoints):
        data_x.append(i)
        data_y.append(i)
        data_z.append(i)
    x = []
    y = []
    z = []
    for i in range(datapoints):
        x.append(choice(data_x))
        z.append(choice(data_z))
        y.append(choice(data_y))

    df = pd.DataFrame(x)
    df['Resistivity'] = pd.DataFrame(x)
    df['Mininimum Ignition Energy'] = pd.DataFrame(y)
    df['Thermal Stability'] = pd.DataFrame(z)
    df.drop([0], axis=1, inplace=True)
    df.to_csv('powder_properties_data.csv')
    print(df)

