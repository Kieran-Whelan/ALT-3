import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#function that cleans segments of data
def clean_up(data, column, graph_range):
    #picks range of quarters for graph to display
    if graph_range == 1:
        data = data.iloc[0:84]
    elif graph_range == 2:
        data = data.iloc[0:40]
    elif graph_range == 3:
        data = data.iloc[40:84]
    data = data.drop(data.iloc[:, 2:], axis=1)
    #parses data for use
    data[column]=data[column].str.replace(",", "")
    data[column]=data[column].astype(int)
    return data

#function thats finds sum of medians
def sum_of_medians(data1, data2, data3, col1, col2, col3):
    col1 = data1[col1]
    col2 = data2[col2]
    col3 = data3[col3]
    res = col1.groupby(np.arange(len(col1))).median() + col2.groupby(np.arange(len(col2))).median() + col3.groupby(np.arange(len(col3))).median()
    return res

def main():
    graph_range = int(input("Select range: (1. Full) (2. First Half) (3. Second Half)\n")) #user input for graph's range

    food_data = pd.read_csv("data\Food.csv")
    restaurant_data = pd.read_csv("data\Hotels.csv")
    clothing_data = pd.read_csv("data\Clothing.csv")
    food_data = clean_up(food_data, "Food and non-alcoholic beverages", graph_range)
    restaurant_data = clean_up(restaurant_data, "Restaurant and hotels", graph_range)
    clothing_data = clean_up(clothing_data, "Clothing and footwear", graph_range)
    median = sum_of_medians(food_data, restaurant_data, clothing_data, "Food and non-alcoholic beverages", "Restaurant and hotels", "Clothing and footwear")

    display = input("Which graph do you want to display? (1. Main), (2. Medians)\n")

    if display == "1":
        plt.plot(food_data["Time period and codes"], food_data["Food and non-alcoholic beverages"], label="Food and non-alcoholic beverages")
        plt.plot(food_data["Time period and codes"], restaurant_data["Restaurant and hotels"], label="Restaurants and hotels")
        plt.plot(food_data["Time period and codes"], clothing_data["Clothing and footwear"], label="Clothing and footwear")
        plt.title("Money Spent Compared To Time Period")

    if display == "2":
        plt.plot(food_data["Time period and codes"], median, label = "Median Expenditure")
        plt.title("Money Spent Compared To Time Period (Median)")

    plt.xlabel("Time period and codes")
    plt.ylabel("Money Spent (£M)")
    plt.legend(loc="upper right")
    plt.xticks(rotation="vertical")
    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()
    
if __name__ == "__main__":
    main()