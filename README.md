# BV system automatic entry software
#### Video Demo: https://youtu.be/nzOI12yFIts
#### Description: This software is developed for the data entry process.

## 1. Background of the assembly drwaing
Assemblies are the combination of parts and sub-assemblies.

Here is one example assembly drawing.

<img src="https://user-images.githubusercontent.com/92499776/203812496-49a03e48-df6e-4d8d-ae59-13444e3286c7.png" width="500">

The Top assembly is made by many sub-assemblies and one of the subassemblies (item 4 X1610-C9081-BD) is shown below.
In the subassembly (X1610-C9081-BD), there are also two assemblies (X0510-C9081-QC and X461A-C9081-PZ)

<img src="https://user-images.githubusercontent.com/92499776/203812563-1cd5949e-6c86-4335-8a68-a6a5a407b916.png" width="500">

The below part is X0510-C9081-QC which is sub-part of X1610-C9081-BD and shown below.

<img src="https://user-images.githubusercontent.com/92499776/203812696-5cbba419-082d-4570-b501-bc8bce800aab.png" width="500">


The naming system of the part number is shown in the below table.


<img src="https://user-images.githubusercontent.com/92499776/203813166-5d5d8c2d-f58d-43c9-b74f-c0e3981209e8.png" width="500">

X05 is the flat part that will be processed with laser cutting.

<img src="https://user-images.githubusercontent.com/92499776/203813699-f0418f1e-09d1-4ad7-be4a-1bab1304ba2f.png" width="500">

X46 is the bent/ rolled part that will be processed with pressing machine.

<img src="https://user-images.githubusercontent.com/92499776/203813574-f25f2db1-062a-4579-b718-057b45264a7d.png" width="500">

X16 is the assembly part which will be assembled in our shop.


<img src="https://user-images.githubusercontent.com/92499776/203813846-dc38dcd2-a296-4e4d-a4d2-2fa1e5ec48a7.png" width="500">



## 2. Entering manufacturing part info to the Business vision software.
This is the most time-consuming part of the design. All information created in the modeling software or in the drawing would be manually input into the software for organizing the manufacturing process.

<img src="https://user-images.githubusercontent.com/92499776/203814060-1049ce47-9d0f-4237-a6ef-fc89c61105d7.png" width="100">


<img src="https://user-images.githubusercontent.com/92499776/203814082-74ef67c8-c049-493c-96c5-bb9070a3f644.png" width="700">


For saving time, I developed this software to input the software into business vision software. at first, the software will grab all the required information from the pdf files and store it in the data.csv Then, it will automatically input the collected data into company software.

the program logic flowchart is listed below.

<img src="https://user-images.githubusercontent.com/92499776/203699207-c45f024a-0a64-4919-9f70-3681ae61edff.png" >

## 3. Demostration

Here is the running example for a small size assembly. 

<img src="https://user-images.githubusercontent.com/92499776/203812496-49a03e48-df6e-4d8d-ae59-13444e3286c7.png" width="500">

All the pdf design information stored in data.csv and sub.csv

<img src="https://user-images.githubusercontent.com/92499776/203903949-c595a9d0-b77e-4946-ad0b-74b2358402e9.png" width="500">

<img src="https://user-images.githubusercontent.com/92499776/203904009-6cbdbfd9-0404-40d1-8459-82dc19960190.png" width="500">

As all the information are already inputted previously, at the end it showed all inventory already exsisted and compeleted.

<img src="https://user-images.githubusercontent.com/92499776/203849780-4d379b25-7ac5-41c7-a992-0240451c6177.png" width="500">

<img src="https://user-images.githubusercontent.com/92499776/203849952-a1716c6f-07c5-45dc-8366-c7f5ff98b6cf.png" width="500">

Thank you.
