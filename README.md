 🚧 **Status: This is an active, ongoing project. Features and models are still under development.**  



<!--  Gradient Logo Title (SVG) -->
<p align="center">
  <svg width="420" height="120">
    <defs>
      <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#4a0900;stop-opacity:1" />
        <stop offset="50%" style="stop-color:#9b6a00;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#f5d9c7;stop-opacity:1" />
      </linearGradient>
    </defs>
    <text x="10" y="60" font-size="55" font-family="Georgia" font-style="italic" fill="url(#grad)">
      BlendBot
    </text>
    <text x="10" y="100" font-size="28" font-family="Arial" fill="#f5d9c7">
      Find Your Perfect Shade!
    </text>
  </svg>
</p>

<h1 align="center"> BlendBot — AI-Powered Foundation Shade Recommender</h1>

<p align="center">
BlendBot helps makeup beginners find their perfect foundation shade by analyzing skin tone and lighting conditions using AI.
</p>

---

#  Project Overview

BlendBot is an AI/ML–powered foundation shade recommender designed to help makeup beginners find their perfect foundation match with precision and ease.

By analyzing a user's skin tone and undertone from an uploaded image, BlendBot reduces mismatches, saves money, and offers professional-grade recommendations across brands such as **MAC**, **Fenty**, **Sugar**, and **Maybelline**.

It uses advanced **Computer Vision**, **Color Science**, and **ML regression models** to deliver accurate matches — even under imperfect lighting.

---

#  Scope

###  Help makeup beginners find the right foundation shade based on their skin tone and lighting  
###  User uploads a face image in good lighting; system analyzes skin tone  
###  Suggests closest matching shades from brands (Sugar, Maybelline, MAC, Fenty)  
###  Reduces product mismatches + unnecessary expenses  

---

# Core Features

###  1. Upload Photo / Live Camera Capture
Users can upload an image or capture directly using webcam.

###  2. Intelligent Lighting Normalization
Normalizes warm, cool, dim, and uneven lighting.

###  3. Precise Skin Region Detection
Uses **MediaPipe Face Mesh** to detect:
- cheeks  
- forehead  
- noise-free skin patches  
while excluding hair, lips, shadows, and edges.

###  4. Image Quality Control
Removes blurry or low-light images using:
- **Laplacian Variance Blurriness Detection**

###  5. Dual-Scale Skin Tone Classification
- **ITA (Individual Typology Angle)** — continuous tone scale  
- **Fitzpatrick Skin Type** — 6-level dermatology scale  

###  6. Shade Matching (ML + Product Data)
Matches skin tone to real foundation shades using:
- k-NN distance in ITA space  
- undertone classification  
- brand-specific shade metadata  

###  7. Shade Recommendations & Visualization
Shows:
- best match  
- 3 closest tones  
- optional simulated preview  

---

# ⚙️ Technical Implementation

### **ML Algorithm 1 — Skin Tone Classification (Regression)**
Predicts continuous ITA° directly from face images using a CNN.

### **ML Algorithm 2 — Foundation Shade Recommendation (k-NN / Distance Matching)**
Finds closest product shades using color + undertone similarity.

---

#  Datasets Used

| Dataset | Purpose | Source |
|--------|---------|--------|
| **MSTE Skin Tone Dataset** | Training CNN for ITA prediction | https://skintone.google/mste-dataset |
| **The Pudding Makeup Shades** | Real foundation shades + undertones | https://github.com/the-pudding/data/blob/master/makeup-shades/shades.csv |

---

#  Repository Structure

<pre>
BlendBot/
├── README.md                     
├── LICENSE                       
├── requirements.txt              
│
├── data/                         
│   ├── processed_shades.csv      
│   └── skin_tone_labels.csv      
│
├── notebooks/
│   ├── EDA_Data_Cleaning.ipynb   
│   └── Model_Training_v1.ipynb   
│
└── src/
    ├── data_processing.py        
    ├── ml_models.py              
    ├── utils.py                  
    └── app.py                    
</pre>

---

<h2> Installation & Usage</h2>

<h3>1. Clone the Repository</h3>
<pre>
git clone https://github.com/varunnavie/BlendBot.git
cd BlendBot
</pre>

<h3>2. Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3. Prepare the Data</h3>
<pre>
python src/data_processing.py
</pre>
<p>Then complete cleaning steps in <code>notebooks/EDA_Data_Cleaning.ipynb</code>.</p>

<h3>4. Train the Model</h3>
<pre>
jupyter notebook notebooks/Model_Training_v1.ipynb
</pre>

<h3>5. Launch the Application</h3>
<pre>
streamlit run src/app.py
</pre>

<br>

##  Project Status

BlendBot is currently **under active development**.  
Several modules (model training, shade mapping, full UI integration) are still being built and refined.  
Expect frequent updates!

<h2>🤝 Contributing</h2>
 🚧 **Status: This is an active, ongoing project. Features and models are still under development.**  
<p>All contributions are welcome! Feel free to open issues or pull requests.</p>

<br>

<h2> License</h2>
<p>This project is licensed under the <b>MIT License</b>.</p>

<br>

<h2> Contact</h2>
<p><b>Varunnavie T N</b><br>
GitHub: <i>https://github.com/varunnavie</i><br>

