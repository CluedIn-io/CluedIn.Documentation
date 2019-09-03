Data Metrics

Data Metrics will allow you to score and monitor the history of data quality over time. Data Metrics are aggregated on many different levels and you might find that you need to control how that aggregation is done at each level. 

At the core of the Metrics are a way to calculate different types of scores given certain data values. This could be in the form of a percentage between 0 and 100, a simple integer or something more advanced. Most of the out of the box data metrics to do with Data Quality are in the form of a percentage between 0 and 100. To date, we support:

Accuracy
Completeness
Relevance
Connectivity

To add new metrics, you will simply need to create a new C# class and inherit from Metric<Percentage>. You will then need to implement the calculation piece and the aggregation piece. It is always recommended that you will start calculation at the highest precision point possible i.e. Property History. It might not always be appropriate for you to calculate at this granularity level e.g. Connectivity is only calculated at the Entity level due the fact that you will most likely only be interested in knowing that after the Entity has been constructed, is it connected or not. 

There are other metrics, like Accuracy where we calculate down to the property history as we are wanting to measure how all permutations of a value correlate with each other. In some cases you might find that the parent levels of metrics are simply an average, mean or sum of the higher precision scores. In other cases you might find that you calculate a score differently at each level. 

