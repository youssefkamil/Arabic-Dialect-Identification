# Arabic-Dialect-Identification

## This Repo contains 5 Main things :

- Data fetching 
- Data pre-processing 
- ML Models Training 
- DL Models Training
- Deployment with Flask 
- Demo GIF

# 1- Data Fetching [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)]( https://colab.research.google.com/drive/1cDgxXtVWdJKkqOvd2mSakJzxKNsxh5Dx?usp=sharing )

- Using **requests** to request the data with **id** column -which was given- by **POST** request
- Save fetched data with its dialect labels as ***tweetsWithLabels.csv***

# 2- Data pre-processing [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)]( https://colab.research.google.com/drive/1VRdMDWtpIJmac4yy4xkSNZNAl6QGVITb?usp=sharing ) 

### This notebook consist of : 
- remove_emoji(text) function
- Two approaches of pre-processing
- explore the most common words in each country
- prepare the QADI test-set  


# 3- ML Models Training [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1D64JrprT8z1RNA52ihh6j1soejs_yboF?usp=sharing) 
### This notebook consist of : 
- Load cleaned data-set
- CountVectorizer
- TFIDF
- Mazajak



# 4- DL Models Training [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13BDdtJ8j2vQIp5eErL3Xgfg9NAJ7KJ6D?usp=sharing ) 
### This notebook consist of : 
- Load cleaned data-set
- AraBERTv2-base with ktrain **( best Results )**
- AraBERTv2-base with PyTorch 

# 5- Deployment with Flask
### in this folder you found : 
- **ktrain with flask.py** for loading pretrained ktrain model add deal with flask
- **AraBERTpreprocess.py** for pre-processing
- **templates/prediction.html** to get inputs
- **templates/Result.html** to display the post-procssing and prediction result
- **static/base.css** 

# 6- Demo

![2022-03-14-10-53-09](https://user-images.githubusercontent.com/37241010/158138839-48316c6f-426d-443e-8bc1-a6ca1302f663.gif)
