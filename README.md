<br/>
<p align="center">
  <a href="https://github.com/TribeOfJudahLion/Exploratory-Data-Analysis">
    <img src="" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Exploratory Data Analysis (EDA) on the Wine Quality Dataset</h3>

  <p align="center">
    "Decoding Dionysus: Unveiling the Secrets of Wine Quality through Physicochemical Analysis"
    <br/>
    <br/>
    <a href="https://github.com/TribeOfJudahLion/Exploratory-Data-Analysis"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/TribeOfJudahLion/Exploratory-Data-Analysis">View Demo</a>
    .
    <a href="https://github.com/TribeOfJudahLion/Exploratory-Data-Analysis/issues">Report Bug</a>
    .
    <a href="https://github.com/TribeOfJudahLion/Exploratory-Data-Analysis/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/TribeOfJudahLion/Exploratory-Data-Analysis/total) ![Contributors](https://img.shields.io/github/contributors/TribeOfJudahLion/Exploratory-Data-Analysis?color=dark-green) ![Stargazers](https://img.shields.io/github/stars/TribeOfJudahLion/Exploratory-Data-Analysis?style=social) ![Issues](https://img.shields.io/github/issues/TribeOfJudahLion/Exploratory-Data-Analysis) ![License](https://img.shields.io/github/license/TribeOfJudahLion/Exploratory-Data-Analysis) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

**Problem Statement:**

The quality of wine is of great interest to producers and consumers alike, influencing both marketability and enjoyment. However, wine quality assessment can be subjective, time-consuming, and require expert knowledge. The Wine Quality dataset, which includes physicochemical properties and quality ratings for red variants, presents an opportunity to explore whether these properties can be used to predict wine quality objectively. This problem is particularly challenging due to the nuanced nature of wine quality, which does not always follow strict rules and can vary based on individual preferences and external conditions.

**Objective:**

The primary goal is to conduct an exploratory data analysis (EDA) on the Wine Quality dataset to uncover initial insights into the relationships between the physicochemical properties of wine and its quality ratings. This analysis will serve as a foundation for further modeling efforts aimed at predicting wine quality based on these properties. 

**Solution Approach:**

1. **Data Acquisition and Loading:**
   - Utilize the Pandas library to import the Wine Quality dataset from the UCI Machine Learning Repository.
   - Use the `read_csv` function, accounting for the semicolon separator in the dataset.

2. **Preliminary Data Inspection:**
   - Perform an initial examination of the dataset by viewing the first few rows, determining its shape, and checking the data types of the columns.
   - These steps help ensure that the data is loaded correctly and that the variables are of the expected types.

3. **Data Cleaning and Preprocessing:**
   - Check for missing values across all columns.
   - Address any data cleaning needs, such as handling missing values or correcting data types, although the given dataset is known to be clean.

4. **Descriptive Statistics:**
   - Generate summary statistics to understand the central tendency, spread, and shape of the dataset’s distribution.

5. **Data Visualization:**
   - Use Seaborn and Matplotlib for visual exploration of the data.
   - Create a histogram (bar plot) to visualize the frequency distribution of the wine quality ratings.
   - Generate box plots for each physicochemical variable, grouped by wine quality rating, to examine the distribution of these variables in relation to wine quality and identify any potential outliers.

6. **Insights and Observations:**
   - From the histogram, observe the distribution of wine quality ratings and identify the most common ratings.
   - Through the box plots, explore how different physicochemical properties vary with wine quality. This can reveal whether any properties are strong indicators of quality.

7. **Report and Documentation:**
   - Document the findings and insights from the EDA, including any notable relationships between physicochemical properties and wine quality.
   - Provide visualizations and their interpretations to support the analysis.

8. **Future Work:**
   - Suggest further analysis or modeling that can be conducted based on the findings of the EDA.
   - Recommend machine learning techniques that could be employed to predict wine quality from the physicochemical properties.

By following this detailed approach, one can systematically analyze the Wine Quality dataset to understand the underlying patterns and lay the groundwork for predictive modeling.

**Solution Based on Output Results:**

1. **Data Acquisition and Loading:**
    - The dataset has been successfully loaded from the UCI Machine Learning Repository using the Pandas library.
    - The dataset used is specifically the Wine Quality dataset for red wines.

