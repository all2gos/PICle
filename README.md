# PICle

PICle (which stands for Procedure to Indicate CLuster Energy) is a code for predicting the energy of clusters composed of copper and nickel using machine learning methods and only geometrics descriptors to train. The repository consists of 3 segments:

- Files used to create the test collection (catalog *creating_data_sets*)
- CSV files contain train/test set (*my_e.csv*), validation set (*clusters_phd.csv*) and the common part of both these files (*phd_common_part_csv*)
- *ML.ipynb* in which we carry out the entire procedure of machine learning, validation and visualization of the results

The entire machine learning procedure is carried out using the scikit-learn library and involves the use of simple techniques. The resulting models are saved using the joblib library.

The entire project has proof of concept status and the conclusions of the research conducted for it will be published in the near future in the form of a scientific article.

The main idea behind this project is to design a tool that can significantly speed up the time of determining the energy of numerous groups of structures. In situations such as the issue of *catalyzing CO2 reduction with nickel-added copper clusters*, the nature of the phenomenon is not well understood as well as the number of potential structures needed to be investigated is disproportionately large. Therefore, the most sensible idea at the present time is to use a technique that will probably not provide us with results with DFT-level accuracy, but will allow us to roughly determine the small fraction of cases from the study group that shows the greatest catalytic potential.

And after such a reduction, as long as the prediction accuracy is not satisfactory (the model achieves an average accuracy of ~0.3 eV) it is possible to optimize the most attractive structures, however, in an incomparably shorter time by reducing the size of the test set. 

The main motivation of the project is to reduce time as much as possible, so we use a number of approximation techniques in the project, for example we do not optimize structures and only determine Single Point Energy. What is very important for us, we do not use descriptors, the acquisition of which would either require optimization of the structure (which would be a contradiction of the whole idea) or those that come from external databases (such descriptors, in turn, would force us to limit ourselves only to structures that have been previously described by someone else, synthesized or we would have to make such classification ourselves). 

As a result, we propose a tool, or rather a certain way of doing preliminary research, that is as fast as possible and what we believe (we haven't proved it yet) as transposable, as possible to any set of structures. 
