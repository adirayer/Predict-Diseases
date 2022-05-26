from keras.models import load_model
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

## Load the models

diabetes_model=pickle.load(open('/home/aditya/Desktop/AR/Multiple Disease Prediction/Diseases/Models/diabetesmodel.sav','rb'))
heart_model=pickle.load(open('/home/aditya/Desktop/AR/Multiple Disease Prediction/Diseases/Models/heart_disease_model.sav','rb'))
parkinson_model=pickle.load(open('/home/aditya/Desktop/AR/Multiple Disease Prediction/Diseases/Models/parkinsons_model.sav','rb'))
cancer_model=load_model('/home/aditya/Desktop/AR/Multiple Disease Prediction/Diseases/Models/cancer.h5')

#sidebar for navigation
with st.sidebar:
    selected=option_menu('Disease Prediction System',
    ['Predict Diabetes',
    'Predict Heart Disease',
    'Predict Parkinsons Disease',
    'Predict Breast Cancer'],
    icons=['activity','heart','file-person-fill','journal-medical'],
    default_index=0)

# Diabetes Prediction Page
if (selected == 'Predict Diabetes'):
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')    
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    # code for Prediction
    diab_diagnosis = ''
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'     
    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Predict Heart Disease'):
    # page title
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')    
    with col2:
        sex = st.text_input('Sex')    
    with col3:
        cp = st.text_input('Chest Pain types')   
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')  
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')    
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')  
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    # code for Prediction
    heart_diagnosis = ''
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'       
    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if (selected == "Predict Parkinsons Disease"):
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)  
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')    
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')      
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')       
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')      
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')  
    with col1:
        RAP = st.text_input('MDVP:RAP')   
    with col2:
        PPQ = st.text_input('MDVP:PPQ')     
    with col3:
        DDP = st.text_input('Jitter:DDP')    
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')   
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')    
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5') 
    with col3:
        APQ = st.text_input('MDVP:APQ') 
    with col4:
        DDA = st.text_input('Shimmer:DDA') 
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')  
    with col2:
        RPDE = st.text_input('RPDE')   
    with col3:
        DFA = st.text_input('DFA') 
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2') 
    with col1:
        D2 = st.text_input('D2') 
    with col2:
        PPE = st.text_input('PPE')
    
    # code for Prediction
    parkinsons_diagnosis = ''
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"   
    st.success(parkinsons_diagnosis)


# Breast Cancer Prediction Page
if (selected == "Predict Breast Cancer"):
    # page title
    st.title("Breast Cancer Prediction using ML")
    col1, col2, col3, col4, col5 ,col6= st.columns(6)  
    with col1:
        meanradius= st.text_input('Mean Radius')    
    with col2:
        meantexture = st.text_input('Mean Texture')      
    with col3:
        meanperimeter = st.text_input('Mean Perimeter')       
    with col4:
        meanarea = st.text_input('Mean Area')      
    with col5:
        meansmoothness = st.text_input('mean smoothness')  
    with col6:
        meancompactness = st.text_input('Mean Compactness')    
    with col1:
        meanconcavity = st.text_input('Mean Concavity')       
    with col2:
        meanconcavepoints = st.text_input('Mean Concave Points')     
    with col3:
        meansymmetry = st.text_input('Mean Symmetry')    
    with col4:
        meanfractaldimension= st.text_input('Mean Fractal Dimension')     
    with col5:
        radiuserror = st.text_input('Radius Error')  
    with col6:
        textureerror = st.text_input('Texture Error')  
    with col1:
        perimetererror = st.text_input('Perimeter Error')  
    with col2:
        areaerror = st.text_input('Area Error')   
    with col3:
        smoothnesserror= st.text_input('Smoothness Error')  
    with col4:
        compactnesserror= st.text_input('Compactness Error')   
    with col5:
        concavityerror = st.text_input('Concavity Error')     
    with col6:
        concavepointserror = st.text_input('Concave Points Error')   
    with col1:
        symmetryerror = st.text_input('Symmetry Error')  
    with col2:
        fractionaldimensionerror = st.text_input('Fractal Dimension Error')   
    with col3:
        worstradius = st.text_input('Worst Radius')   
    with col4:
        worsttexture = st.text_input('Worst Texture')  
    with col5:
        worstperimeter = st.text_input('Worst Perimeter')  
    with col6:
        worstarea = st.text_input('Worst Area')  
    with col1:
        worstsmoothness = st.text_input('Worst Smoothness')  
    with col2:
        worstcompactness = st.text_input('Worst Compactness')  
    with col3:
        worstconcavity = st.text_input('Worst Concavity')  
    with col4:
        worstconcavepoints = st.text_input('Worst Concave Points')  
    with col5:
        worstsymmetry = st.text_input('Worst Symmetry')  
    with col6:
        worstfractaldimension = st.text_input('Worst Fractal Dimension')  
    # code for Prediction
    breast_diagnosis = ''
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        cancer_prediction = cancer_model.predict([['meanradius','meantexture','meanperimeter','meanarea'
'meansmoothness',
'meancompactness',
'meanconcavity',
'meanconcavepoints',
'meansymmetry',
'meanfractaldimension',
'radiuserror',
'textureerror',
'perimetererror',
'areaerror',
'smoothnesserror',
'compactnesserror',
'concavityerror',
'concavepointserror',
'symmetryerror',
'fractaldimension error',
'worstradius',
'worsttexture',
'worstperimeter',
'worstarea',
'worstsmoothness',
'worstcompactness',
'worstconcavity',
'worstconcavepoints',
'worstsymmetry',
'worstfractaldimension',
]])                          
        
        if (cancer_prediction[0] == 1):
          breast_diagnosis = "The Tumer is Malignant "
        else:
          breast_diagnosis = "The Tumer is Benign"   
    st.success(breast_diagnosis)