2. **Preliminary Data Inspection:**
    - The dataset consists of 1599 rows and 12 columns, indicating 1599 wine samples each with 12 attributes.
    - Initial rows of the dataset show attributes such as 'fixed acidity', 'volatile acidity', 'citric acid', and so forth.
    - The data types are mostly `float64` for the physicochemical properties, except 'quality' which is `int64`, representing the wine quality score.

3. **Data Cleaning and Preprocessing:**
    - Inspection for missing values in the dataset reveals that there are no missing values in any of the columns. This means that the dataset is quite clean and does not require imputation or handling of missing data.
    
4. **Descriptive Statistics:**
    - The average (mean) fixed acidity level is approximately 8.32, volatile acidity averages around 0.53, and the mean alcohol content is roughly 10.42%.
    - Most wines in the dataset have a quality rating between 5 and 6. The minimum quality rating is 3, and the maximum is 8.
    - The standard deviation (std) shows variation in the dataset. For instance, the alcohol content has a std of 1.065668, which suggests some variability in the alcohol percentages among the wines.

5. **Data Visualization:**
    - While the visualization outputs (such as histograms and box plots) are not directly shown in the text outputs, we can infer that:
        - The histogram would depict the frequency distribution of the wine quality, giving a visual sense of the most common quality ratings.
        - The box plots, grouped by wine quality, would provide insights into the distribution of physicochemical properties for wines of different quality scores. Outliers, median values, and the spread of the data can be discerned from these plots.

6. **Insights and Observations:**
    - The frequency distribution shows that the majority of wines are rated as quality 5 (681 instances) or 6 (638 instances). Few wines achieve a rating of 8 (18 instances), and only a handful have a low rating of 3 (10 instances).
    - This suggests that most wines in this dataset are of average quality, with few outliers on either end of the quality spectrum.

7. **Report and Documentation:**
    - The dataset provides a comprehensive overview of the physicochemical properties of red wines and their associated quality ratings.
    - From the provided statistics and data distributions, it's evident that there is a variety in the dataset, which will be valuable for any subsequent analysis or predictive modeling efforts.
    - The absence of missing values ensures that the dataset is robust and reduces the preprocessing steps required in future analysis.

8. **Future Work:**
    - The exploratory data analysis has laid a solid foundation for predictive modeling. Machine learning algorithms, such as regression models or classification techniques, could be used to predict wine quality based on its physicochemical properties.
    - Further analysis could involve examining potential correlations between specific properties and wine quality or clustering wines based on their properties to identify patterns or groups.
    - Given the ordinal nature of the quality rating, ordinal regression or classification algorithms might be particularly suitable for predicting wine quality.


## Built With

This project utilizes several key technologies and libraries. Here's a rundown of the main tools used in the development and analysis process:

- [Python](https://www.python.org/) - The programming language used for the entirety of the project.
- [Pandas](https://pandas.pydata.org/) - An open-source data analysis and manipulation tool built on top of Python.
- [Matplotlib](https://matplotlib.org/) - A comprehensive library for creating static, animated, and interactive visualizations in Python.
- [Seaborn](https://seaborn.pydata.org/) - A Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.
- [Jupyter Notebook](https://jupyter.org/) - An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.

### Additional Tools

Alongside the main technologies, the following tools and resources were used to aid in the development and analytical process:

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) - A collection of databases, domain theories, and data generators widely used by the machine learning community.
- [Git](https://git-scm.com/) - A free and open-source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
- [GitHub](https://github.com/) - A platform for version control and collaboration. It lets you and others work together on projects from anywhere.

By leveraging the combination of these tools and libraries, we've constructed a robust framework for analyzing the Wine Quality dataset and drawing meaningful insights from it.

- [Pandas](https://pandas.pydata.org/) - An open-source data analysis and manipulation tool, built on top of the Python programming language.
- [Matplotlib](https://matplotlib.org/) - A comprehensive library for creating static, animated, and interactive visualizations in Python.
- [Seaborn](https://seaborn.pydata.org/) - A Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.



## Getting Started

This section provides instructions on how to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or later
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name


## Contributing



### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/TribeOfJudahLion/Exploratory-Data-Analysis/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion/) - **

## Acknowledgements

* []()
* [](Best-README-Template)
* []()
