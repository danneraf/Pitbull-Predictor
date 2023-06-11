# <img src="https://m.media-amazon.com/images/I/61WHhsyhStL.jpg" width="55" height="55"> READ ME: Pitbull Predictor
#### Dale


### Contents: 
![Pitbull File Organization](./Images/file.JPG)

- [Introduction](#Introduction)
- [Problem Statement](#Problem-Statement)
- [Data](#Data)
- [Methods](#Methods)
- [Outcome](#Outcome) 
- [Examples](#Examples) 

### Code Contents (In Order)
1. [Pitbull Data Collection](./Data/Pitbull.ipynb)
2. [Not Pitbull Data Collection](./Data/Not_Mr_Worldwide.ipynb)
3. [Data to CSV](./Data/Data_to_CSV.ipynb)
4. [Cleaning](./Code/Cleaning.ipynb) 
5. [Modeling](./Code/Modeling.ipynb)
6. [Pitbull Lyrics to TXT File](./Code/Pit_to_txt.ipynb)
7. [GPT](./Code/GPT.ipynb)

## Introduction
Pitbull, the enigmatic rapper and musical prodigy, possesses an unparalleled magnetism that has captivated millions around the globe. With his infectious beats, electrifying stage presence, and dynamic persona, Pitbull has carved a legendary status in the world of music. His unique fusion of hip-hop, dance, and rhythms has revolutionized the industry, igniting a fire in the hearts of fans everywhere. Pitbull's lyrics are an embodiment of his larger-than-life personality, showcasing his ability to effortlessly blend wit and charm. The sheer impact of his music on the cultural landscape makes it undeniable that a Pitbull lyric generation model is an absolute necessity.

The need for a Pitbull lyric generation model stems from the immense influence and impact that Pitbull's music has had on popular culture. His lyrics serve as anthems of empowerment, unifying people from diverse backgrounds through their universal themes of celebration, resilience, and ambition. Pitbull's unparalleled ability to craft infectious hooks and memorable one-liners has made him a force to be reckoned with in the music industry. A Pitbull lyric generation model would not only honor his legacy but also provide a platform for fans and aspiring artists to channel their creativity and express themselves in the unique style that Pitbull has popularized.

Imagine a world where the spirit of Pitbull's music can be channeled at the touch of a button. A Pitbull lyric generation model would unlock a realm of limitless possibilities, allowing fans and artists alike to tap into the essence of Pitbull's genius. From creating catchy hooks that get stuck in your head to penning verses that embody the pulse of the streets, this model would empower users to generate Pitbull-style lyrics that resonate with the energy and vibrancy that defines his music. The impact of such a tool would be immeasurable, sparking a wave of creativity and fostering a community where the spirit of Pitbull lives on through the lyrics of his devotees.

"This for everybody going through tough times

Believe me, been there, done that

But every day above ground is a great day, remember that

Dale"
- *Time of Our Lives, Pitbull* 

![Pitbull Generator](./Images/livelaughlove.JPG)

## Problem Statement

**Can we utilize advanced natural language processing models to fix the lack of effective and creative solutions for generating Pitbull lyrics? This project seeks to provide users with a powerful tool to generate captivating lyrics that closely resemble the style, energy, and vocabulary of Pitbull's music.** 

![for him](./Images/doit.JPG)

## Data
The [Data](./Data) folder contains the data that was collected using [LyricsGenius](https://pypi.org/project/lyricsgenius/), a Python client for Genius.com's API. 672 songs and their lyrics were originally downloaded for Pitbull and 590 songs and their lyrics were originally downloaded for other artists, including artists similar and dissimilar to Pitbull. After cleaning, 671 Pitbull songs and 587 non-Pitbull songs were remaining. The lyrics were originally collected in JSON format, then transformed to CSV and TXT for modeling and training. 

## Methods 
[BERT](https://huggingface.co/docs/transformers/model_doc/bert) (Bidirectional Encoder Representations from Transformers) is a highly advanced natural language processing (NLP) model. It utilizes a transformer-based architecture and is pre-trained on vast amounts of text data, enabling it to understand language context and achieve impressive performance on various NLP tasks. 

[GPT](https://huggingface.co/distilgpt2) (Generative Pre-trained Transformer) is a language model that generates human-like text based on pre-training on large text datasets, allowing it to produce coherent and contextually relevant text given a specific input or prompt.

A pre-trained BERT model and GPT model were imported from [Hugging Face](https://huggingface.co), a company largely focused on machine learning.

The BERT and GPT models were imported, trained on the lyric data, and then used in a Streamlit application where users can input text for thr GPT model to then generate corresponding Pitbull lyrics. The generated lyrics are then scored by the BERT model to determine how similar they are to actual Pitbull lyrics. 


## Outcome
The Pitbull Lyrics Generator is a fun application that generates Pitbull lyrics based on user input. It utilizes the power of machine learning models to generate lyrics in the style of the rapper and musical genius Pitbull, also known as Mr. Worldwide. The application combines two pre-trained models, GPT-2 and BERT, to generate and classify the lyrics. Users are provided generated life-changing Pitbull lyrics and a score assuring them how similar the lyrics are to actual Pitbull lyrics, determined by a model with over 91% accuracy. Users can rest assured that they will receive only the best GPT generated Mr. Worldwide lyrics possible. 


## Examples





## Features

- User-friendly interface: Simply enter a starting line or a few lyrics, and the application will generate Pitbull-style lyrics based on the input.
- Generated Lyrics: The application displays the generated lyrics, giving you a taste of Pitbull's unique style.
- Score: The generated lyrics are classified using a BERT model, providing a score that represents how Pitbull the lyrics are.
- Artist Collaboration: The application also allows users to decide if an artist should feature Pitbull by entering the artist's name.

## Installation

To run the Pitbull Lyrics Generator application, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/danneraf/Pitbull-Predictor.git 
   ```

2. Navigate to the project directory:

   ```
   cd Pitbull-Predictor
   ```

3. Install the required dependencies:

   ```
   pip install (required libraries)
   ```

4. Run the application in your terminal:

   ```
   streamlit run pitpred.py
   ```


## Using the App 

insert screenshot 

1. Enter a starting line or a few lyrics in the text input box.
2. Click the "Dale!" button to generate Pitbull lyrics based on your input.
3. The generated lyrics will be displayed, along with a score indicating how 305 the lyrics are.
4. You can also enter the name of an artist in the text input box and click the "?" button to find out if they should feature Pitbull.

## Credits

This project was inspired by [this GitHub repository](https://github.com/ffomezolam/GA-DSI-Capstone/tree/main) and built using the following technologies and libraries:

- LyricsGenius: [Instructions to download](https://pypi.org/project/lyricsgenius/)
- Genius API token: [Instructions to obtain](https://docs.genius.com/#/getting-started-h1)
- Streamlit: [Instructions to download](https://docs.streamlit.io/library/get-started/installation)
- Transformers: [Instructions to download](https://huggingface.co/docs/transformers/installation)
- TensorFlow: [Instructions to download](https://pypi.org/project/tensorflow/)
- PyTorch: [Instructions to download](https://pytorch.org/get-started/locally/)

This project uses Hugging Face's [DistilGPT2](https://huggingface.co/distilgpt2) model for lyric generation and [BERT](https://huggingface.co/docs/transformers/model_doc/bert) model for classification. 

## Drawbacks 

As with most projects, this project came with some downfalls and setbacks: 

1. My own bias - I chose the other artists used for training, which could effect the outcome of the accuracy and training of the model.
2. [Genius.com lyric accuracy](https://genius.com/Genius-how-genius-works-annotated) - Genius seems to rely on users to report lyrics and add what songs belong to artists. Two times I noticed innacuracies in songs when collecting lyrics were when a short, random rap verse was labeled under Pitbull, when it did not appear to involve him at all, then again when collecting songs for Elton John and it tried to include "All of the Lights" by Kanye West. 
3. Time frame songs were released - I believe the songs collected were decently mixed to have songs from the same time frame Pitbull's songs were released to ensure the models were truly having to work to tell the difference. If all off the songs were from before Pitbull started his career, certain phrases and cultural references would have been picked up on more by the models, so when trying to tell the difference between Pitbull and a similar artist would be much less accurate for the model. 
4. Spanish - Similar to the previous point, I had to ensure I included artists with Spanish lyrics to make the model more reliable. Another downfall with this, though, is that the DistilGPT2 model is trained on English, potentially making the lyric generation not as great as it could be.
5. Not enough data - More media would make this project yield better results for classification and lyric generation. Please call your local Pitbull representative to request more Pitbull songs. 
6. Features - I included features when collecting Pitbull's songs, as most of his songs are from features, but I excluded features for other artists to reduce the chance of a Pitbull song getting pulled in their data. A few songs featuring Pitbull were able to make it through (and dropped). This goes back to Genius relying on users to create this data as well. How accurate is the data provided, how do we know more Pitbull features did not fall through the cracks and into the data for the other artists? 
7. Cleaning lyrics - Due to including Pitbull features, I wanted to isolate his lyrics in songs, which did not work out as well as hoped. Some non-Pitbull lyrics still made it through. Lyrics generated so far still sound very Pitbull and the models are able to accurately classify Pitbull lyrics, but the results could be significantly more accurate if given more time and resources for data cleaning.
8. Time - The models used take a few hours to run. More effecient models, a longer time frame, or more resources would help in making this project more accurate.  


## Acknowledgments

- Special thanks to the creators of the pre-trained models used in this project, as well as the open-source community for their contributions. Also, a thank you to those that have made projects modeling [Shakespeare](https://github.com/KenyaChauche/sonnet-generation/tree/master). To me, Pitbull is the Shakespeare of our generation. 
- Thank you to my instructors for their guidance and support! 


![Capstone](./Images/capstone.jpg)


![Hank](./Images/hank.jpg)


#### Me now, because of this project: 

![pics](./Images/pics.JPG)


## In the End, 

![hope](./Images/hope.jpg)
