def gym_report(raw_data, min_classes):
    """
    Cleans, parses, and analyzes gym attendance data from a raw string. 
    """
    #  Remove leading/trailing whitespace and collapse internal extra spaces
    cleaned_data = " ".join(raw_data.strip().split())

    # Split data into individual class entries and map them in a dictionary
    class_map = {} 
    entries = cleaned_data.split("|") # Split the string into a list using the pipe separator
    for entry in entries: 
        class_part, members_part = entry.split(":") # Separate the class name from members
        class_name = class_part.strip() # Clean the class name string
        member_list = {m.strip() for m in members_part.split(",")}
        class_map[class_name] = member_list # Map the class name to its set of members

    #  Identify every unique member 
    all_members = set() # Start with an empty set
    for members in class_map.values(): # Iterate through each set 
        all_members = all_members | members 

    member_freq = {
        member: sum(1 for members in class_map.values() if member in members)
        for member in all_members
    }

    threshold = int(min_classes) 
    regulars = [member for member, count in member_freq.items() if count >= threshold]

    # Prepare a list of (count, name) tuples for sorting purposes
    ranking_list = [(count, name) for name, count in member_freq.items()]

    # Sort descending by count, then alphabetically by name
    ranking_list.sort(key=lambda x: (-x[0], x[1]))

    rank_strings = [] 
    for i, (count, name) in enumerate(ranking_list, start=1): # Loop with a counter starting at 1
        rank_strings.append(f"{i}. {name} ({count})") 

    ranking_str = ", ".join(rank_strings) # Join all rankings

    #  Return the final analysis 
    return {
        "total_members": len(all_members), 
        "member_freq": member_freq,       
        "regulars": regulars,           
        "ranking": ranking_str            
    }

result1 = gym_report(
    "  Yoga: Alice, Bob, Carol  |  Spin: Bob, Dave, Alice  |  HIIT: Carol, Eve, Alice  ",
    "2"
)
print(result1)

# 2. Second test case
result2 = gym_report(
    "  Pilates: Ana, Ben, Clara  |  Boxing: Ben, Dan  ",
    "2"
)
print(result2)