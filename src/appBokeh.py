import bokeh
from bokeh.sampledata.stocks import AAPL, FB, GOOG, MSFT
from bokeh.plotting import figure, output_file, show 
import numpy as np

output_file = 'stocks.html'
graph = figure(x_axis_type='datetime', title='Stock closing price')
graph.xaxis.axis_label = "Date"
graph.yaxis.axis_label = "Price (in USD)"


# Ploteo la linea de Apple 
x_axis_coordinate = np.array(AAPL['date'], dtype=np.datetime64)
y_axis_coordinate = AAPL['adj_close']
color = "blue"
legend_label = "APPLE"
graph.line(x_axis_coordinate, y_axis_coordinate, color=color, legend=legend_label)

# Ploteo la linea de Facebook 
x_axis_coordinate = np.array(FB['date'], dtype=np.datetime64)
y_axis_coordinate = FB['adj_close']
color = "black"
legend_label = "Face"
graph.line(x_axis_coordinate, y_axis_coordinate, color=color, legend=legend_label)


# Ploteo la linea de Google
x_axis_coordinate = np.array(GOOG['date'], dtype=np.datetime64)
y_axis_coordinate = GOOG['adj_close']
color = "orange"
legend_label = "Google"
graph.line(x_axis_coordinate, y_axis_coordinate, color=color, legend=legend_label)



# Ploteo la linea de Microsoft 
x_axis_coordinate = np.array(MSFT['date'], dtype=np.datetime64)
y_axis_coordinate = MSFT['adj_close']
color = "green"
legend_label = "Microsoft"
graph.line(x_axis_coordinate, y_axis_coordinate, color=color, legend=legend_label)


# Relocate the legend at the top left

graph.legend.location = "top_left"


# Displaying the model 
show(graph)