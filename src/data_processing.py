import cv2
import numpy as np
import pandas as pd
import os
import rawpy
from src.utils import calculate_ita

BLUR_THRESHOLD = 100 # Rule-of-thumb: variance of Laplacian

def dng_to_jpg_conversion(dng_path, jpg_path):
    """Converts a raw DNG image to a standard JPG file."""
    try:
        with rawpy.imread(dng_path) as raw:
            rgb = raw.postprocess() # Process and convert to RGB
            cv2.imwrite(jpg_path, cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))
            return True
    except Exception as e:
        print(f"Error processing {dng_path}: {e}")
        return False

def check_blurriness(frame):
    """Uses the Laplacian variance to check if a frame is blurry."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # The variance of the Laplacian measures image sharpness
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var >= BLUR_THRESHOLD

def extract_key_frames(video_path, output_dir, time_interval_sec=3):
    """
    Extracts sharp, non-redundant frames from a video based on a time interval
    and a blur check.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return []

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * time_interval_sec)
    frame_count = 0
    saved_frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            if check_blurriness(frame):
                # Placeholder for face/skin segmentation before saving
                # skin_region = segment_skin(frame) 
                
                frame_name = f"{os.path.basename(video_path).split('.')[0]}_f{frame_count:04d}.jpg"
                output_path = os.path.join(output_dir, frame_name)
                cv2.imwrite(output_path, frame)
                saved_frames.append(output_path)
        
        frame_count += 1

    cap.release()
    return saved_frames

def segment_skin(frame):
    """
    Placeholder for skin detection using MediaPipe or other CV techniques.
    Goal: Isolate the cheeks/forehead area to calculate mean skin color.
    """
    # ... Implementation using Mediapipe Face Mesh or color-based segmentation
    return frame # returns the cropped/segmented skin area

def calculate_mean_ita_from_image(image_path):
    """Loads image, segments skin, and calculates the mean ITA value."""
    img = cv2.imread(image_path)
    if img is None:
        return None
        
    # 1. Skin Segmentation & Cropping (essential for accuracy)
    skin_region = segment_skin(img) # Needs to be implemented properly

    # 2. Get the average BGR value (OpenCV uses BGR)
    mean_bgr = np.mean(skin_region.reshape(-1, 3), axis=0)
    
    # 3. Convert BGR (OpenCV) to RGB (for ITA calculation)
    mean_rgb = mean_bgr[[2, 1, 0]]
    
    # 4. Calculate ITA
    ita = calculate_ita(mean_rgb)
    return ita

# --- Main Data Processing Script ---
def process_mste_dataset(raw_dir, processed_dir):
    """
    Orchestrates the entire MSTE data processing pipeline.
    """
    print("Starting MSTE Dataset Processing...")
    
    # Ensure output directories exist
    os.makedirs(processed_dir, exist_ok=True)
    
    # Collect metadata for the final skin_tone_labels.csv
    metadata = []
    
    # Logic to iterate through subjects, convert DNG, extract keyframes, 
    # calculate ITA, and save the results.
    # ... (This is where the main loop and file logic will go)
    
    # Example logic snippet:
    for subject_folder in os.listdir(raw_dir):
        # ... logic to find DNGs and videos
        pass

    # Save final metadata
    df = pd.DataFrame(metadata)
    df.to_csv(os.path.join(processed_dir, 'skin_tone_labels.csv'), index=False)
    print(f"Processing complete. Metadata saved to {os.path.join(processed_dir, 'skin_tone_labels.csv')}")

if __name__ == '__main__':
    # Define your local paths here to run the script
    # process_mste_dataset('/path/to/MSTE_raw', 'data/')
    print("Run process_mste_dataset(raw_dir, processed_dir) to begin pipeline.")
