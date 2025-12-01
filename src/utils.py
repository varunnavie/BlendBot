import numpy as np
from skimage import color # Using scikit-image for color space conversion

def calculate_ita(rgb_array):
    """
    Calculates the Individual Typology Angle (ITA) from a mean RGB value.
    ITA is calculated from the CIELAB L* (lightness) and b* (yellowness) channels.

    Args:
        rgb_array (np.array): A 3-element NumPy array of mean RGB values (0-255).

    Returns:
        float: The ITA value in degrees.
    """
    if rgb_array.shape != (3,):
        raise ValueError("Input array must be a 3-element array (R, G, B).")

    # 1. Convert RGB (0-255) to CIELAB (L*, a*, b*)
    # scikit-image color.rgb2lab expects RGB in range [0, 1]
    rgb_normalized = rgb_array / 255.0

    # Ensure the input has the correct dimension for conversion (1 pixel)
    rgb_reshaped = np.array([rgb_normalized]) 
    
    lab = color.rgb2lab(rgb_reshaped)[0]
    
    L_star = lab[0]
    b_star = lab[2]

    # 2. Apply the ITA formula
    # ITA = (arctan ((L*-50)/b*) * 180) / pi
    
    # arctan2 is safer than arctan for handling signs
    ita_rad = np.arctan2(L_star - 50, b_star)
    ita_deg = (ita_rad * 180) / np.pi
    
    return ita_deg

def map_ita_to_fitzpatrick(ita_value):
    """
    Maps continuous ITA value to the discrete Fitzpatrick Skin Type (FST) scale.
    Standard mapping ranges used in dermatology and color science.
    """
    if ita_value > 55:
        return 1 # Very Light (Type I)
    elif ita_value > 41:
        return 2 # Light (Type II)
    elif ita_value > 28:
        return 3 # Intermediate (Type III)
    elif ita_value > 10:
        return 4 # Tan (Type IV)
    elif ita_value > -30:
        return 5 # Brown (Type V)
    else:
        return 6 # Dark (Type VI)

# Placeholder for other helper functions (e.g., lighting normalization matrix)
def normalize_lighting(img):
    """Placeholder: Applies white balancing or light normalization."""
    # Implementation will involve advanced CV techniques or learned models.
    return img
