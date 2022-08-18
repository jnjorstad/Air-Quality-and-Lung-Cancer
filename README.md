# Impact of Environment Quality on Lung Cancer Mortality

# Background:

Lung cancer kills more men and women in the U.S. than any other cancer. When you think of risk factors for lung cancer, what comes to mind? Most of us think about the risk associated with smoking cigarettes, but did you know that air pollution can also cause lung cancer and so can poor land and water environment qualities? Overwhelming evidence shows that particle pollution in the outdoor air we breathe—like that from vehicle exhaust, coal-fired power plants, and other industrial sources, forest fires, organic chemicals, metals, soil, and dust particles—can cause lung cancer and increases the risk of dying early. Here, we tested various supervised learning methods to predict how environmental qualities can have an effect on lung cancer mortality in the United States.

# Rationale:

Exposure to ambient air pollutants has been associated with increased lung cancer incidence and mortality. However, little is known about the impacts of poor quality land and water environments alongside the air pollution exposures on lung cancer-related deaths. The present study aims to determine whether ambient air pollutant exposures and various environment quality indexes are associated with lung cancer deaths.

# Methods Used:
ETL, Supervised Machine Learning; Linear Regression, Random Forest Regression, Support Vector Regression (SVR), Five-fold cross validation, train-test split

# Technologies:
Python Pandas, Python Matplotlib, HTML, Heroku, Sklearn, Flask, pickle

# Dataset Preparation and Data Source:
Population-based lung cancer incidence rates for 2010-2014 were abstracted from National Cancer Institute state cancer profiles (Schwartz et al. 1996). This national county-level database of cancer data is collected by state public health surveillance systems. The domain-specific county-level environmental quality index (EQI) data for 2000-2005 were abstracted from the United States Environmental Protection Agency (USEPA) profile. Complete descriptions of the datasets used in the EQI are provided in Lobdell’s paper (Lobdell 2011). Data were merged based on the Federal Information Processing Standards (FIPS) code. Out of 3144 counties in the United States, this study has available information for 2602 counties: Data was not available for four states, namely Kansas, Michigan, Minnesota, and Nevada, due to state legislation and regulations which prohibit the release of county-level data to outside entities, a county whose lung cancer mortality information is missing were omitted from the data set, the Union County, Florida is an outlier in terms of mortality information which was deleted from the data set. The dataset is available free of cost from https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/HMOEJO/D3GVNB. The dataset (lung-data.xlsx) is also available in excel format. 

# Results:

All three state-of-the-art supervised learning methods--i) linear Regression, ii) random forest Regression, and iii) Support Vector Regression--perform well on the cleaned dataset. Both LinearRegression and RandomForestRegressor works better than SVR model.

![alt text](http://url/to/img.png](https://github.com/jnjorstad/Air-Quality-and-Lung-Cancer/blob/main/performance_table.png)

# Analyses:

* LinearRegression model works a touch better than RandomForestRegressor model. 
* Both LinearRegression and RandomForestRegressor works much better than SVR model. 
* SVR model can also be used for prediction with reasonable accuracy for this particular dataset
* Overall, our findings can help understanding the use of various supervised learning algorithms for predicting lung cancer mortality based on various air * pollutants features as well as land and water quality indexes.
* The scope of this work is limited. The results solely depend on the dataset, data range used for training, and the features considered for training.

# Preview:
