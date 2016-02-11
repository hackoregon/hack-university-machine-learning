# Time Series

Time series can be a gold mine for machine learning. It's fun (and valuable) to be able to forecast the future. 

- sound files
  - speech recognition
  - song identification
- log files on servers
- financial transaction logs
- finance (stock market) time series
- [weather data](http://slides.com/hobsonlane/pycon2015-predict-weather-with-pybrain#/)
- twitter streams (but that requires NLP, more on that later)
- mobile phone GPS tracks
- mobile phone accelerometer/gyro (IMU data)
  - gesture recognition
  - [cycling](http://cal.streetsblog.org/2016/02/04/crowdsource-bicycling-app-ride-report-goes-national-today/)
  - sport and activity monitoring
  - [Intel's Curie](http://www.intel.com/content/www/us/en/wearables/wearable-soc.html)
  - wearables like fitbit
  - Turing test to tell who's using your phone (security/auto-signin)
- medical
  - EKG heart monitors
  - pulmanary stress test data
  - lie detector data 
  - FMRI "movies"
- prosthetic arm


## Time Series Data Quirks

But time series data has a lot of quirks to worry about 

- What's different
  - both continuous and number as well as categorical and discontinuous
  - features
    - days of the week
    - months of the year
    - leap years
    - day of the year
    - day of the month
    - day of the quarter
    - quarter of the year
  - segmentation
  - data points are highly correlated with each other
  - time and relative time are added dimensions of all features
  - order of samples matters 
- Adding and subtracting times in python
- Preprocessing
  - What is DSP
  - downsampling
  - upsampling
  - synchronization
  - windowing
    - nonoverlapping windows
    - rolling windows
  - incremental or recursive processing
    - advantages and disadvantages
  - online vs offline processing

## Features

Generating and extracting features from time series data requires creativity, secret recipes. For one the features themselves are time-varying so you can filter the filters ad-infinitum.


- types of features
  - spectral
      - FFT-based
      - wavelets
      - Hong? filters?
  - statistical
    - variance
  - shape
  - "meta" features
  - derivatives/rates
  - rotation/transformation
- windowing
  - nonoverlapping windows
  - rolling windows
- IMU "registration" or normalization
  - Kalman Filter on just acceleromters
  - Kalman Filter on gyros and accels
  - Subtract a moving average/bias (gravity) 
