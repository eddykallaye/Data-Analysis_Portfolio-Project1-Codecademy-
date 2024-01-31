Comprehensive Insurance Dataset Analysis Project
Introduction
This Jupyter Notebook embarks on a comprehensive analysis of the "insurance.csv" dataset, with a primary focus on comparing insurance costs between smokers and non-smokers. The dataset encompasses seven columns:

Age: Integer representing the age of the insured. Sex: String indicating the gender of the insured (male/female). BMI: Float representing the Body Mass Index of the insured. Children: Integer indicating the number of children/dependents covered by the insurance. Smoker: Boolean value specifying whether the insured is a smoker (yes/no). Region: String denoting the region of the insured. Charges: Float representing the insurance charges.

Project Scope and Goals
Average Age Calculation: Determine the average age of the patients in the dataset.

Gender Distribution: Return the count of males and females present in the dataset.

Geographical Analysis: Identify the geographical distribution of patients based on their regions.

Average Yearly Medical Charges: Calculate and return the average yearly medical charges incurred by the patients.

Insurance Cost Comparison:

Calculate the average insurance charges for male smokers. Calculate the average insurance charges for male non-smokers. Calculate the average insurance charges for female smokers. Calculate the average insurance charges for female non-smokers. Compare insurance costs between male smokers and male non-smokers. Compare insurance costs between female smokers and female non-smokers.

Implementation Details
To perform these inspections,define a class named PatientsInfo, containing five methods:

analyze_ages(): Calculates the average age of the patients. analyze_sexes(): Returns the count of males and females in the dataset. unique_regions(): Identifies the unique geographical regions represented in the dataset. average_charges(): Calculates and returns the average yearly medical charges incurred by the patients. insurance_cost_comparison(): Compares insurance costs between male smokers, male non-smokers, female smokers, and female non-smokers.

This comprehensive analysis aims to provide detailed insights into various facets of the dataset. By focusing on demographic distribution, regional representation, and tailored comparisons of insurance costs based on gender and smoking habits, the analysis offers a comprehensive exploration of the dataset. The PatientsInfo class facilitates the execution of these operations, enhancing the overall understanding of the dataset.
