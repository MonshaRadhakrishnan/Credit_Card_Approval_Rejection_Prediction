# Credit_Card_Approval_Rejection_Prediction
This project analyzes credit card approval data to understand key risk factors and build a predictive model for approval decisions. The goal is to reduce financial risk by minimizing false approvals while maintaining explainable and business driven insights.

Exploratory analysis was performed using Tableau for clear, stakeholder friendly visualizations, while machine learning models were built using Python.

**ML Model Results:**

<img width="424" height="305" alt="image" src="https://github.com/user-attachments/assets/9a09079e-32d6-4a25-9b07-198d37109a43" />

### my positive class is 1 and negative class is 0 here
### True negative = 21, False Positive = 5, False Negative = 1, True Positive = 4999
### Since this is a credit card approval problem, reducing false positives (5) is more important than reducing false negatives (1)
### Approving a credit card for a high-risk customer can result in financial loss, while rejecting a low-risk customer mainly leads to missed opportunity.
### So the model evaluation focuses more on Recall rather than overall accuracy
Going with Decision Tree and Random forest to improve RECALL thus reducing False Positives.

<img width="426" height="304" alt="image" src="https://github.com/user-attachments/assets/c5689a7d-3943-49c3-80df-09d81e9c9917" />
<img width="413" height="299" alt="image" src="https://github.com/user-attachments/assets/d7453442-edec-448d-86cb-c46e6ad2952f" />



**Detailed exploratory analysis and business insights were developed using Tableau, focusing on:**
Approval vs rejection trends
Segment wise risk analysis
Percentage based comparisons for decision making

**Tableau Dashboard link:**
https://public.tableau.com/app/profile/monisha.radhakrishnan/viz/Credit_Card_Approval_Dashboard/Dashboard1_1

**All Applicants:**

<img width="1885" height="877" alt="image" src="https://github.com/user-attachments/assets/1b8ad5a4-8941-45b9-935b-0099a939d1d4" />


**For Applicants having Good Debts**

<img width="1893" height="868" alt="image" src="https://github.com/user-attachments/assets/d41abdf5-33cf-4c16-84cb-8ce64b8c7562" />


**For Applicants having Bad Debts**

<img width="1896" height="876" alt="image" src="https://github.com/user-attachments/assets/2d064e2a-125e-457c-ad1b-866ba2c38648" />


