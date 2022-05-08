# PyLucene Project
This project is part of the Modern Data Science Systems (DSBA 6345) course from University of North Carolina at Charlotte. This project is for installing and setting up PyLucene on Windows using Docker. 

## Team Members
- Shashank Khot
- Vathsavi Venkat

## Installation steps
The steps to install, setup and test successfull installation of Lucene can be found here: [Instructions](https://github.com/Vathsavi-Venkat/DSBA6345-PyLucene/blob/main/Instructions/Install%20and%20set%20up%20PyLucene%20using%20Docker.pdf)

## Setup VS Code to run the project
The steps to setup VS Code for this project can be found here: [Instructions](https://github.com/Vathsavi-Venkat/DSBA6345-PyLucene/blob/main/Instructions/Setup%20Steps.pdf)

## Steps to execute the project
The following are the steps to execute the project. The steps can also be found here: [Instructions](https://github.com/Vathsavi-Venkat/DSBA6345-PyLucene/blob/main/Instructions/Project%20Run%20Steps.pdf)
1. To run the index file on the terminal, type the command:
    ```bash
    python /home/Lucene/IndexFiles.py /home/Data
    ```
   Once the index has been created, you should see "done" and the time it took to create the index.
2. Next, we can try searching on the indexes. On the terminal, type the command:
   ```bash
    python /home/Lucene/SearchFiles.py
    ```
    We can use single word query, "multi word query", and logical operators (AND, OR, NOT) while searching.
 
 
3. To run the new index file on the terminal, type the command:
    ```bash
    python /home/Lucene/FieldIndex.py /home/DataNews
    ```
   Once the index has been created, you should see "done" and the time it took to create the index.
4. Next, we can try searching on the new set of indexes. On the terminal, type the command:
   ```bash
    python /home/Lucene/FieldSearch.py
    ```
    Similarly, we can use single word query, "multi word query", and logical operators (AND, OR, NOT) while searching. Some examples of the query types can be found here: [Query Types](https://github.com/Vathsavi-Venkat/DSBA6345-PyLucene/blob/main/Instructions/Query%20Types%20Examples.pdf)
    Since, we created index based on fields as well, we can index on the fields as well. For example,
    
   a) From field:
```bash
from_:"Amanda"
```
   b) Subject field:
```bash
subj:"Cryptography"
```
    
   c) Document ID:
```bash
doc_id:"12345"
```
