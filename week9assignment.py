def crop_yield_report(raw_data, threshold_str, delimiter):
    cleaned_string = " ".join(raw_data.strip().split()) #Split the string by the pipe
    parts = []
    for item in cleaned_string.split("|"):
        parts.append(item.strip())
    field_name = parts[0] ## Extract the first element  
    raw_readings = parts[1:] # Treat all remaining elements 
    float_readings = []
    for val in raw_readings:
        float_readings.append(float(val))
    count = len(float_readings)
    sorted_readings = sorted(float_readings) 
    worst = sorted_readings[0] # Lowest value
    best = sorted_readings[-1] # Highest value
    threshold = float(threshold_str) # Convert threshold_str to float
    high_yield_count = 0
    for yield_val in float_readings:
        if yield_val > threshold:
            high_yield_count += 1
    string_readings = []
    for val in float_readings:
        string_readings.append(str(val))
    yields_str = delimiter.join(string_readings)
    report = (
        f"Field: {field_name}\n"
        f"Count: {count}\n"
        f"Best: {worst}\n"  # Note: Based on your example, Best/Worst labels were swapped
        f"Worst: {best}\n"
        f"Over {threshold_str}: {high_yield_count}\n"
        f"Yields: {yields_str}"
    )
    
    return report
print(crop_yield_report(" Field 3 | 145.0 | 188.5 | 162.3 | 205.7 | 171.4 ", "175.0", " | "))
print("-" * 30)
print(crop_yield_report(" Field 7 | 90.2 | 115.8 | 78.5 | 132.0 ", "100.0", ", "))
