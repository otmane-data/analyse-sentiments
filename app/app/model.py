from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
import logging
import os
model_path = os.path.join(os.path.dirname(__file__), 'final_nb_pipeline.joblib')
model = joblib.load(model_path)

# Load the model
# model = joblib.load('app/final_nb_pipeline.joblib')

# Define class names
class_names = np.array(['negative', 'positive'])  # Assuming 0 is negative and 1 is positive

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
def read_root():
    return {'message': 'analyse_sentiment model API'}

@app.get('/testing')
def testmethod():
    return {'message': 'analyse_sentiment model API'}

@app.post('/recommend')
def recommend(data: dict):
    """
    API endpoint to determine whether a hotel is recommended based on comments.
    """
    try:
        # Extract sentences from the input data
        sentences = data.get('sentences', None)
        if not sentences:
            raise HTTPException(status_code=400, detail="Key 'sentences' not found in input data")
        
        # Make predictions
        predictions = model.predict(sentences)
        
        # Map predictions to class names
        predicted_labels = class_names[predictions]
        
        # Count positive and negative comments
        positive_count = int(np.sum(predicted_labels == 'positive'))
        total_count = len(sentences)
        positive_percentage = (positive_count / total_count) * 100
        
        # Determine recommendation status (e.g., threshold: 70% positive comments)
        is_recommended = positive_percentage >= 70
        
        # Log the results
        logger.info(f"Positive comments: {positive_count}/{total_count} ({positive_percentage:.2f}%)")
        
        return {
            'total_comments': total_count,
            'positive_comments': positive_count,
            'positive_percentage': positive_percentage,
            'is_recommended': is_recommended
        }
    
    except Exception as e:
        logger.error(f"Error during recommendation analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))
