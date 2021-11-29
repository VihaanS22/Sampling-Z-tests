import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

print("")
print("Article Reading Time Analyzer")
print("")
print("What would you like to view?")
print("")
print("1.Total mean and the stdev of data")
print("2.Sampling mean and z-test score")

print("")

analyze = input("Enter Your Choice as 1 or 2:- ")

df = pd.read_csv("medium_data.csv")

data = df["reading_time"].tolist()

if(analyze == "1"):


    p_mean = statistics.mean(data)
    print("THE POPULATION MEAN IS ", p_mean)
    print("")

    stdev = statistics.stdev(data)
    print("THE STDEV IS ", stdev)
    print("")

if(analyze ==  "2"):
   
    def randomSetOfMeans(counter):
        dataset=[]
        for i in range(0, counter):
            randIndex = random.randint(0, len(data)) 
            value = data[randIndex]
            dataset.append(value)

        t_mean = statistics.mean(dataset)
        return t_mean

    mean_list = []

    for i in range(0,100):
        setOfMeans = randomSetOfMeans(30)
        mean_list.append(setOfMeans)

    sample_mean = statistics.mean(mean_list)
    print("The mean of 30 samples is", sample_mean)
    print("")

    sample_stdDev = statistics.stdev(mean_list)
    print("The 30 samples stdev is", sample_stdDev)
    print("")



    first_start, first_end = sample_mean - sample_stdDev, sample_mean + sample_stdDev
    sec_start, sec_end = sample_mean - 2*sample_stdDev, sample_mean + 2*sample_stdDev
    three_start, three_end = sample_mean - 3*sample_stdDev, sample_mean + 3*sample_stdDev

    sampleFig = ff.create_distplot([mean_list],["Sample Means"],show_hist=False)
    sampleFig.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0,1], mode = "lines", name = "Mean"))

    sampleFig.add_trace(go.Scatter(x = [first_start, first_start], y = [0, 1], mode = "lines", name = "-Deviate"))

    sampleFig.add_trace(go.Scatter(x = [first_end, first_end], y = [0, 1], mode = "lines", name = "+Deviate"))

    sampleFig.add_trace(go.Scatter(x = [sec_start, sec_start], y = [0, 1], mode = "lines", name = "-2Deviate"))

    sampleFig.add_trace(go.Scatter(x = [sec_end, sec_end], y = [0, 1], mode = "lines", name = "+2Deviate"))

    sampleFig.add_trace(go.Scatter(x = [three_start, three_start], y = [0, 1], mode = "lines", name = "-3Deviate"))

    sampleFig.add_trace(go.Scatter(x = [three_end, three_end], y = [0, 1], mode = "lines", name = "+3Deviate"))

    sampleFig.show()

    z_test = (sample_mean - p_mean)/stdev
    print("The z-test score according to the 30 samples is ", z_test)
    print("")