def calculate_bmi(weight, height_meters):
    """Calculate the BMI."""
    return round(weight / (height_meters ** 2), 1)

def determine_bmi_level(BMI):
    """Determine the BMI level based on the BMI value."""
    bmi_levels = ['Severe Underweight', 'Underweight', 'Normal', 'Overweight', 'Obesity', 'Severe Obesity']
    thresholds = [13, 18.5, 25, 30, 43]
    return next((label for label, threshold in zip(bmi_levels, thresholds) if BMI <= threshold), bmi_levels[-1])

def calculate_dial_rotation(BMI):
    """Calculate the dial rotation for the SVG gauge."""
    rotation_range = 180
    thresholds = [13, 18.5, 25, 30, 43]
    
    # Normalize the BMI to the rotation range
    normalized_bmi = max(min(BMI, thresholds[-1]), thresholds[0])
    return round(((normalized_bmi - thresholds[0]) / (thresholds[-1] - thresholds[0])) * rotation_range)

def create_gauge_svg(BMI, dial_rotation):
    """Create the SVG gauge with animation."""
    return f"""
    <svg width="300" height="163" viewBox="0 0 300 163">
        <g transform="translate(18,18)" font-family="Arial" font-size="12">
            <path d="M0 140 A140 140 0 0 1 280 140 L140 140 Z" fill="#bc2020"></path>
            <path d="M12.1 83.1 A140 140 0 0 1 280 140 L140 140 Z" fill="#ffe400"></path>
            <path d="M96.7 6.9 A140 140 0 0 1 280 140 L140 140 Z" fill="#008137"></path>
            <path d="M233.7 36 A140 140 0 0 1 280 140 L140 140 Z" fill="#bc2020"></path>
            <circle cx="140" cy="140" r="5" fill="#666"></circle>
            <line x1="140" y1="140" x2="65" y2="140" stroke="#666" stroke-width="2" transform="rotate({dial_rotation} 140 140)" />
            <text x="67" y="120" font-size="30" font-weight="bold">BMI = {BMI}</text>
        </g>
    </svg>
    """
