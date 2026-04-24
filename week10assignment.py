def streaming_report(raw_data, threshold_str):
    entries = [entry.strip() for entry in raw_data.split("|") if entry.strip()] # Strip whitespace, split by pipe, and handle uneven spacing
    platform_map = {}
    for entry in entries:
        name, count = entry.split(":")  # Split on colon, strip both parts, and convert count to float
        platform_map[name.strip()] = float(count.strip())
    platform_list = list(platform_map.items())
    num_platforms = len(platform_list)
    total_subscribers = sum(platform_map.values())
    avg_subscribers = round(total_subscribers / num_platforms, 1) if num_platforms > 0 else 0
    largest_item = max(platform_list, key=lambda x: x[1]) # Using key=lambda to sort by the subscriber count (index 1 of the tuple)
    smallest_item = min(platform_list, key=lambda x: x[1])
    largest_str = f"{largest_item[0]} ({largest_item[1]}M)"
    smallest_str = f"{smallest_item[0]} ({smallest_item[1]}M)"
    threshold = float(threshold_str)# 4. Count platforms above threshold
    above_threshold_count = sum(1 for sub in platform_map.values() if sub >= threshold)
    sorted_platforms = sorted(platform_list, key=lambda x: x[1], reverse=True)# Sort items by subscribers descending
    ranking_parts = []
    for i, (name, count) in enumerate(sorted_platforms, 1):
        ranking_parts.append(f"{i}. {name} ({count})")
    ranking_string = ", ".join(ranking_parts)
    return {
        "platforms": num_platforms,
        "average": avg_subscribers,
        "largest": largest_str,
        "smallest": smallest_str,
        "above_20M": above_threshold_count, 
        "ranking": ranking_string
    }
result = streaming_report(
    " StreamMax: 45.2 | WatchIt: 18.7 | PlayHub: 32.5 | FlickZone: 8.1 | CinePass: 27.4 ", 
    "20.0"
)
print(result)
