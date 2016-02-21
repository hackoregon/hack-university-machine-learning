# Measuring Performance

The most important algorithm in a machine learning system is the model performance evaluation "algorithm."

If you don't know how good your prediction is likely to be, then you don't know whether you need to try to tune or change your machine learning algorithm.

[This medium article by  Tavish Srivastava](http://www.analyticsvidhya.com/blog/2016/02/7-important-model-evaluation-error-metrics/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29) has a good explanation of some important performance metrics.

- RMSE: Root Mean Squared Error
  - works for both continuous values (regression) and categorical (classification)
- Confusion Matrix
  - works for both continuous values (regression) and categorical (classification)
  - several scalar "summary" metrics are possible
    - sensitivity
    - specificity
    - Mathews Correlation Coefficient (Phi)
      - equivalent to classical Pierson Correlation Co
- Gain and Lift
  - often used in A/B testing and marketing campaign planning
- Kolmogorov Smirnov
  - requires a continuous score and a classification label
    - can threshold a regression problem to create arbitrary classes to use with K-S metric
  - separation or difference between two distributions
- Area Under the ROC Curve
  - ROC: Radio Operating Characteristic (from information theory)
- Gini Coefficient
- Concordant/Discordant ratio

## Performance Metrics

### RMSE

`np.sqrt(np.mean((predicted_value - true_value) ** 2))

This is the *1-sigma* error typically reported along with predictions. When people report a range of possible outcomes they typically multiple the 1-sigma value by 3 to get a *3-sigma* range that the outcome has a 99% chance of falling within.

This is what most people think of as error, such as when people are reporting values like [Gallup pole predictions](http://www.gallup.com/poll/158519/romney-obama-gallup-final-election-survey.aspx) of the presidential election last year: "Romney 49%, Obama 48% in Gallup's Final Election Survey... margin of error +/- 2%." [Obama won that election 51% to 47%](http://uselectionatlas.org/RESULTS/national.php) through [use of Machine Learning](https://www.technologyreview.com/s/509026/how-obamas-team-used-big-data-to-rally-voters/) to target the right states during the campaign. Dan Wagner, Obama's chief data scientist, put together a team of coders to help win the election. His algorithms and error metrics were better than Gallup's and the Romney campaign's.

Gallup's error was right at the edge of their predicted accuracy range, indicating that their error metric was probably inadequate. It didn't gage the true unpredictability of American voters in a close race well at all. But this isn't a fair criticism, because Gallup wasn't making a prediction of the election outcome or estimating the error in their prediction, but merely reporting the error range of the poll they took. They did radically adjust their polling procedures in 2012 as a result of this "outlier" result, though.

## Confusion Matrix

A [confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) is just a truth table of matches and mismatches between a set of classifications. So it's often called:

-  contingency table (or matrix)
-  error matrix
-  agreement matrix ? (my own positive spin on "confusion")

(TODO: Example Graphic or Whiteboard Drawing here)

## [Project](../../huml/day2/)

### Confusion Matrix

See if you can build a confusion matrix.
Work your way from top to bottom with this feature set.

- Binary classification
  - matrix/dataframe with 4 values TP, TN, FP, FN
- Multiple Category Classification
  - NxN table of hits/misses in classification
- Aggregate statistics methods
- AUC (Area Under the Curve)

